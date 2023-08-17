#!/usr/bin/env python3

import sys
import hashlib
import time
import os
import random
import binascii
import zlib
from urllib.request import urlopen
from urllib.parse import urlencode
from re import search

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

    # Random Color
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
    print(CC + '\n              Hash Generator' + GG + ' v1.0.0')
    print(P + '  #      #' + WW + ' #########################################')
    print(P + '  #      #   ##    ####  #    #  ####  ###### #    # ')
    print(P + '  #      #  #  #  #      #    # #    # #      ##   # ')
    print(P + '  ######## #    #  ####  ###### #      #####  # #  # ')
    print(P + '  #      # ######      # #    # #  ### #      #  # # ')
    print(P + '  #      # #    # #    # #    # #    # #      #   ## ')
    print(P + '  #      # #    #  ####  #    #  ####  ###### #    # ')
    print(WW + '  #################[' + CC + ' TheDarkRoot' + WW + ' ]################## ')
    print(P + "              python3 " + sys.argv[0] + " --info\n" + W)

def info():
    print(GG + "\n 0{======================" + WW + " INFO " + GG + "=======================}0")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Name     " + CC + ":" + WW + " Hashgen" + GG + "                              |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Code     " + CC + ":" + WW + " Python3" + GG + "                              |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Version  " + CC + ":" + WW + " v1.0.0 (Alpha)" + GG + "                       |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Author   " + CC + ":" + WW + " TheDarkRoot" + GG + "                          |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Email    " + CC + ":" + WW + " 7H3D4RKR007@gmail.com" + GG + "                |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Github   " + CC + ":" + WW + " https://github.com/TheDarkRoot" + GG + "       |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Telegram " + CC + ":" + WW + " @TheDarkRoot (t.me/TheDarkRoot)" + GG + "      |")
    print(GG + " |" + BB + " [" + RR + "=" + BB + "] " + WW + "Team     " + CC + ":" + WW + " TurkHackTeam (www.turkhackteam.org)" + GG + "  |")
    print(GG + " 0{===================================================}0\n")
    print(BB + " [" + RR + "=" + BB + "] " + WW + "python3 " + sys.argv[0] + " -u")
    print(BB + "\n [" + RR + "=" + BB + "] " + WW + "To Update Hashgen.py")
    print(BB + "\n [" + RR + "=" + BB + "] " + WW + "List of supported hashes:")
    print(YY + "\n                          [" + WW + "01" + YY + "] " + CC + "MySQL 3.2.3")
    print(YY + "                          [" + WW + "02" + YY + "] " + CC + "MySQL 4.1")
    print(YY + "                          [" + WW + "03" + YY + "] " + CC + "MSSQL 2000")
    print(YY + "                          [" + WW + "04" + YY + "] " + CC + "MSSQL 2005")
    print(YY + "                          [" + WW + "05" + YY + "] " + CC + "MD4")
    print(YY + "                          [" + WW + "06" + YY + "] " + CC + "MD5")
    print(YY + "                          [" + WW + "07" + YY + "] " + CC + "SHA1")
    print(YY + "                          [" + WW + "08" + YY + "] " + CC + "SHA224")
    print(YY + "                          [" + WW + "09" + YY + "] " + CC + "SHA256")
    print(YY + "                          [" + WW + "10" + YY + "] " + CC + "SHA384")
    print(YY + "                          [" + WW + "11" + YY + "] " + CC + "SHA512")
    print(YY + "                          [" + WW + "12" + YY + "] " + CC + "RIPEMD160")
    print(YY + "                          [" + WW + "13" + YY + "] " + CC + "WHIRLPOOL")
    print(YY + "                          [" + WW + "14" + YY + "] " + CC + "CRC32")
    print(YY + "                          [" + WW + "15" + YY + "] " + CC + "ADLER32")
    print(YY + "                          [" + WW + "16" + YY + "] " + CC + "DES Crypt")
    print(YY + "                          [" + WW + "17" + YY + "] " + CC + "BSDi Crypt")
    print(YY + "                          [" + WW + "18" + YY + "] " + CC + "BIGCrypt")
    print(YY + "                          [" + WW + "19" + YY + "] " + CC + "Crypt16")
    print(YY + "                          [" + WW + "20" + YY + "] " + CC + "MD5 Crypt")
    print(YY + "                          [" + WW + "21" + YY + "] " + CC + "SHA1 Crypt")
    print(YY + "                          [" + WW + "22" + YY + "] " + CC + "SHA256 Crypt")
    print(YY + "                          [" + WW + "23" + YY + "] " + CC + "SHA512 Crypt")
    print(YY + "                          [" + WW + "24" + YY + "] " + CC + "Sun MD5 Crypt")
    print(YY + "                          [" + WW + "25" + YY + "] " + CC + "Apr MD5 Crypt")
    print(YY + "                          [" + WW + "26" + YY + "] " + CC + "PHPASS")
    print(YY + "                          [" + WW + "27" + YY + "] " + CC + "CTA PBKDF2 SHA1")
    print(YY + "                          [" + WW + "28" + YY + "] " + CC + "Dlitz PBDKF2 SHA1")
    print(YY + "                          [" + WW + "29" + YY + "] " + CC + "Atlassian's PBKDF2")
    print(YY + "                          [" + WW + "30" + YY + "] " + CC + "Django PBKDF2 SHA1")
    print(YY + "                          [" + WW + "31" + YY + "] " + CC + "Django PBKDF2 SHA256")
    print(YY + "                          [" + WW + "32" + YY + "] " + CC + "Grub's PBKDF2")
    print(YY + "                          [" + WW + "33" + YY + "] " + CC + "SCRAM Hash")
    print(YY + "                          [" + WW + "34" + YY + "] " + CC + "BSD nthash")
    print(YY + "                          [" + WW + "35" + YY + "] " + CC + "Oracle11")
    print(YY + "                          [" + WW + "36" + YY + "] " + CC + "LanManager Hash")
    print(YY + "                          [" + WW + "37" + YY + "] " + CC + "Windows NT-Hash")
    print(YY + "                          [" + WW + "38" + YY + "] " + CC + "Cisco Type 7")
    print(YY + "                          [" + WW + "39" + YY + "] " + CC + "FHSP\n" + W)

