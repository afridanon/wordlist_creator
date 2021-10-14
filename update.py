import os
import time
from colorama import Fore




os.system("chmod +x *")
os.system("bash update.sh")

print(Fore.Yellow + "Updated Successfully")
time.sleep(4)
os.system("clear")
os.system("python wodlist.py")
