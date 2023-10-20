import platform
import sys
import os

from mod.ssh import SSH_BRUTEFORCE
from mod.ftp import FTP_BRUTEFORCE
from mod.telnet import TELNET_BRUTEFORCE


class Main:
    def __init__(self, mod):
        self.mod = mod
    
    def run(self):
        try:
            if self.mod == "FTP":
                self.clear()
                print("""
                <===FTP BRUTE FORCE===>
                """)
                host = input("Target (Domain / IP): ")
                username = input("Username: ")
                wordlist = input("Wordlist Location: ")

                ftp_bf = FTP_BRUTEFORCE(username, host, wordlist)
                ftp_bf.start()

            elif self.mod == "TELNET":
                self.clear()
                print("""
                <===TELNET BRUTE FORCE===>
                """)
                host = input("Target (Domain / IP): ")
                username = input("Username: ")
                wordlist = input("Wordlist Location: ")
                timeout = int(input("Timeout: "))

                telnet_bf = TELNET_BRUTEFORCE(username, host, wordlist, timeout)
                telnet_bf.start()

            elif self.mod == "SSH":
                self.clear()
                print("""
                <===SSH BRUTE FORCE===>
                """)
                host = input("Target (Domain / IP): ")
                username = input("Username: ")
                wordlist = input("Wordlist Location: ")

                ssh_bf = SSH_BRUTEFORCE(host, username, wordlist)
                ssh_bf.start()

            else:
                print("Invalid Mod")
        
        except KeyboardInterrupt:
            self.clear()
    
    def clear(self):
        if platform.system().lower() == "windows":
            os.system("cls")
        else:
            os.system("clear")

def start(argv):
    if len(argv) <= 1:
        print("""

 ▄▄▄▄    ██▓     █    ██ ▓█████▄      █████▒ ▒█████   ██▀███    ▄████ ▓█████ 
▓█████▄ ▓██▒     ██  ▓██▒▒██▀ ██▌   ▓██   ▒ ▒██▒  ██▒▓██ ▒ ██▒ ██▒ ▀█▒▓█   ▀ 
▒██▒ ▄██▒██░    ▓██  ▒██░░██   █▌   ▒████ ░ ▒██░  ██▒▓██ ░▄█ ▒▒██░▄▄▄░▒███   
▒██░█▀  ▒██░    ▓▓█  ░██░░▓█▄   ▌   ░▓█▒  ░ ▒██   ██░▒██▀▀█▄  ░▓█  ██▓▒▓█  ▄ 
░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▓    ░▒█░    ░ ████▓▒░░██▓ ▒██▒░▒▓███▀▒░▒████▒
░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒  ▒▒▓  ▒     ▒ ░    ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ░▒   ▒ ░░ ▒░ ░
▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ▒  ▒     ░        ░ ▒ ▒░   ░▒ ░ ▒░  ░   ░  ░ ░  ░
 ░    ░   ░ ░    ░░░ ░ ░  ░ ░  ░     ░ ░    ░ ░ ░ ▒    ░░   ░ ░ ░   ░    ░   
 ░          ░  ░   ░        ░                   ░ ░     ░           ░    ░  ░
      ░                   ░            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
python main.py --m <MOD: (FTP/TELNET/SSH)>
""")
    else:
        mod = str(argv[2]).upper()
        Main(mod).run()

if __name__ == "__main__":
    start(argv=sys.argv)
        
