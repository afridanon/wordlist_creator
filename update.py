import os
import time
from colorama import Fore




os.system("cd ..")
os.system("rm -rf wordlist_creator")
os.system("git clone https://github.com/afridanon/wordlist_creator")
os.system("cd wordlist_creator")
print(Fore.YELLOW + "Updated Successfully")
time.sleep(4)
os.system("clear")
os.system("python wordlist.py")
