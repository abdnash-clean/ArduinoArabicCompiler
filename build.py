#!/usr/bin/env python3
"""
build.py — مساعد بناء سريع للمترجم.

الاستخدام:
    python build.py compile          # تشغيل main.py بالكامل
    python build.py test             # تشغيل اختبارات الخلفية
    python build.py link [core.a]    # ربط output.o مع النواة
    python build.py flash [PORT]     # رفع firmware.hex على اللوحة
    python build.py clean            # حذف الملفات المولّدة
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# التأكد من تشغيل الأوامر من جذر المشروع
PROJECT_ROOT = Path(__file__).resolve().parent
os.chdir(PROJECT_ROOT)

PYTHON = sys.executable
DEFAULT_PORT_WINDOWS = "COM3"
DEFAULT_PORT_LINUX = "/dev/ttyACM0"


def run(cmd, check=True):
    print(f"$ {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=check)
    except subprocess.CalledProcessError as e:
        print(f"فشل الأمر (exit {e.returncode})")
        sys.exit(e.returncode)


def cmd_setup(args):
    print("[build] تثبيت Arduino AVR toolchain ...")
    run([PYTHON, "tools/setup_avr_toolchain.py"])
    print("[build] بناء core.a ...")
    run([PYTHON, "tools/build_core.py"])
    print("[build] ✅ جاهز للترجمة والربط.")


def cmd_compile(args):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    run([PYTHON, "main.py"], check=False)


def cmd_test(args):
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    run([PYTHON, "-m", "unittest", "backend.tests.test_backend", "-v"])


def cmd_link(args):
    from backend.linker import link_and_build_hex, LinkError
    try:
        link_and_build_hex(
            obj="output.o",
            core_a=args.core,
            verbose=True,
        )
    except LinkError as e:
        print(f"\n⚠️  فشل الربط:\n{e}")
        sys.exit(1)


def cmd_flash(args):
    from backend.linker import flash_hex
    port = args.port or (DEFAULT_PORT_LINUX if sys.platform != "win32" else DEFAULT_PORT_WINDOWS)
    try:
        flash_hex(hex_path="firmware.hex", port=port)
        print(f"✅ تم الرفع على {port}")
    except Exception as e:
        print(f"⚠️  فشل الرفع: {e}")
        sys.exit(1)


def cmd_ports(args):
    from backend.linker import _find_executable
    arduino_cli = PROJECT_ROOT / "tools" / "arduino-cli" / "bin" / "arduino-cli.exe"
    if arduino_cli.exists():
        env = os.environ.copy()
        env["ARDUINO_DATA_DIR"] = str(PROJECT_ROOT / "tools" / "arduino-cli" / "data")
        env["ARDUINO_CONFIG_DIR"] = str(PROJECT_ROOT / "tools" / "arduino-cli" / "config")
        subprocess.run([str(arduino_cli), "board", "list"], env=env)
    else:
        print("arduino-cli غير مثبت. استخدم: python build.py setup")


def cmd_clean(args):
    files_to_remove = [
        "output.o", "output.s", "arduino_glue.o",
        "firmware.elf", "firmware.hex",
        "debug.ll", "parse_tree.png",
    ]
    for name in files_to_remove:
        path = PROJECT_ROOT / name
        if path.exists():
            path.unlink()
            print(f"حُذف: {name}")


def main():
    parser = argparse.ArgumentParser(description="مساعد بناء Arduino Arabic Compiler")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("compile", help="تشغيل main.py")
    sub.add_parser("test", help="تشغيل اختبارات الخلفية")
    sub.add_parser("setup", help="تثبيت Arduino AVR toolchain وبناء core.a")

    p_link = sub.add_parser("link", help="ربط output.o مع النواة")
    p_link.add_argument("core", nargs="?", default=None, help="مسار core.a")

    p_flash = sub.add_parser("flash", help="رفع firmware.hex على اللوحة")
    p_flash.add_argument("port", nargs="?", default=None, help="منفذ اللوحة (COM3 / /dev/ttyACM0)")

    sub.add_parser("ports", help="عرض المنافذ المتاحة / اللوحات المتصلة")

    sub.add_parser("clean", help="حذف الملفات المولّدة")

    args = parser.parse_args()

    commands = {
        "compile": cmd_compile,
        "test": cmd_test,
        "setup": cmd_setup,
        "link": cmd_link,
        "flash": cmd_flash,
        "ports": cmd_ports,
        "clean": cmd_clean,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
