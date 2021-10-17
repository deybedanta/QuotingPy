import requests
import os
import platform
import time
from quotee.random import Quotee
from colorama import Fore

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


splash = """

 _  _    ___                      _    _                  _______         _  _  
| || | .'   `.                   / |_ (_)                |_   __ \       | || | 
\_|\_|/  .-.  \  __   _    .--. `| |-'__   _ .--.   .--./) | |__) |_   __\_|\_| 
      | |   | | [  | | | / .'`\ \| | [  | [ `.-. | / /'`\; |  ___/[ \ [  ]      
      \  `-'  \_ | \_/ |,| \__. || |, | |  | | | | \ \._//_| |_    \ '/ /       
       `.___.\__|'.__.'_/ '.__.' \__/[___][___||__].',__`|_____| [\_:  /        
                                                  ( ( __))        \__.'         


"""

def begin():
    print(Fore.BLUE + splash + Fore.WHITE)
    print("")
    print("Welcome to" + Fore.YELLOW + " QuotingPy" + Fore.WHITE + "! This program generates random quotes that might just brighten your day! [Made by Bedanta Dey]")
    print("")
    print("Please use '" + Fore.GREEN + "g" + Fore.WHITE + "' to generate a quote, or '" + Fore.RED + "q" + Fore.WHITE + "' to quit the program.")

    run = input('> ')

    if run == 'g':
        clear()
        print(Fore.BLUE + 'Please wait while QuotingPy is generating a wonderful quote...' + Fore.WHITE)
        time.sleep(1.5)
        clear()
        main()
    elif run == 'q':
        clear()
        print("Thanks for using " + Fore.YELLOW + "QuotingPy" + Fore.WHITE + ". I hope to see you soon! " + Fore.RED + "[Ending in 3...]" + Fore.WHITE)
        time.sleep(3)
        exit()
    else:
        print("'Sometimes, you just have to type in the right command.' -- Bedanta Dey" + Fore.RED + "[Ending in 3...]" + Fore.WHITE)
        time.sleep(3)
        exit()

def main():
    
    q = Quotee()

    quote = q.quote
    author = q.author

    print('')
    print('"' + quote + '"')
    print("   -- " + author)
    runagain()

def runagain():
    print("")
    print("")
    print("Would you like to try " + Fore.YELLOW + "the wheel of quotes " + Fore.WHITE + " and" + Fore.BLUE + " roll another quote " + Fore.WHITE + "again?")
    print("Type in '" + Fore.GREEN + "y" + Fore.WHITE + "' to generate a new quote, or '" + Fore.RED + "n" + Fore.WHITE + "' to return to the navigation.")
    print("")

    run2 = input('> ')

    if run2 == 'y':
        print("")
        print('Please wait...')
        time.sleep(1)
        clear()
        main()
    elif run2 == 'n':
        print("")
        print('Please wait...')
        time.sleep(1)
        clear()
        begin()
    else:
        print("'Sometimes, you just have to type in the right command.' -- Bedanta Dey" + Fore.RED + "[Ending in 3...]" + Fore.WHITE)
        time.sleep(3)
        exit()


begin()

