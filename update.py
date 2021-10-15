


import os
import shutil
import sys
import time
def depe():
    os.system("pip install colorama")
def modules():
    
    from colorama import Fore



if __name__ == "__main__":
    depe()
    modules()
    if shutil.which('git'):
        print(Fore.YELLOW +" -->>   UPDATING THE SCRIPT   <<--")
        os.system('git checkout . && git pull')
        print(Fore.YELLOW + " ->  UPDATED SUCCESSFULLY RUN THE TOOL AGAIN  <-")
        time.sleep(4)
        os.system("python wordlist.py")
    else:
        print("Please reclone wordlist_creator Again")
        sys.exit()

    
