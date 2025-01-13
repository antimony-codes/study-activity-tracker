from datetime import datetime as dt
import pyuac
from datetime import time

def block_sites():
    with open('blockedWebsites.txt', 'r') as file:
        lines = []
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

sites_to_block = block_sites()
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def main():
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
            with open(hosts_path, 'r+') as file: 
                content = file.read() 
                file.seek(0)
                for website in sites_to_block: 
                    if website in content: 
                        pass
                    else: 
                        # mapping hostnames to your localhost IP address 
                        file.write(redirect + " " + website + "\n")
                        # file.flush()
                file.truncate()
    
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:  
        main()

# currently wont run without admin privileges from ide
# but if formatted in the task manager to run at startup and given admin privileges
# should not have an issue