def Update():
    if sys.platform == "linux" or sys.platform == "linux2":
        print(BB + " 0={" + WW + " Update Hashgen. " + BB + "}=0\n")
        time.sleep(1)

        print(BB + "[" + WW + "=" + BB + "] " + GG + "Remove old Hashgen.")
        os.system("rm -rf Hashgen.py")
        time.sleep(1)

        print(BB + "[" + WW + "=" + BB + "] " + GG + "Downloading Hashgen.")
        time.sleep(1)

        print(RR + "[" + WW + "*" + RR + "] " + RR + "Curl Started...\n" + W)

        os.system("curl https://raw.githubusercontent.com/TheDarkRoot/Hashgen/master/Hashgen.py -o Hashgen.py")

        print(RR + "\n[" + WW + "*" + RR + "] " + GG + "Download finish.\n" + W)
        sys.exit()
    else:
        print("Sorry, Hashgen update feature is only available on linux platform.\n")
        sys.exit()

try:
    import progressbar
    import passlib

except ImportError:
    banner()
    time.sleep(0.5)
    print(BB + "[" + WW + "=" + BB + "] " + GG + "installing module " + RR + "progressbar, passlib.\n" + W)

    os.system("pip3 install --upgrade pip")
    os.system("pip3 install passlib")
    os.system("pip3 install progressbar2")

    print(BB + "\n[" + WW + "=" + BB + "] " + GG + "install success, run program again.\n" + W)
    sys.exit()

try:
    banner()
    x = input(CC + "[" + WW + "~" + CC + "] " + GG + "String" + CC + ": " + W)

except NameError:
    print(RR + "\n[" + WW + "!" + RR + "] " + GG + "use " + WW + "python3\n")
    quit()

print(YY + "[" + WW + "!" + YY + "] " + GG + "Generate Hash        :" + YY + " Please Wait!!!" + W)
time.sleep(0.5)

# mysql1323
from passlib.hash import mysql323
mysql1323 = mysql323.hash(x)
print(YY + "\n[" + WW + "01" + YY + "]>" + GG + "MySQL 3.2.3         : " + W + mysql1323)

# mysql141
from passlib.hash import mysql41
mysql141 = mysql41.hash(x)
print(YY + "[" + WW + "02" + YY + "]>" + GG + "MySQL 4.1           : " + W + mysql141)

