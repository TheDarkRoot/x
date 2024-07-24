#!/bin/bash
# -*- coding: utf-8 -*-

# Spinner Function
spin () {
  local pid=$!
  local delay=0.10
  local spinner=( '\033[34;1m■■■■■■■' '\033[32;1m█\033[33;1m■■■■■■' '\033[33;1m■\033[32;1m█\033[33;1m■■■■■' '\033[33;1m■■\033[32;1m█\033[33;1m■■■■' '\033[33;1m■■■\033[32;1m█\033[33;1m■■■' '\033[33;1m■■■■\033[32;1m█\033[33;1m■■' '\033[33;1m■■■■■\033[32;1m█\033[33;1m■' '\033[33;1m■■■■■■\033[32;1m█' '\033[34;1m■■■■■■■' '\033[33;1m■■■■■■\033[32;1m█' '\033[33;1m■■■■■\033[32;1m█\033[33;1m■' '\033[33;1m■■■■\033[32;1m█\033[33;1m■■' '\033[33;1m■■■\033[32;1m█\033[33;1m■■■' '\033[33;1m■■\033[32;1m█\033[33;1m■■■■' '\033[33;1m■\033[32;1m█\033[33;1m■■■■■' '\033[32;1m█\033[33;1m■■■■■■' )

  while [ "$(ps -p $pid)" ]; do
    for i in "${spinner[@]}"; do
      echo -ne "\r$CC [$YY↓$CC]$YY Downloading please wait...$CC 【$i$CC】";
      sleep $delay
      printf "\b\b\b\b\b\b\b\b";
    done
  done
  printf "   \b\b\b\b\b"
  printf "$WW⟫$GG Completed.\n";
  echo "";
}

# Colors
BB="\033[34;1m" # Blue Light
YY="\033[33;1m" # Yellow Light
GG="\033[32;1m" # Green Light
WW="\033[0;1m"  # White Light
RR="\033[31;1m" # Red Light
CC="\033[36;1m" # Cyan Light
MM="\033[35;1m" # Magenta Light
B="\033[34;1m"  # Blue
Y="\033[33;1m"  # Yellow
G="\033[32;1m"  # Green
W="\033[0;1m"   # White
R="\033[31;1m"  # Red
C="\033[36;1m"  # Cyan
M="\033[35;1m"  # Magenta

# Log File
LOGFILE="terpack_install.log"
exec 3>&1 1>>${LOGFILE} 2>&1

# Başlangıç mesajı ve Temizlik
clear; echo -e "$CC\n [$YY↓$CC]$GG Updating...\n"
rm -rf Terpack.sh
cd ~/
curl -fsSL https://raw.githubusercontent.com/TheDarkRoot/Terpack/master/Terpack.sh -o Terpack.sh
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Terpack.sh indirilemedi.$WW" >&3
  exit 1
fi
chmod +x Terpack.sh
apt update -y && apt upgrade -y

# Hata kontrolü
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Paket listesi güncellenemedi.$WW" >&3
  exit 1
fi

# Banner
clear; echo -e "
$CC #######$YY ##################$CC ######$YY #####################
$CC    #    ###### #####       #     #  ####   ####  #    #
$CC    #    #      #    #      #     # #    # #    # #   #
$CC    #    ###### #    #  ##  ######  #    # #      ####
$CC    #    #      #####       #       ###### #      #  #
$CC    #    #      #   #       #       #    # #    # #   #
$CC    #    ###### #    #      #       #    #  ####  #    #
$YY ###################[›$GG TheDarkRoot $YY‹]###################\n
$GG 0{======================$WW INFO $GG=======================}0
$GG |$YY [$CC=$YY]$WW Name     $CC:$WW Terpack$GG                              |
$GG |$YY [$CC=$YY]$WW Code     $CC:$WW Shell$GG                                |
$GG |$YY [$CC=$YY]$WW Version  $CC:$WW v1.2.7 (Alpha)$GG                       |
$GG |$YY [$CC=$YY]$WW Author   $CC:$WW TheDarkRoot$GG                          |
$GG |$YY [$CC=$YY]$WW Email    $CC:$WW 7H3D4RKR007@gmail.com$GG                |
$GG |$YY [$CC=$YY]$WW Github   $CC:$WW https://github.com/TheDarkRoot$GG       |
$GG |$YY [$CC=$YY]$WW Telegram $CC:$WW @TheDarkRoot (t.me/TheDarkRoot)$GG      |
$GG |$YY [$CC=$YY]$WW Team     $CC:$WW TurkHackTeam (www.turkhackteam.org)$GG  |
$GG 0{===================================================}0\n"

# Paketlerin kurulumu
echo -e "$CC [$YY»$CC]$GG Packages Installing...";
(
  pkg install -y ruby git python python2 python3 python-pip php zip unzip cowsay figlet wget curl vim proot crunch neofetch nano cmatrix toilet zsh sl tmate bash tor privoxy termux-api termux-tools play-audio mpv openssh openssl-tool
) &> /dev/null & spin

# Hata kontrolü
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Paketler kurulamadı.$WW" >&3
  exit 1
fi

# Araçların kurulumu
echo -e "$CC [$YY»$CC]$GG Tools Installing...";
(
  gem install lolcat;
  pip3 install --upgrade pip;
  pip3 install bs4 requests mechanize passlib progressbar2 pillow termcolor speedtest speedtest-cli;
  pkg install -y nodejs nodejs-lts;
  npm install readline-sync;
  npm install;
  npm install --global speed-test;
) &> /dev/null & spin

# Hata kontrolü
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Araçlar kurulamadı.$WW" >&3
  exit 1
fi

# TheDarkroot Repositories Download
echo -e "$CC [$YY»$CC]$GG Tdr-Tool Installing...";
(
  cd ~/;
  curl -fsSL https://raw.githubusercontent.com/TheDarkRoot/FileStore/master/Software%20Files/Tdr-Tool.termux -o Tdr-Tool.sh;
  if [ $? -ne 0 ]; then
    echo -e "$RR Hata: Tdr-Tool.sh indirilemedi.$WW" >&3
    exit 1
  fi
  chmod +x Tdr-Tool.sh;
  bash Tdr-Tool.sh;
  rm -rf Tdr-Tool.sh;
) &> /dev/null & spin

# Hata kontrolü
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Tdr-Tool kurulamadı.$WW" >&3
  exit 1

fi

# Termux Setups Update
echo -e "$CC [$YY»$CC]$GG Termux Setup Updating...";
(
  cd /data/data/com.termux/files/usr/etc/
  curl -fsSL https://raw.githubusercontent.com/TheDarkRoot/FileStore/master/Software%20Files/TheDarkRoot.termux -o bash.bashrc
  if [ $? -ne 0 ]; then
    echo -e "$RR Hata: bash.bashrc indirilemedi.$WW" >&3
    exit 1
  fi
  cd ~/.termux/
  curl -fsSL https://raw.githubusercontent.com/TheDarkRoot/FileStore/master/Software%20Files/Terkey.termux -o termux.properties
  if [ $? -ne 0 ]; then
    echo -e "$RR Hata: termux.properties indirilemedi.$WW" >&3
    exit 1
  fi
  cd ~/
  rm -rf storage
  termux-setup-storage
  termux-reload-settings
) &> /dev/null & spin

# Hata kontrolü
if [ $? -ne 0 ]; then
  echo -e "$RR Hata: Termux ayarları güncellenemedi.$WW" >&3
  exit 1
fi

echo -e "$CC [$YY»$CC]$GG Update Successful.\n"
