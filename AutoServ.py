import os
import random
import platform
import subprocess
from time import sleep as s
import time
import colorama
colorama.init(autoreset=True)

bye_txt = ["GoodBye", "See You", "Bye Bye", "Have a Great Time"]

b = r'''                                                                         
      db                mm             .M"""bgd                             
     ;MM:               MM            ,MI    "Y                             
    ,V^MM. `7MM  `7MM mmMMmm ,pW"Wq.  `MMb.      .gP"Ya `7Mb,od8 `7M'   `MF'
   ,M  `MM   MM    MM   MM  6W'   `Wb   `YMMNq. ,M'   Yb  MM' "'   VA   ,V'''

b2 = r'''   AbmmmqMA  MM    MM   MM  8M     M8 .     `MM 8M""""""  MM        VA ,V   
  A'     VML MM    MM   MM  YA.   ,A9 Mb     dM YM.    ,  MM         VVV    
.AMA.   .AMMA`Mbod"YML. `Mbmo`Ybmd9'  P"Ybmmd"   `Mbmmd'.JMML.        W'''

def banner():
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + b)
    print(colorama.Fore.RED + colorama.Style.BRIGHT + b2)
    print("")

os.system("clear")
banner()

if platform.system() == "Windows":
    print("")
    print(colorama.Fore.RED + "[-] The Script is Only for UNEX Systems")
    print("")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[UwU] {random.choice(bye_txt)}")
    exit(0)
else:
    pass

if os.getenv("SUDO_USER") == None:
    print("")
    print(colorama.Fore.RED + "[-] Please Run The Script As Root | Try 'sudo python3 AutoServ.py'")
    print("")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[UwU] {random.choice(bye_txt)}")
    exit(0)
else:
    pass

print("")
print(colorama.Fore.CYAN + colorama.Style.BRIGHT + f"[+] Updating Linux..")
print("")

try:
    while True:
        try:
            os.system("sudo apt-get update")
            print("")
            print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[+] System Update Successful!")
            print("")
            break
        except:
            print(colorama.Fore.RED + "[-] Update Failed...")
            print("")
            inp = input(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[?] Do You Want To Retry (y/n): ")
            if inp == "y" or inp == "yes":
                continue
            else:
                break
    time.sleep(3)
    os.system("clear")
    banner()
    print("")
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[=] Starting Default Services")
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "=============================>")
    print("")
    os.system("service apache2 start")
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.GREEN + '●'}{colorama.Fore.WHITE + '] Service Apache2 Started'}")
    s(0.5)
    os.system("service postgresql start")
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.GREEN + '●'}{colorama.Fore.WHITE + '] Service PostGreSql Started'}")
    s(0.5)
    os.system("service tor start")
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.GREEN + '●'}{colorama.Fore.WHITE + '] Service Tor Started'}")
    s(2)
    while True:
        os.system("clear")
        banner()
        print("")
        inp2 = input(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[?] Do You Want To Stop All The Services (y/n): ")
        if inp2 == "y":
            os.system("clear")
            banner()
            print("")
            print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[=] Stopping Default Services")
            print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "=============================>")
            print("")
            os.system("service apache2 stop")
            print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.RED + '●'}{ colorama.Fore.WHITE + '] Service Apache2 Stopped'}")
            s(0.5)
            os.system("service postgresql stop")
            print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.RED + '●'}{colorama.Fore.WHITE + '] Service PostGreSql Stopped'}")
            s(0.5)
            os.system("service tor stop")
            print(colorama.Fore.WHITE + colorama.Style.BRIGHT + f"[{colorama.Fore.RED + '●'}{colorama.Fore.WHITE + '] Service Tor Stopped'}")
            print("")
            s(2)
            break
        elif inp2 == "n" or inp2 == "":
            break
        else:
            os.system("clear")
            banner()
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "[-] Please Select A Valid Option")
            s(1.75)
            continue

    while True:
        os.system("clear")
        banner()
        print("")
        print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[=] Checking For Updates..")
        print("")
        upgradables = subprocess.run("sudo apt list --upgradable", shell=True, capture_output=True).stdout.decode()
        upgradables = upgradables.rstrip()
        if upgradables == "Listing...":
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[++] System Up-To Date!")
            time.sleep(3)
            break
        else:
            time.sleep(3)
            os.system("clear")
            banner()
            print("")
            print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[+] These are The Packages that can be Upgraded...")
            print("")
            print(colorama.Fore.RED + colorama.Style.BRIGHT + upgradables)
            print("")
        inp3 = input(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[?] Do You Want To Upgrade the System (y/n): ")
        if inp3 == "y":
            os.system("clear")
            banner()
            print("")
            print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[=] Preparing For Upgrade")
            os.system("sudo dpkg --configure -a")
            print("")
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[++] Done")
            print("")
            while True:
                inp4 = input(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[?] 1) Full-Upgrade type | 2) Normal Upgrade type (n) | Or Enter To Exit: ")
                if inp4 == "1":
                    os.system("clear")
                    banner()
                    print("")
                    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[+] Full-Upgrading Linux...")
                    print("")
                    os.system("sudo apt full-upgrade -y")
                    print("")
                    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[++] System Upgrade Successful!")
                    time.sleep(3)
                    break
                elif inp4 == "2":
                    os.system("clear")
                    banner()
                    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[+] Upgrading Linux...")
                    print("")
                    os.system("sudo apt upgrade")
                    print("")
                    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[++] System Upgrade Successful!")
                    time.sleep(3)
                    break
                elif inp4 == "":
                    break
                elif inp4 != "1" or inp4 != "2" or inp4 != "":
                    os.system("clear")
                    banner()
                    print("")
                    print(colorama.Fore.RED + colorama.Style.BRIGHT + "[-] Please Select A Valid Option")
                    s(1.75)
                    os.system("clear")
                    continue
            break
        elif inp3 == "n":
            break
        elif inp3 != "y" or inp3 != "n":
            os.system("clear")
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "[-] Please Select A Valid Option")
            s(1.75)
            continue

    os.system("clear")
    banner()
    print("")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[=] Auto-Removing Unwanted Update Files")
    print("")
    os.system("sudo apt autoremove")
    print("")
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "[++] Auto-Remove Successful!")
    time.sleep(3)
    os.system("clear")
    banner()
    print("")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[UwU] {random.choice(bye_txt)}")
    exit(0)

except KeyboardInterrupt:
    print("")
    print("")
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "[-] Exiting AutoServ")
    print("")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[UwU] {random.choice(bye_txt)}")
    exit(0)
