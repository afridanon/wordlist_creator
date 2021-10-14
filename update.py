import os
import shutil
import sys
import time
from colorama import Fore







if shutil.which('git'):
    print(Fore.YELLOW +"UPDATING....")
    os.system('git checkout . && git pull')
    print(Fore.YELLOW + "UPDATED SUCCESSFULLY RUN THE TOOL AGAIN ")
    time.sleep(4)
    os.system("python wordlist.py")
else:
    print("Please reclone TBomb Again")
    sys.exit()