# mssql2000
from passlib.hash import mssql2000 as m20
mssql2000 = m20.hash(x)
print(YY + "[" + WW + "03" + YY + "]>" + GG + "MSSQL 2000          : " + W + mssql2000)

# mssql2005
from passlib.hash import mssql2005 as m25
mssql2005 = m25.hash(x)
print(YY + "[" + WW + "04" + YY + "]>" + GG + "MSSQL 2005          : " + W + mssql2005)

# md4
md4 = hashlib.new("md4", x.encode("utf-16le")).hexdigest()
print(YY + "[" + WW + "05" + YY + "]>" + GG + "MD4                 : " + W + md4)

# md5
md5 = hashlib.md5(x.encode()).hexdigest()
print(YY + "[" + WW + "06" + YY + "]>" + GG + "MD5                 : " + W + md5)

# sha1
sha1 = hashlib.sha1(x.encode()).hexdigest()
print(YY + "[" + WW + "07" + YY + "]>" + GG + "SHA1                : " + W + sha1)

# sha224
sha224 = hashlib.sha224(x.encode()).hexdigest()
print(YY + "[" + WW + "08" + YY + "]>" + GG + "SHA224              : " + W + sha224)

# sha256
sha256 = hashlib.sha256(x.encode()).hexdigest()
print(YY + "[" + WW + "09" + YY + "]>" + GG + "SHA256              : " + W + sha256)

# sha384
sha384 = hashlib.sha384(x.encode()).hexdigest()
print(YY + "[" + WW + "10" + YY + "]>" + GG + "SHA384              : " + W + sha384)

# sha512
sha512 = hashlib.sha512(x.encode()).hexdigest()
print(YY + "[" + WW + "11" + YY + "]>" + GG + "SHA512              : " + W + sha512)

# ripemd160
ripemd160 = hashlib.new("ripemd160", x.encode()).hexdigest()
print(YY + "[" + WW + "12" + YY + "]>" + GG + "RIPEMD-160          : " + W + ripemd160)

# whirlpool
whirlpool = hashlib.new("whirlpool", x.encode()).hexdigest()
print(YY + "[" + WW + "13" + YY + "]>" + GG + "WHIRLPOOL           : " + W + whirlpool)

# crc32
crc32 = binascii.crc32(x.encode())
print(YY + "[" + WW + "14" + YY + "]>" + GG + "CRC32               : " + W + hex(crc32))

# adler32
adler32 = binascii.adler32(x.encode())
print(YY + "[" + WW + "15" + YY + "]>" + GG + "ADLER32             : " + W + hex(adler32))

# des_crypt
des_crypt = hashlib.new("des_crypt", x.encode()).hexdigest()
print(YY + "[" + WW + "16" + YY + "]>" + GG + "DES Crypt           : " + W + des_crypt)

# bsd_nthash
bsd_nthash = hashlib.new("md4", x.encode("utf-16le")).hexdigest()
print(YY + "[" + WW + "34" + YY + "]>" + GG + "BSD nthash          : " + W + bsd_nthash)

# oracle11
oracle11 = hashlib.sha1(x.encode()).hexdigest()
print(YY + "[" + WW + "35" + YY + "]>" + GG + "Oracle11            : " + W + oracle11)

# lanmanager
from passlib.hash import lmhash
lanmanager = lmhash.hash(x)
print(YY + "[" + WW + "36" + YY + "]>" + GG + "LanManager Hash     : " + W + lanmanager)

# windows_nthash
from passlib.hash import nthash
windows_nthash = nthash.hash(x)
print(YY + "[" + WW + "37" + YY + "]>" + GG + "Windows NT-Hash     : " + W + windows_nthash)

# cisco_type7
from passlib.hash import cisco_type7
cisco_type7 = cisco_type7.hash(x)
print(YY + "[" + WW + "38" + YY + "]>" + GG + "Cisco Type 7        : " + W + cisco_type7)

# cta_pbkdf2_hmac_sha1
from passlib.hash import cta_pbkdf2_sha1
cta_pbkdf2_hmac_sha1 = cta_pbkdf2_sha1.hash(x)
print(YY + "[" + WW + "39" + YY + "]>" + GG + "CTA PBKDF2 HMAC SHA1: " + W + cta_pbkdf2_hmac_sha1)

