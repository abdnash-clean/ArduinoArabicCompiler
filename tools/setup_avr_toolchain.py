#!/usr/bin/env python3
"""
tools/setup_avr_toolchain.py
=============================================================================
يقوم بتنزيل arduino-cli المحمول وتثبيت نواة arduino:avr داخل مجلد المشروع.

الاستخدام:
    python tools/setup_avr_toolchain.py

بعد الاكتمال:
    - tools/arduino-cli/arduino-cli.exe
    - tools/arduino-cli/data/... (cores, packages)

يمكن لـ backend/linker.py استخدام هذه الأدوات تلقائياً.
=============================================================================
"""

import json
import os
import platform
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = PROJECT_ROOT / "tools" / "arduino-cli"
CLI_DIR = TOOLS_DIR / "bin"
DATA_DIR = TOOLS_DIR / "data"
CONFIG_DIR = TOOLS_DIR / "config"

GITHUB_API_URL = "https://api.github.com/repos/arduino/arduino-cli/releases/latest"


def ensure_dirs():
    CLI_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def cli_path() -> Path:
    if platform.system() == "Windows":
        return CLI_DIR / "arduino-cli.exe"
    return CLI_DIR / "arduino-cli"


def is_installed() -> bool:
    return cli_path().exists()


def _fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (ArduinoArabicCompiler setup)",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def _get_download_url() -> str:
    print("[setup] البحث عن أحدث إصدار من arduino-cli ...")
    release = _fetch_json(GITHUB_API_URL)
    version = release.get("tag_name", "unknown")
    print(f"[setup] أحدث إصدار: {version}")

    # اختيار أصل zip المناسب لنظام التشغيل
    system = platform.system()
    machine = platform.machine().lower()
    if system == "Windows":
        suffix = "Windows_64bit.zip"
    elif system == "Darwin":
        suffix = "macOS_64bit.tar.gz" if machine == "x86_64" else "macOS_ARM64.tar.gz"
    else:
        suffix = "Linux_64bit.tar.gz" if machine in ("x86_64", "amd64") else "Linux_ARM64.tar.gz"

    for asset in release.get("assets", []):
        name = asset.get("name", "")
        if name.endswith(suffix):
            return asset["browser_download_url"]

    raise RuntimeError(f"لم يُعثر على ملف التنزيل المناسب: {suffix}")


def download_arduino_cli():
    ensure_dirs()
    zip_path = TOOLS_DIR / "arduino-cli.zip"

    if zip_path.exists():
        print(f"[setup] يوجد ملف محمّل مسبقاً: {zip_path}")
    else:
        download_url = _get_download_url()
        print(f"[setup] جاري تنزيل arduino-cli ...")
        print(f"[setup] من: {download_url}")
        print("[setup] قد يستغرق ذلك بضع دقائق حسب سرعة الإنترنت.")
        urllib.request.urlretrieve(download_url, zip_path)
        print(f"[setup] اكتمل التنزيل: {zip_path.stat().st_size / 1024 / 1024:.1f} MB")

    print("[setup] فك الضغط ...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(CLI_DIR)

    if not cli_path().exists():
        raise RuntimeError("فشل فك الضغط أو لم يُعثر على arduino-cli.exe")

    print(f"[setup] ✅ arduino-cli جاهز في: {cli_path()}")


def run_cli(*args, check=True):
    cmd = [str(cli_path()), *args]
    env = os.environ.copy()
    env["ARDUINO_DATA_DIR"] = str(DATA_DIR)
    env["ARDUINO_CONFIG_DIR"] = str(CONFIG_DIR)
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if check and result.returncode != 0:
        raise RuntimeError(f"فشل الأمر: {' '.join(cmd)} (exit {result.returncode})")
    return result


def install_avr_core():
    print("[setup] تحديث فهرس النواة ...")
    run_cli("core", "update-index")

    print("[setup] تثبيت نواة arduino:avr ...")
    run_cli("core", "install", "arduino:avr")

    print("[setup] ✅ تم تثبيت نواة arduino:avr")


def print_paths():
    print("\n[setup] معلومات المسارات:")
    print(f"  arduino-cli: {cli_path()}")
    print(f"  data dir:    {DATA_DIR}")
    print(f"\nيمكنك الآن تشغيل:")
    print(f"  python build.py compile")
    print(f"  python build.py link")
    print(f"  python build.py flash")


def main():
    if is_installed():
        print(f"[setup] arduino-cli موجود بالفعل في {cli_path()}")
    else:
        download_arduino_cli()

    # التحقق من تثبيت النواة
    try:
        run_cli("core", "list", check=False)
    except Exception as e:
        print(f"[setup] تحذير: {e}")

    # نحاول تثبيت النواة دائماً (إذا كانت مثبتة فلن يحدث شيء)
    try:
        install_avr_core()
    except RuntimeError as e:
        print(f"[setup] ⚠️  فشل تثبيت النواة: {e}")
        print("[setup] يمكنك إعادة المحاولة لاحقاً بـ:")
        print(f"  python {__file__}")
        sys.exit(1)

    print_paths()


if __name__ == "__main__":
    main()
