# backend/linker.py
# =============================================================================
#  الربط النهائي: LLVM object + Arduino glue + Arduino core → .elf → .hex
# -----------------------------------------------------------------------------
#  يجمع ملف الكائن القادم من المترجم مع طبقة الربط (arduino_glue.cpp) ونواة
# // Arduino المبنية مسبقاً (core.a) لإنتاج ملفات firmware.elf و firmware.hex
# // الجاهزتين للرفع على لوحة Arduino Uno / Nano (ATmega328P).
# // =============================================================================

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

from backend.avr_target import AVR_CPU, AVR_TRIPLE

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOCAL_TOOLCHAIN_DIR = PROJECT_ROOT / "tools" / "arduino-cli"
LOCAL_AVR_GCC_DIR = LOCAL_TOOLCHAIN_DIR / "data" / "packages" / "arduino" / "tools" / "avr-gcc"
LOCAL_CORE_A = PROJECT_ROOT / "runtime" / "core.a"

DEFAULT_MCU = AVR_CPU
DEFAULT_FCPU = "16000000L"
DEFAULT_PORT_WINDOWS = "COM3"
DEFAULT_PORT_LINUX = "/dev/ttyACM0"
DEFAULT_BAUD = "115200"


class LinkError(RuntimeError):
    """خطأ أثناء عملية الربط أو التحويل إلى HEX."""


def _find_local_avr_bin_dir() -> Optional[Path]:
    """البحث عن مجلد bin الخاص بـ avr-gcc المحلي داخل أدوات المشروع."""
    if not LOCAL_AVR_GCC_DIR.exists():
        return None
    try:
        versions = [d for d in LOCAL_AVR_GCC_DIR.iterdir() if d.is_dir()]
        if not versions:
            return None
        # نستخدم أحدث إصدار (ترتيب أبجدي يكفي عادةً)
        versions.sort()
        bin_dir = versions[-1] / "bin"
        if bin_dir.exists():
            return bin_dir
    except Exception:
        pass
    return None


def _find_executable(name: str) -> Optional[str]:
    """البحث عن أمر: أولاً محلياً، ثم في PATH."""
    # أدوات avr-gcc (g++, objcopy, size, ...)
    local_bin = _find_local_avr_bin_dir()
    if local_bin:
        local_exe = local_bin / (name + ".exe" if sys.platform == "win32" else name)
        if local_exe.exists():
            return str(local_exe)
    # أداة avrdude لها مجلد منفصل
    if name == "avrdude":
        local_avrdude = LOCAL_TOOLCHAIN_DIR / "data" / "packages" / "arduino" / "tools" / "avrdude"
        if local_avrdude.exists():
            versions = [d for d in local_avrdude.iterdir() if d.is_dir()]
            if versions:
                versions.sort()
                avrdude_exe = versions[-1] / "bin" / "avrdude.exe"
                if avrdude_exe.exists():
                    return str(avrdude_exe)
    return shutil.which(name)


def _find_local_arduino_cli_core() -> Optional[Path]:
    """البحث عن نواة Arduino AVR داخل بيانات arduino-cli المحلية."""
    local_core = LOCAL_TOOLCHAIN_DIR / "data" / "packages" / "arduino" / "hardware" / "avr"
    if local_core.exists():
        versions = [d for d in local_core.iterdir() if d.is_dir()]
        if versions:
            versions.sort()
            return versions[-1]
    return None


def _find_arduino_cli_core() -> Optional[Path]:
    """محاولة اكتشاف مسار نواة Arduino AVR عبر arduino-cli."""
    local = _find_local_arduino_cli_core()
    if local:
        return local

    cli = shutil.which("arduino-cli")
    if not cli:
        return None
    try:
        out = subprocess.check_output(
            [cli, "core", "list", "--format", "json"],
            stderr=subprocess.DEVNULL,
            text=True,
        )
        import json
        cores = json.loads(out)
        for core in cores:
            if core.get("id") == "arduino:avr":
                install_dir = core.get("install_dir") or core.get("InstallationPath")
                if install_dir:
                    return Path(install_dir)
    except Exception:
        pass
    return None


