
def depn():
    os.system("pip install wordlist colorama")
    os.system("clear")


def banner():
    BANNER = """
 __      _____  ___ ___  _    ___ ___ _____ 
 \ \    / / _ \| _ \   \| |  |_ _/ __|_   _|
  \ \/\/ / (_) |   / |) | |__ | |\__ \ | |  
   \_/\_/ \___/|_|_\___/|____|___|___/ |_|  
   """
    print(Fore.RED + BANNER )
    print(Fore.YELLOW + "                     AUTHOR :- 𝐒𝐇𝐀𝐈𝐊 𝐀𝐅𝐑𝐈𝐃")


def bio():
    global name,dob,pos
    name = input(Fore.BLUE + "Enter Victim Name:-")
    dob =  input(Fore.BLUE + "Enter Victim date Of Birth Year(ex:-2001):- ")
    print(Fore.YELLOW + "Do U Want Possible Hints press YES OR No")
    check = input(Fore.BLUE + "Enter Ur Option :-").lower()
    if check == "yes":
        poss = 143123
        pos = str(poss)
    else:
        pos = ""
    main()
def main():
    wordlist_maker = "wordlist -m 6 -M 7 -o passwords.txt"+" "+name+dob+pos 
    print(Fore.CYAN + "Plese Wait Wordlist creating ....")
    os.system(wordlist_maker)
    print(Fore.MAGENTA + "Created successfully ....! passwords.txt")
    time.sleep(2)
    sys.exit()
def WARNING():
    print(Fore.BLUE+ ">>This Tool Will Create Wordlist for our tools")
    print(Fore.BLUE+ ">>Size Of Wordlist Will More Then 10GB \n>>So Be Carefull With This Tool  ")
    print(Fore.BLUE +">>We Are Warning You !")
    time.sleep(15)
    os.system("clear")
    time.sleep(2)
    bio()

    
   
def ASKS():
    print(Fore.MAGENTA+"Do U Want Create Wordlist !")
    verify = str(input(Fore.YELLOW + "ENTER UR  OPTION(YES OR NO) :-")).lower()
    if verify == "yes":
        WARNING()
    else:
        print("Thanks For Using Our Tool : )")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    depn()
    import os
    from colorama import init
    init(autoreset=True)
    from colorama import Fore
    import time
    import sys
    banner()
    ASKS()
