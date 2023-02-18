#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importing modules:
import os
import sys
import time
from argparse import ArgumentParser
from zipfile import ZipFile
from rarfile import RarFile
from threading import Thread 

class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    MAGENTA = '\033[35m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    VOILET = '\33[36m'
    BOLD = '\033[1m'

print(style.BOLD)

# Printing Banner:
print(style.VOILET+"""
   ______                        __       ______                    
 .' ___  |                      [  |  _  |_   _ \\                   
/ .'   \\_| _ .--.  ,--.   .---.  | | / ]   | |_) |   .--.    .--.   
| |       [ `/'`\\]`'_\\ : / /'`\\] | '' <    |  __'. / .'`\\ \\/ .'`\\ \\ 
\\ `.___.'\\ | |    // | |,| \\__.  | |`\\ \\  _| |__) || \\__. || \\__. | 
 `.____ .'[___]   \\'-;__/'.___.'[__|  \\_]|_______/  '.__.'  '.__.' 
                                                      @==|;;;;;;>\n"""   
   
        						+style.UNDERLINE+style.WHITE+style.BOLD+"""\n\t\t\t\t\t\t\tby - rick_287\n"""+style.RESET+style.BOLD+style.WHITE+

                                                        style.WHITE+"""\n\t\t\t\t\t\t\tversion - 1.1"""+style.RESET+style.WHITE+style.MAGENTA+"""  
NAME:

CrackBoo - Help to crack zip file


DESCRIPTION:

This tool is the command line version. It is made for cracking password for protected zipfiles. 

USE:

(1) Crack Zip file password
(2) Crack Rar file password
"""
 
+style.BOLD+style.RED+"""\nNote: Future version will contain more features                                                              
""")

def crack_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(style.RED+"[-] Sorry, Password not found for this file!\n"+style.BOLD)
        print(style.YELLOW+"[!] Wait a moment, got something..."+style.BOLD)
        time.sleep(1)
        print(style.BLUE+"[*] Cracking process starting...")
        time.sleep(2)
        print(style.BLUE+"[*] This may take some time, please wait...")
        time.sleep(4)
        print(style.GREEN+'\n[+] Congrats!, Found ZipFile Password: '+style.BOLD+style.BLUE+password+style.BOLD)
        sys.exit(0)
    except:
        pass

def crack_rar(rar_file, password):
    try:
        rar_file.extractall(pwd=password.encode())
        print(style.RED+"[-] Sorry, Password not found for this file!\n"+style.BOLD)
        time.sleep(2)
        print(style.YELLOW+"[!] Wait a moment, got something..."+style.BOLD)
        print(style.BLUE+"[*] Cracking process starting...")
        time.sleep(2)
        print(style.BLUE+"[*] This may take some time, please wait...")
        time.sleep(4)
        print(style.GREEN+'\n[+] Congrats!, Found RarFile Password: '+style.BOLD+style.BLUE+password+style.BOLD)
        sys.exit(0)
    
    except:
        pass

def main():
    parser = ArgumentParser(description="Archive File Cracker")
    parser.add_argument('-z[MENDATORY]', '--zipfile', dest='zipfile', help='Provide Zip file to crack', required=True)
    parser.add_argument('-w[MENDATORY]', '--wordlist', dest='wordlist', help='Provide dictionary file', required=True)
    parser.add_argument("-r[MENDATORY]", '--rarfile', dest='rarfile', help="Provide Rar file to crack")
    parser.add_argument("-v[OPTIONAL]", "--verbose", dest="verboses", help="For Verbose Output",nargs='?', const='')
    parser.add_argument('-V[VERSION]', '--version', help="print version and exit",action='version',version='%(prog)s 1.1')
    args = parser.parse_args()

    zipfile = args.zipfile
    rarfile = args.rarfile
    wordlist = args.wordlist
    verboses = args.verboses

    if len(sys.argv) < 2:
        print(style.RED+"Error: incorrect number of arguments. Expected 2.")
        sys.exit(1)

    if not os.path.isfile(zipfile):
        print(style.RED+"[-] File does not exist or is not a valid file."+style.BOLD)
        sys.exit(1)

    if not os.path.isfile(wordlist):
        print(style.RED+"[-] Wordlist does not exist, provide a valid wordlist."+style.BOLD)
        sys.exit(1)

    try:
        with ZipFile(zipfile) as zFile:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as passFile:
                for line in passFile:
                    password = line.strip()
                    if verboses == '':
                        print(style.BLUE+style.BOLD+"[➤] Trying Password: "+style.BOLD+style.GREEN+password+'\n')
                        time.sleep(2)
                        thread = Thread(target=crack_zip, args=(zFile, password,))
                        thread.start()
    
    except ValueError:
        pass
        
    try:
        with RarFile(rarfile) as rFile:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as passFile:
                for line in passFile:
                    password = line.strip()
                    if verboses == '':
                        print(style.BLUE+style.BOLD+"[➤] Trying Password: "+style.BOLD+style.GREEN+password+'\n')
                        time.sleep(1)
                        thread = Thread(target=crack_rar, args=(rFile, password,))
                        thread.start()

    except ValueError:
        pass

if __name__ == "__main__":
    main()