def _find_core_a(core_dir: Path) -> Optional[Path]:
    """البحث عن ملف core.a داخل مجلد النواة أو مجلدات البناء المؤقتة."""
    # البحث المباشر
    for candidate in (
        core_dir / "core.a",
        core_dir / "variants" / "standard" / "core.a",
    ):
        if candidate.exists():
            return candidate

    # البحث في مجلدات البناء المؤقتة لـ arduino-cli
    import tempfile
    tmp_root = Path(tempfile.gettempdir())
    try:
        for sub in tmp_root.iterdir():
            if sub.is_dir() and "arduino" in sub.name.lower():
                for candidate in sub.rglob("core.a"):
                    if candidate.exists():
                        return candidate
    except Exception:
        pass
    return None


def _guess_arduino_paths() -> dict:
    """تجميع أفضل تخمين لمسارات النواة والمتغير والنواة المبنية."""
    # أولوية لـ core.a المبني مسبقاً داخل runtime/
    if LOCAL_CORE_A.exists():
        local_core_dir = _find_local_arduino_cli_core()
        if local_core_dir:
            return {
                "core_dir": local_core_dir,
                "core_inc": local_core_dir / "cores" / "arduino",
                "variant_inc": local_core_dir / "variants" / "standard",
                "core_a": LOCAL_CORE_A,
            }

    core_dir = _find_arduino_cli_core()
    if core_dir:
        core_root = core_dir / "cores" / "arduino"
        variant_dir = core_dir / "variants" / "standard"
        core_a = _find_core_a(core_dir)
        return {
            "core_dir": core_dir,
            "core_inc": core_root if core_root.exists() else None,
            "variant_inc": variant_dir if variant_dir.exists() else None,
            "core_a": core_a,
        }
    return {}


