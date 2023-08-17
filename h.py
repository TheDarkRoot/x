import sys
import hashlib
import time
import os
import random
import binascii
from urllib.request import urlopen, urlencode
from re import search
import progressbar
from passlib.hash import mysql323 as m20
from passlib.hash import mysql41 as m25
from passlib.hash import mssql2000 as ms20
from passlib.hash import mssql2005 as ms25
from passlib.hash import nthash as nthash
from passlib.hash import lmhash as lmhash

# Color
if sys.platform == "linux" or sys.platform == "linux2":
    BB = "\033[34;1m"  # Blue Light
    YY = "\033[33;1m"  # Yellow Light
    GG = "\033[32;1m"  # Green Light
    WW = "\033[0;1m"   # White Light
    RR = "\033[31;1m"  # Red Light
    CC = "\033[36;1m"  # Cyan Light
    MM = "\033[35;1m"  # Magenta Light
    B = "\033[34;1m"   # Blue
    Y = "\033[33;1m"   # Yellow
    G = "\033[32;1m"   # Green
    W = "\033[0;1m"    # White
    R = "\033[31;1m"   # Red
    C = "\033[36;1m"   # Cyan
    M = "\033[35;1m"   # Magenta
    rand = (BB, YY, GG, RR, CC)
    P = random.choice(rand)
elif sys.platform == "win32":
    BB = ''  # Blue Light
    YY = ''  # Yellow Light
    GG = ''  # Green Light
    WW = ''  # White Light
    RR = ''  # Red Light
    CC = ''  # Cyan Light
    B = ''   # Blue
    Y = ''   # Yellow
    G = ''   # Green
    W = ''   # White
    R = ''   # Red
    C = ''   # Cyan
    P = ''   # Random Color

def banner():
    print(CC + '\n              Hash Cracker' + GG + ' v1.0.0')
    print(P + '  #      #' + WW + ' ##################################')
    print(P + '  #      #   ##    ####  #    # ###### #####  ')
    print(P + '  #      #  #  #  #      #    # #      #    # ')
    print(P + '  ######## #    #  ####  ###### #####  #    # ')
    print(P + '  #      # ######      # #    # #      #####  ')
    print(P + '  #      # #    # #    # #    # #      #   #  ')
    print(P + '  #      # #    #  ####  #    # ###### #    # ')
    print(WW + '  ##############[' + CC + ' TheDarkRoot' + WW + ' ]############## ')
    print(P + "            python3 " + sys.argv[0] + " --info\n" + W)

def info():
    print(GG + "\n 0{======================" + WW + " INFO " + GG + "=======================}0")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Name     " + CC + ":" + WW + " Hasher" + GG + "                               |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Code     " + CC + ":" + WW + " Python3" + GG + "                              |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Version  " + CC + ":" + WW + " v1.0.0 (Alpha)" + GG + "                       |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Author   " + CC + ":" + WW + " TheDarkRoot" + GG + "                          |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Email    " + CC + ":" + WW + " thedarkroot@tuta.io" + GG + "                   |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "GitHub   " + CC + ":" + WW + " https://github.com/TheDarkRoot" + GG + "        |")
    print(GG + " 0{======================" + WW + " INFO " + GG + "=======================}0\n" + WW)
    sys.exit()

def manual():
    print(CC + "\n 0{======================" + WW + " MANUAL " + CC + "=======================}0")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-h --help" + CC + "            |" + GG + " Show this help manual        |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-b --banner" + CC + "           |" + GG + " Show the banner             |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-i --info" + CC + "             |" + GG + " Show the info                |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-l --list" + CC + "             |" + GG + " Show the hash list           |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-s --server" + CC + " <server>  |" + GG + " Use server to crack hashes  |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-S --server-list" + CC + "        |" + GG + " Show the server list         |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-u --username" + CC + " <username>|" + GG + " Set the username to crack    |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-U --userlist" + CC + " <userlist>|" + GG + " Use a list of usernames     |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-H --hash" + CC + " <hash>      |" + GG + " Use a single hash            |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-f --hashfile" + CC + " <hashfile> |" + GG + " Use a list of hashes        |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-p --password" + CC + " <password>|" + GG + " Use single password for hash|")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "-P --passlist" + CC + " <passlist>|" + GG + " Use list of passwords for hash|")
    print(GG + " 0{======================" + WW + " MANUAL " + GG + "=======================}0\n" + WW)
    sys.exit()

def server_list():
    print(CC + "\n 0{=======================" + WW + " SERVER LIST " + CC + "========================}0")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "hashes.org" + GG + "                            |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decryption.com" + GG + "                      |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "hashes.com" + GG + "                             |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5.my-addr.com" + GG + "                         |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5.net" + GG + "                                 |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decrypt.net" + GG + "                          |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decryption.com" + GG + "                      |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decryption.com" + GG + "                      |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "sha1decryption.com" + GG + "                     |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "onlinehashcrack.com" + GG + "                    |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "hashcrack.blogspot.com" + GG + "                 |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5.cz" + GG + "                                  |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5hashing.net" + GG + "                          |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "sha1-online.com" + GG + "                         |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "sha1hash.com" + GG + "                            |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decrypter.co.uk" + GG + "                     |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "hashtoolkit.com" + GG + "                         |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "hashcrack.com" + GG + "                            |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5decrypt.co.uk" + GG + "                        |")
    print(GG + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "md5lookup.com" + GG + "                            |")
    print(GG + " 0{=======================" + WW + " SERVER LIST " + GG + "========================}0\n" + WW)
    sys.exit()

