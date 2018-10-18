#!/usr/bin/python3
# Author = Jeff Barron
# Whatismyip scrapes google for your public IP address

import requests
import re

WARNING = '\033[93m'
FAILRED = '\033[91m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'
def main():


    res = requests.get('https://www.google.com/search?q=what+is+my+ip')


  
    #NOPE THIS WAS FUCKING WRONG. found = re.findall(r'address (?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', res.text)

    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', res.text)

    print("Your IP is: ", OKGREEN + ip[0])
    print(ENDC)




if __name__ == "__main__":
    main()