# dlitz_pbkdf2_hmac_sha1
from passlib.hash import dlitz_pbkdf2_sha1
dlitz_pbkdf2_hmac_sha1 = dlitz_pbkdf2_sha1.hash(x)
print(YY + "[" + WW + "40" + YY + "]>" + GG + "Dlitz PBKDF2 HMAC SHA1: " + W + dlitz_pbkdf2_hmac_sha1)

# atlassian_pbkdf2_sha1
from passlib.hash import atlassian_pbkdf2_sha1
atlassian_pbkdf2_sha1 = atlassian_pbkdf2_sha1.hash(x)
print(YY + "[" + WW + "41" + YY + "]>" + GG + "Atlassian's PBKDF2  : " + W + atlassian_pbkdf2_sha1)

# django_pbkdf2_sha1
from passlib.hash import django_pbkdf2_sha1
django_pbkdf2_sha1 = django_pbkdf2_sha1.hash(x)
print(YY + "[" + WW + "42" + YY + "]>" + GG + "Django PBKDF2 SHA1  : " + W + django_pbkdf2_sha1)

# django_pbkdf2_sha256
from passlib.hash import django_pbkdf2_sha256
django_pbkdf2_sha256 = django_pbkdf2_sha256.hash(x)
print(YY + "[" + WW + "43" + YY + "]>" + GG + "Django PBKDF2 SHA256: " + W + django_pbkdf2_sha256)

# grub_pbkdf2_sha512
from passlib.hash import grub_pbkdf2_sha512
grub_pbkdf2_sha512 = grub_pbkdf2_sha512.hash(x)
print(YY + "[" + WW + "44" + YY + "]>" + GG + "Grub's PBKDF2 SHA512: " + W + grub_pbkdf2_sha512)

# scram
from passlib.hash import scram
scram = scram.hash(x)
print(YY + "[" + WW + "45" + YY + "]>" + GG + "SCRAM Hash          : " + W + scram)

# apr_md5_crypt
from passlib.hash import apr_md5_crypt
apr_md5_crypt = apr_md5_crypt.hash(x)
print(YY + "[" + WW + "46" + YY + "]>" + GG + "Apr MD5 Crypt       : " + W + apr_md5_crypt)

# phpass
from passlib.hash import phpass
phpass = phpass.hash(x)
print(YY + "[" + WW + "47" + YY + "]>" + GG + "PHPASS              : " + W + phpass)

# crypt16
from passlib.hash import crypt16
crypt16 = crypt16.hash(x)
print(YY + "[" + WW + "48" + YY + "]>" + GG + "Crypt16             : " + W + crypt16)

# md5_crypt
from passlib.hash import md5_crypt
md5_crypt = md5_crypt.hash(x)
print(YY + "[" + WW + "49" + YY + "]>" + GG + "MD5 Crypt           : " + W + md5_crypt)

# sha1_crypt
from passlib.hash import sha1_crypt
sha1_crypt = sha1_crypt.hash(x)
print(YY + "[" + WW + "50" + YY + "]>" + GG + "SHA1 Crypt          : " + W + sha1_crypt)

# sha256_crypt
from passlib.hash import sha256_crypt
sha256_crypt = sha256_crypt.hash(x)
print(YY + "[" + WW + "51" + YY + "]>" + GG + "SHA256 Crypt        : " + W + sha256_crypt)

# sha512_crypt
from passlib.hash import sha512_crypt
sha512_crypt = sha512_crypt.hash(x)
print(YY + "[" + WW + "52" + YY + "]>" + GG + "SHA512 Crypt        : " + W + sha512_crypt)

# sun_md5_crypt
from passlib.hash import sun_md5_crypt
sun_md5_crypt = sun_md5_crypt.hash(x)
print(YY + "[" + WW + "53" + YY + "]>" + GG + "Sun MD5 Crypt       : " + W + sun_md5_crypt)

# bigcrypt
from passlib.hash import bigcrypt
bigcrypt = bigcrypt.hash(x)
print(YY + "[" + WW + "54" + YY + "]>" + GG + "BIGCrypt            : " + W + bigcrypt)