def _run(cmd: list, check: bool = True) -> subprocess.CompletedProcess:
    """تشغيل أمر خارجي مع إظهار الخطأ بوضوح."""
    try:
        return subprocess.run(cmd, check=check, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise LinkError(
            f"فشل الأمر: {' '.join(cmd)}\n"
            f"المخرجات القياسية:\n{e.stdout}\n"
            f"المخرجات الخطأ:\n{e.stderr}"
        ) from e


def build_glue(
    glue_cpp: str = "runtime/arduino_glue.cpp",
    out_o: str = "arduino_glue.o",
    mcu: str = DEFAULT_MCU,
    fcpu: str = DEFAULT_FCPU,
    core_inc: Optional[str] = None,
    variant_inc: Optional[str] = None,
) -> Path:
    """تجميع ملف طبقة الربط إلى كائن AVR."""
    avr_gpp = _find_executable("avr-g++")
    if not avr_gpp:
        raise LinkError(
            "لم يتم العثور على avr-g++. الرجاء تثبيت Arduino AVR toolchain:\n"
            "  - Windows/Linux: arduino-cli core install arduino:avr\n"
            "  - Linux: sudo apt install gcc-avr avr-libc binutils-avr"
        )

    cmd = [
        avr_gpp,
        f"-mmcu={mcu}",
        f"-DF_CPU={fcpu}",
        "-Os",
        "-ffunction-sections",
        "-fdata-sections",
        "-c",
        glue_cpp,
        "-o",
        out_o,
    ]
    if core_inc:
        cmd.extend(["-I", core_inc])
    if variant_inc:
        cmd.extend(["-I", variant_inc])

    _run(cmd)
    return Path(out_o)


def link(
    obj: str = "output.o",
    glue_o: str = "arduino_glue.o",
    core_a: Optional[str] = None,
    out_elf: str = "firmware.elf",
    mcu: str = DEFAULT_MCU,
) -> Path:
    """ربط ملفات الكائن مع نواة Arduino لإنتاج firmware.elf."""
    avr_gpp = _find_executable("avr-g++")
    if not avr_gpp:
        raise LinkError("لم يتم العثور على avr-g++.")

    if core_a and not Path(core_a).exists():
        raise LinkError(f"ملف النواة غير موجود: {core_a}")

    cmd = [
        avr_gpp,
        f"-mmcu={mcu}",
        "-Os",
        "-Wl,--gc-sections",
        obj,
        glue_o,
    ]
    if core_a:
        cmd.append(core_a)
    cmd.extend(["-o", out_elf])

    _run(cmd)
    return Path(out_elf)


def elf_to_hex(elf: str = "firmware.elf", out_hex: str = "firmware.hex") -> Path:
    """تحويل firmware.elf إلى Intel HEX."""
    avr_objcopy = _find_executable("avr-objcopy")
    if not avr_objcopy:
        raise LinkError("لم يتم العثور على avr-objcopy.")

    _run([
        avr_objcopy,
        "-O", "ihex",
        "-R", ".eeprom",
        elf,
        out_hex,
    ])
    return Path(out_hex)


def size_report(elf: str = "firmware.elf", mcu: str = DEFAULT_MCU) -> str:
    """طباعة تقرير استهلاك الذاكرة."""
    avr_size = _find_executable("avr-size")
    if not avr_size:
        return "[تحذير] avr-size غير متوفر."
    result = _run([avr_size, f"--mcu={mcu}", "-C", elf])
    return result.stdout


def flash_hex(
    hex_path: str = "firmware.hex",
    port: Optional[str] = None,
    mcu: str = DEFAULT_MCU,
    baud: str = DEFAULT_BAUD,
) -> None:
    """رفع ملف HEX على اللوحة باستخدام avrdude."""
    avrdude = _find_executable("avrdude")
    if not avrdude:
        raise LinkError("لم يتم العثور على avrdude.")

    if port is None:
        port = DEFAULT_PORT_LINUX if sys.platform != "win32" else DEFAULT_PORT_WINDOWS

    _run([
        avrdude,
        "-c", "arduino",
        "-p", mcu,
        "-P", port,
        "-b", baud,
        "-U", f"flash:w:{hex_path}:i",
    ])


def link_and_build_hex(
    obj: str = "output.o",
    glue_cpp: str = "runtime/arduino_glue.cpp",
    out_elf: str = "firmware.elf",
    out_hex: str = "firmware.hex",
    core_a: Optional[str] = None,
    core_inc: Optional[str] = None,
    variant_inc: Optional[str] = None,
    mcu: str = DEFAULT_MCU,
    fcpu: str = DEFAULT_FCPU,
    auto_find_core: bool = True,
    verbose: bool = True,
) -> Path:
    """خطوة واحدة: تجميع Glue + ربط + إنتاج HEX."""
    if auto_find_core and not core_a:
        guessed = _guess_arduino_paths()
        if guessed.get("core_a"):
            core_a = str(guessed["core_a"])
            if not core_inc:
                core_inc = str(guessed["core_inc"]) if guessed.get("core_inc") else None
            if not variant_inc:
                variant_inc = str(guessed["variant_inc"]) if guessed.get("variant_inc") else None
            if verbose:
                print(f"[linker] تم اكتشاف النواة تلقائياً: {core_a}")

    if verbose:
        print("[linker] تجميع طبقة الربط ...")
    build_glue(glue_cpp, "arduino_glue.o", mcu, fcpu, core_inc, variant_inc)

    if verbose:
        print("[linker] ربط الكائنات ...")
    link(obj, "arduino_glue.o", core_a, out_elf, mcu)

    if verbose:
        print("[linker] تحويل ELF إلى HEX ...")
    hex_path = elf_to_hex(out_elf, out_hex)

    if verbose:
        print(f"[linker] ✅ تم إنشاء {hex_path}")
        print(size_report(out_elf, mcu))

    return hex_path


# تشغيل مستقل: python -m backend.linker [output.o] [core.a]
if __name__ == "__main__":
    obj_file = sys.argv[1] if len(sys.argv) > 1 else "output.o"
    core_file = sys.argv[2] if len(sys.argv) > 2 else None
    link_and_build_hex(obj=obj_file, core_a=core_file, verbose=True)
