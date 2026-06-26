#!/usr/bin/env python3
"""
build.py — مساعد بناء سريع للمترجم.

الاستخدام:
  python build.py compile                # تشغيل main.py بالكامل
  python build.py test                   # تشغيل اختبارات الخلفية
  python build.py link [core.a]          # ربط output.o مع النواة
  python build.py flash [PORT]           # رفع firmware.hex على اللوحة
  python build.py ports                  # عرض المنافذ المتاحة
  python build.py monitor [PORT] [BAUD]  # فتح السيريال مونيتور (للـ IDE)
  python build.py clean                  # حذف الملفات المولّدة
"""

import argparse
import os
import subprocess
import sys
import time
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
    res =  subprocess.run([PYTHON, "main.py"], check=False)
    if res.returncode!=0:
        sys.exit(1)


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
        print(f"\n⚠️ فشل الربط:\n{e}")
        sys.exit(1)

def cmd_flash(args):
    from backend.linker import flash_hex
    port = args.port or (DEFAULT_PORT_LINUX if sys.platform != "win32" else DEFAULT_PORT_WINDOWS)
    try:
        flash_hex(hex_path="firmware.hex", port=port)
        print(f"✅ تم الرفع على {port}")
    except Exception as e:
        print(f"⚠️ فشل الرفع: {e}")
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

def cmd_monitor(args):
    """جسر بين منفذ السيريال و stdio لاستخدامه من الـ IDE.
    - بايتات من اللوحة  -> stdout (يقرأها محول الـ IDE)
    - أسطر من stdin     -> تُرسَل إلى اللوحة
    يتوقف عند إغلاق stdin (الـ IDE يغلق المونيتور) أو عند خطأ في السيريال.
    """
    import threading
    try:
        import serial  # pyserial
    except ImportError:
        print("pyserial غير مثبت. شغّل: pip install -r requirements.txt",
              file=sys.stderr, flush=True)
        sys.exit(1)

    port = args.port or (DEFAULT_PORT_LINUX if sys.platform != "win32" else DEFAULT_PORT_WINDOWS)
    baud = args.baud

    try:
        ser = serial.Serial(port, baud, timeout=0.1)
    except serial.SerialException as e:
        print(f"SERIAL_ERROR: {e}", file=sys.stderr, flush=True)
        sys.exit(1)

    # إعادة ضبط لوحة Uno (نبضة DTR) لالتقاط مخرجات اعداد()/setup():
    # سطر الترحيب وكامل دفعة الأرقام، تماماً كما يفعل Arduino IDE الرسمي.
    ser.dtr = False
    time.sleep(0.1)
    ser.reset_input_buffer()
    ser.dtr = True
    time.sleep(0.05)

    stop = threading.Event()

    def reader():
        while not stop.is_set():
            try:
                data = ser.read(256)
            except serial.SerialException as e:
                print(f"SERIAL_ERROR: {e}", file=sys.stderr, flush=True)
                stop.set()
                break
            if data:
                # نمرّر البايتات كما هي إلى stdout؛ محول الـ IDE يفك UTF-8
                # ويقسّم الأسطر. errors="replace" يبقي التدفق حيّاً عند
                # وصول UTF-8 جزئي (للعربية).
                sys.stdout.write(data.decode("utf-8", errors="replace"))
                sys.stdout.flush()

    t = threading.Thread(target=reader, daemon=True)
    t.start()

    # يقرأ الرسائل الصادرة من stdin حتى يغلق الـ IDE المنفذ (stdin EOF).
    try:
        for line in sys.stdin:
            ser.write(line.rstrip("\n").encode("utf-8") + b"\n")
    except (serial.SerialException, BrokenPipeError):
        pass
    finally:
        stop.set()
        t.join(timeout=1)
        ser.close()

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

    p_monitor = sub.add_parser("monitor", help="فتح السيريال مونيتور على منفذ")
    p_monitor.add_argument("port", nargs="?", default=None, help="منفذ اللوحة (COM3 / /dev/ttyACM0)")
    p_monitor.add_argument("baud", nargs="?", type=int, default=9600, help="سرعة الاتصال (baud)")

    sub.add_parser("clean", help="حذف الملفات المولّدة")

    args = parser.parse_args()

    commands = {
        "compile": cmd_compile,
        "test": cmd_test,
        "setup": cmd_setup,
        "link": cmd_link,
        "flash": cmd_flash,
        "ports": cmd_ports,
        "monitor": cmd_monitor,
        "clean": cmd_clean,
    }
    commands[args.command](args)

if __name__ == "__main__":
    main()