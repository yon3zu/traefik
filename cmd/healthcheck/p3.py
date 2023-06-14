import requests
import os
import time
import re
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init

init(autoreset=True)

def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{} xReverse V9  | {}#No_Identity - @xxyz4".format(Fore.CYAN, Fore.GREEN))
    print("\t{} IP Reverse From 3 {}Server !\n".format(Fore.GREEN, Fore.YELLOW))
    print("{} Server 1 {}Active !".format(Fore.CYAN, Fore.GREEN))
    print("{} Server 2 {}Active !".format(Fore.CYAN, Fore.GREEN))
    print("{} Server 3 {}Active !\n".format(Fore.CYAN, Fore.GREEN))

    try:
        list = input("MAINTENANCE ")
        url = open(list, 'r').read().splitlines()
        THREAD = input("root@youez[thread]:~# ")
        pp = ThreadPool(int(THREAD))
        pr = pp.map(revip, url)
    except:
        pass


if __name__ == '__main__':
    Main()
