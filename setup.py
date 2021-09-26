from subprocess import run
from colorama import Fore, Style
import colorama
colorama.init(autoreset=True)

print()
print(Fore.CYAN + Style.BRIGHT + "[*] Installing Tor Service")
run("sudo apt-get install tor", capture_output=True, shell=True)
print(Fore.CYAN + Style.BRIGHT + "[*] Installing Postgresql Service")
run("sudo apt-get install postgresql", capture_output=True, shell=True)
print(Fore.CYAN + Style.BRIGHT + "[*] Installing Apache2 Service")
run("sudo apt-get install apache2", capture_output=True, shell=True)
print()
print(Fore.GREEN + Style.BRIGHT + "[+] Done")