def error(errmsg):
    print(RR + "\n [!] " + WW + errmsg + RR + " [!]\n" + WW)
    sys.exit()

def warning(wrnmsg):
    print(RR + "\n [!] " + WW + wrnmsg + RR + " [!]\n" + WW)

def success(scsmsg):
    print(GG + "\n [!] " + WW + scsmsg + GG + " [!]\n" + WW)

def show_cracking_progress(start_time, current_attempt, total_attempts, hash_type, current_password):
    elapsed_time = time.time() - start_time
    avg_speed = elapsed_time / current_attempt if current_attempt > 0 else 0
    remaining_time = avg_speed * (total_attempts - current_attempt)

    if current_password:
        message = f"\r{CC}[{GG}{current_attempt}/{total_attempts}{CC}] " \
                  f"Hash Type: {GG}{hash_type}{CC} - " \
                  f"Current Password: {GG}{current_password}{CC} - " \
                  f"Avg Speed: {GG}{avg_speed:.4f} sec/attempt{CC} - " \
                  f"Elapsed Time: {GG}{elapsed_time:.2f} sec{CC} - " \
                  f"Estimated Time Remaining: {GG}{remaining_time:.2f} sec{CC}"
    else:
        message = f"\r{CC}[{GG}{current_attempt}/{total_attempts}{CC}] " \
                  f"Hash Type: {GG}{hash_type}{CC} - " \
                  f"Avg Speed: {GG}{avg_speed:.4f} sec/attempt{CC} - " \
                  f"Elapsed Time: {GG}{elapsed_time:.2f} sec{CC} - " \
                  f"Estimated Time Remaining: {GG}{remaining_time:.2f} sec{CC}"

    sys.stdout.write(message)
    sys.stdout.flush()

def crack_hash(hash_value, hash_type, password_list):
    print(GG + "\n\n" + WW + " 0{========================" + CC + " CRACKING " + WW + "=========================}0")
    print(CC + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Hash Value" + CC + " : " + GG + hash_value)
    print(CC + " |" + YY + " [" + CC + "=" + YY + "] " + WW + "Hash Type" + CC + "  : " + GG + hash_type)
    print(CC + " 0{========================" + WW + " CRACKING " + CC + "=========================}0\n" + WW)

    start_time = time.time()
    total_attempts = len(password_list)

    for attempt, password in enumerate(password_list, start=1):
        password = password.strip()
        hashed_password = hash_function(password)

        show_cracking_progress(start_time, attempt, total_attempts, hash_type, password)

        if hash_value == hashed_password:
            print("\n")
            success("Password found!")
            print("\n")
            print(GG + " " * 29 + CC + "[" + WW + "+" + CC + "] " + WW + "Password" + CC + " : " + GG + password + "\n" + WW)
            sys.exit()

    print("\n")
    warning("Password not found in the provided password list.\n")
    sys.exit()

def hash_function(password):
    return hashlib.md5(password.encode()).hexdigest()

def main():
    if len(sys.argv) < 2:
        error("Missing arguments! Use '-h' or '--help' for help.")

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        manual()

    if sys.argv[1] == "-b" or sys.argv[1] == "--banner":
        banner()

    if sys.argv[1] == "-i" or sys.argv[1] == "--info":
        info()

    if sys.argv[1] == "-S" or sys.argv[1] == "--server-list":
        server_list()

    if sys.argv[1] == "-u" or sys.argv[1] == "--username":
        if len(sys.argv) >= 3:
            global username
            username = sys.argv[2]

    if sys.argv[1] == "-U" or sys.argv[1] == "--userlist":
        if len(sys.argv) >= 3:
            global userlist
            userlist = sys.argv[2]

    if sys.argv[1] == "-H" or sys.argv[1] == "--hash":
        if len(sys.argv) >= 3:
            global hash_value
            hash_value = sys.argv[2]

    if sys.argv[1] == "-f" or sys.argv[1] == "--hashfile":
        if len(sys.argv) >= 3:
            hashfile = sys.argv[2]

    if sys.argv[1] == "-p" or sys.argv[1] == "--password":
        if len(sys.argv) >= 3:
            global password
            password = sys.argv[2]

    if sys.argv[1] == "-P" or sys.argv[1] == "--passlist":
        if len(sys.argv) >= 3:
            passlist = sys.argv[2]

    if sys.argv[1] == "-s" or sys.argv[1] == "--server":
        if len(sys.argv) >= 3:
            server = sys.argv[2]

            if sys.argv[3] == "-H" or sys.argv[3] == "--hash":
                if len(sys.argv) >= 4:
                    hash_value = sys.argv[4]

            if sys.argv[3] == "-f" or sys.argv[3] == "--hashfile":
                if len(sys.argv) >= 4:
                    hashfile = sys.argv[4]

            if sys.argv[3] == "-u" or sys.argv[3] == "--username":
                if len(sys.argv) >= 4:
                    username = sys.argv[4]

            if sys.argv[3] == "-U" or sys.argv[3] == "--userlist":
                if len(sys.argv) >= 4:
                    userlist = sys.argv[4]

            if sys.argv[3] == "-p" or sys.argv[3] == "--password":
                if len(sys.argv) >= 4:
                    password = sys.argv[4]

            if sys.argv[3] == "-P" or sys.argv[3] == "--passlist":
                if len(sys.argv) >= 4:
                    passlist = sys.argv[4]

    try:
        banner()

        if len(sys.argv) >= 2:
            main()

    except KeyboardInterrupt:
        warning("User interrupted the process.")

if __name__ == "__main__":
    main()