# bcrypt
from passlib.hash import bcrypt
bcrypt = bcrypt.hash(x)
print(YY + "[" + WW + "55" + YY + "]>" + GG + "BCrypt              : " + W + bcrypt)

# cisco_pix
from passlib.hash import cisco_pix
cisco_pix = cisco_pix.hash(x)
print(YY + "[" + WW + "56" + YY + "]>" + GG + "Cisco PIX           : " + W + cisco_pix)

# cisco_asa
from passlib.hash import cisco_asa
cisco_asa = cisco_asa.hash(x)
print(YY + "[" + WW + "57" + YY + "]>" + GG + "Cisco ASA           : " + W + cisco_asa)

# juniper_junos
from passlib.hash import juniper_junos
juniper_junos = juniper_junos.hash(x)
print(YY + "[" + WW + "58" + YY + "]>" + GG + "Juniper Junos       : " + W + juniper_junos)

# pbkdf2_sha1
from passlib.hash import pbkdf2_sha1
pbkdf2_sha1 = pbkdf2_sha1.hash(x)
print(YY + "[" + WW + "59" + YY + "]>" + GG + "PBKDF2 SHA1         : " + W + pbkdf2_sha1)

# pbkdf2_sha256
from passlib.hash import pbkdf2_sha256
pbkdf2_sha256 = pbkdf2_sha256.hash(x)
print(YY + "[" + WW + "60" + YY + "]>" + GG + "PBKDF2 SHA256       : " + W + pbkdf2_sha256)

# pbkdf2_sha512
from passlib.hash import pbkdf2_sha512
pbkdf2_sha512 = pbkdf2_sha512.hash(x)
print(YY + "[" + WW + "61" + YY + "]>" + GG + "PBKDF2 SHA512       : " + W + pbkdf2_sha512)

# cisecure_hash
from passlib.hash import cisecure_hash
cisecure_hash = cisecure_hash.hash(x)
print(YY + "[" + WW + "62" + YY + "]>" + GG + "CISecure Hash       : " + W + cisecure_hash)

# phps
from passlib.hash import phps
phps = phps.hash(x)
print(YY + "[" + WW + "63" + YY + "]>" + GG + "PHP's               : " + W + phps)

# mysql323
from passlib.hash import mysql323
mysql323 = mysql323.hash(x)
print(YY + "[" + WW + "64" + YY + "]>" + GG + "MySQL323            : " + W + mysql323)

# oracle
from passlib.hash import oracle10
oracle10 = oracle10.hash(x)
print(YY + "[" + WW + "65" + YY + "]>" + GG + "Oracle 10           : " + W + oracle10)

# bcrypt_sha256
from passlib.hash import bcrypt_sha256
bcrypt_sha256 = bcrypt_sha256.hash(x)
print(YY + "[" + WW + "66" + YY + "]>" + GG + "BCrypt SHA256       : " + W + bcrypt_sha256)

# mssql2000
from passlib.hash import mssql2000
mssql2000 = mssql2000.hash(x)
print(YY + "[" + WW + "67" + YY + "]>" + GG + "MSSQL2000           : " + W + mssql2000)

# mssql2005
from passlib.hash import mssql2005
mssql2005 = mssql2005.hash(x)
print(YY + "[" + WW + "68" + YY + "]>" + GG + "MSSQL2005           : " + W + mssql2005)

# md5
md5 = hashlib.md5(x.encode()).hexdigest()
print(YY + "[" + WW + "69" + YY + "]>" + GG + "MD5                 : " + W + md5)

# ripemd160
ripemd160 = hashlib.new("ripemd160", x.encode()).hexdigest()
print(YY + "[" + WW + "70" + YY + "]>" + GG + "RIPEMD-160          : " + W + ripemd160)

# whirlpool
whirlpool = hashlib.new("whirlpool", x.encode()).hexdigest()
print(YY + "[" + WW + "71" + YY + "]>" + GG + "WHIRLPOOL           : " + W + whirlpool)

# crc32
crc32 = binascii.crc32(x.encode())
print(YY + "[" + WW + "72" + YY + "]>" + GG + "CRC32               : " + W + hex(crc32))

# adler32
adler32 = binascii.adler32(x.encode())
print(YY + "[" + WW + "73" + YY + "]>" + GG + "ADLER32             : " + W + hex(adler32))

print("\n")
info()
