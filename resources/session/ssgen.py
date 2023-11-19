#!/usr/bin/python3
# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os
from time import sleep

ULTROID = r"""
                                                                                          
88b           d88          ,d8  I8,        8        ,8I  88  888b      88    ,ad8888ba,   
888b         d888        ,d888  `8b       d8b       d8'  88  8888b     88   d8"'    `"8b  
88`8b       d8'88      ,d8" 88   "8,     ,8"8,     ,8"   88  88 `8b    88  d8'            
88 `8b     d8' 88    ,d8"   88    Y8     8P Y8     8P    88  88  `8b   88  88             
88  `8b   d8'  88  ,d8"     88    `8b   d8' `8b   d8'    88  88   `8b  88  88      88888  
88   `8b d8'   88  8888888888888   `8a a8'   `8a a8'     88  88    `8b 88  Y8,        88  
88    `888'    88           88      `8a8'     `8a8'      88  88     `8888   Y8a.    .a88  
88     `8'     88           88       `8'       `8'       88  88      `888    `"Y88888P"   
                                                                                          
                                                                                          
"""


def spinner(x):
    if x == "tele":
        print("Checking if Telethon is installed...")
    else:
        print("Checking if Pyrogram is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org or @ScrapperRoBot to proceed.\n\n",
    )
    try:
        API_ID = int(input("ASUPKEUN API ID : "))
    except ValueError:
        print("APP ID na teu baleg.\nQuitting...")
        exit(0)
    API_HASH = input("Asupkeun API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")
        import telethon
        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except ImportError:
        print("Installing Telethon...")
        os.system("pip uninstall telethon -y && pip install -U telethon")

        x = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(ULTROID)
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as ultroid:
            print("Generating a string session for •M4WING•")
            try:
                ultroid.send_message(
                    "me",
                    f"**M4WING** `SESSION`:\n\n`{ultroid.session.save()}`\n\n**Do not share this anywhere!**",
                )
                print(
                    "SESSION na nggs jadi, sok cobaan di cek di PESAN TERSIMPAN!"
                )
                return
            except UserIsBotError:
                print("You are trying to Generate Session for your Bot's Account?")
                print("Here is That!\n{ultroid.session.save()}\n\n")
                print("NOTE: You can't use that as User Session..")
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)
    except Exception as er:
        print("Unexpected Error Occurred while Creating Session")
        print(er)
        print("If you think It as a Bug, Report to @UltroidSupportChat.\n\n")


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bFound an existing installation of Pyrogram...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bDone. Installed and imported Pyrogram."
        from pyrogram import Client
        
    clear_screen()
    print(ULTROID)
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("Enter phone number when asked.\n\n")
    try:
        with Client(name="ultroid", api_id=API_ID, api_hash=API_HASH, in_memory=True) as pyro:
            ss = pyro.export_session_string()
            pyro.send_message(
                "me",
                f"`{ss}`\n\nAbove is your Pyrogram Session String for @TheUltroid. **DO NOT SHARE it.**",
            )
            print("Session has been sent to your saved messages!")
            exit(0)
    except Exception as er:
      print("Unexpected error occurred while creating session, make sure to validate your inputs.")
      print(er)


def main():
    clear_screen()
    print(ULTROID)
    try:
        type_of_ss = int(
            input(
                "\nM4wing supports both telethon as well as pyrogram sessions.\n\nWhich session do you want to generate?\n1. Telethon Session.\n2. Pyrogram Session.\n\nEnter choice:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        telethon_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("Invalid choice.")
    x = input("Jalankeun deui? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)


main()
