



def depe():
    os.system("pip install colorama")


if shutil.which('git'):
    print(Fore.YELLOW +" -->>   UPDATING THE SCRIPT   <<--")
    os.system('git checkout . && git pull')
    print(Fore.YELLOW + " ->  UPDATED SUCCESSFULLY RUN THE TOOL AGAIN  <-")
    time.sleep(4)
    os.system("python wordlist.py")
else:
    print("Please reclone wordlist_creator Again")
    sys.exit()
if __name__ == "__main__":
    depe()
    import os
    import shutil
    import sys
    import time
    from colorama import Fore
    
