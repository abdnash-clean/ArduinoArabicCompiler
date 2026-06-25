#!/usr/bin/env python3
"""
tools/build_core.py
=============================================================================
يبني ملف core.a الخاص بنواة Arduino AVR باستخدام arduino-cli.

الاستخدام:
    python tools/build_core.py

النتيجة:
    runtime/core.a — جاهز للربط مع output.o و arduino_glue.o.
=============================================================================
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIR = PROJECT_ROOT / "runtime"
OUTPUT_CORE = RUNTIME_DIR / "core.a"


def find_arduino_cli() -> Path:
    # أولوية للنسخة المحلية
    local = PROJECT_ROOT / "tools" / "arduino-cli" / "bin" / "arduino-cli.exe"
    if local.exists():
        return local

    system = shutil.which("arduino-cli")
    if system:
        return Path(system)

    raise RuntimeError(
        "لم يتم العثور على arduino-cli. الرجاء تشغيل:\n"
        "  python tools/setup_avr_toolchain.py"
    )


def run_cli(*args, env_extra=None, check=True):
    cli = find_arduino_cli()
    cmd = [str(cli), *args]
    env = os.environ.copy()
    env["ARDUINO_DATA_DIR"] = str(PROJECT_ROOT / "tools" / "arduino-cli" / "data")
    env["ARDUINO_CONFIG_DIR"] = str(PROJECT_ROOT / "tools" / "arduino-cli" / "config")
    if env_extra:
        env.update(env_extra)
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if check and result.returncode != 0:
        raise RuntimeError(f"فشل الأمر (exit {result.returncode})")
    return result


def build_core():
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        sketch_dir = Path(tmp) / "dummy_sketch"
        sketch_dir.mkdir()
        sketch_file = sketch_dir / "dummy_sketch.ino"
        sketch_file.write_text("void setup() {}\nvoid loop() {}\n")

        build_dir = Path(tmp) / "build"
        print("[build_core] جاري بناء النواة باستخدام arduino-cli ...")
        run_cli(
            "compile",
            "--fqbn", "arduino:avr:uno",
            "--build-path", str(build_dir),
            str(sketch_dir),
        )

        # core.a يُوضع داخل مجلد core/ تحت build-path
        candidates = list(build_dir.rglob("core/core.a"))
        if not candidates:
            raise RuntimeError("لم يُعثر على core.a بعد البناء.")

        source_core = candidates[0]
        shutil.copy2(source_core, OUTPUT_CORE)
        print(f"[build_core] ✅ تم نسخ النواة إلى: {OUTPUT_CORE}")
        print(f"[build_core] الحجم: {OUTPUT_CORE.stat().st_size / 1024:.1f} KB")


def main():
    try:
        build_core()
    except RuntimeError as e:
        print(f"\n⚠️  {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
