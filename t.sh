#!/bin/bash
spin () {
local pid=$!
local delay=0.10
local spinner=( '\033[34;1m■■■■■■■' '\033[32;1m█\033[33;1m■■■■■■' '\033[33;1m■\033[32;1m█\033[33;1m■■■■■' '\033[33;1m■■\033[32;1m█\033[33;1m■■■■' '\033[33;1m■■■\033[32;1m█\033[33;1m■■■' '\033[33;1m■■■■\033[32;1m█\033[33;1m■■' '\033[33;1m■■■■■\033[32;1m█\033[33;1m■' '\033[33;1m■■■■■■\033[32;1m█' '\033[34;1m■■■■■■■' '\033[33;1m■■■■■■\033[32;1m█' '\033[33;1m■■■■■\033[32;1m█\033[33;1m■' '\033[33;1m■■■■\033[32;1m█\033[33;1m■■' '\033[33;1m■■■\033[32;1m█\033[33;1m■■■' '\033[33;1m■■\033[32;1m█\033[33;1m■■■■' '\033[33;1m■\033[32;1m█\033[33;1m■■■■■' '\033[32;1m█\033[33;1m■■■■■■' )

while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do

for i in "${spinner[@]}"
do
  echo -ne "\r$CC [$YY↓$CC]$YY Downloading please wait...$CC 【$i$CC】";
  sleep $delay
  printf "\b\b\b\b\b\b\b\b";
done
done
printf "   \b\b\b\b\b"
printf "$WW⟫$GG Completed.\n";
echo "";
}
#Colors
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
clear;

while true; do
clear;echo -e "
$CC #######$YY ##################$CC #######$YY ####################
$CC    #    #####  #####          #     ####   ####  #
$CC    #    #    # #    #         #    #    # #    # #
$CC    #    #    # #    #  #####  #    #    # #    # #
$CC    #    #    # #####          #    #    # #    # #
$CC    #    #    # #   #          #    #    # #    # #
$CC    #    #####  #    #         #     ####   ####  ######
$YY ###################[›$GG TheDarkRoot $YY‹]###################
$CC =======================================================
$CC ┌⊸⟜┬───⊸ [$MM TheDarkRoot Repositories: $CC]
$CC │  ├─┬─⊸ [$YY›1$YY‹$RR AnonSMS$CC]
$CC │  │ └─⊸ [$YY »$GG Anonymous SMS sending tool.$CC]
$CC │  ├─┬─⊸ [$YY›2$YY‹$RR Hasher$CC]
$CC │  │ └─⊸ [$YY »$GG This is a Hash Cracker.$CC]
$CC │  ├─┬─⊸ [$YY›3$YY‹$RR Hashgen$CC]
$CC │  │ └─⊸ [$YY »$GG Generate more 39 type hash.$CC]
$CC │  ├─┬─⊸ [$YY›4$YY‹$RR Terpack$CC]
$CC │  │ └─⊸ [$YY »$GG TheDarkRoot termux package installer.$CC]
$CC │  ├─┬─⊸ [$YY›5$YY‹$RR Tertest$CC]
$CC │  │ └─⊸ [$YY »$GG Termux internet speed test.
$CC │  ├─┬─⊸ [$YY›6$YY‹$RR Tertext$CC]
$CC │  │ └─⊸ [$YY »$GG Program for creating words from letters.$CC]
$CC │  ├─┬─⊸ [$YY›7$YY‹$RR UserID$CC]
$CC │  │ └─⊸ [$YY »$GG Search usernames on social media.$CC]
$CC │  └─┬─⊸ [$YY›X$YY‹$RR X-Project$CC]
$CC │    └─⊸ [$YY »$GG Code in the trial period.$CC]
$CC └⊸⟜┬───⊸ [$MM Termux Settings: $CC]
$CC    ├─┬─⊸ [$YY›U$YY‹$RR Update$CC]
$CC    │ └─⊸ [$YY »$GG Termux update.$CC]
$CC    ├─┬─⊸ [$YY›P$YY‹$RR ParrotOS-T$CC]
$CC    │ └─⊸ [$YY »$GG Parrot OS theme for Termux.$CC]
$CC    ├─┬─⊸ [$YY›T$YY‹$RR TheDarkRoot-T$CC]
$CC    │ └─⊸ [$YY »$GG TheDarkRoot theme for Termux.$CC]
$CC    ├─┬─⊸ [$YY›K$YY‹$RR Terkey$CC]
$CC    │ └─⊸ [$YY »$GG Utility to add direction keys to Termux.$CC]
$CC    └─┬─⊸ [$YY›Q$YY‹$RR Exit$CC]
$CC      └─⊸ [$YY »$GG Tdr-Tool exit.$CC]\n"

read -p " $(echo -e " ${CC}[${YY}»${CC}]${MM} Program Number:ⓘ 🛈 ℹ️ \u2139🛈🛈🛈 ${YY}")" pn
	
	if [[ $pn == U || $pn == u ]]; then
	clear;echo -e "$CC\n [$YY↓$CC]$GG Updating...\n";apt update -y;apt upgrade -y;clear;
	#Termux Packages Installing
	echo -e "$CC [$YY»$CC]$GG Packages Installing...";
	( pkg install ruby git python python2 python3 python-pip php zip unzip cowsay figlet wget curl vim proot crunch neofetch nano cmatrix toilet zsh sl tmate bash tor privoxy -y;pkg install termux-api termux-tools play-audio mpv openssh openssl-tool crunch -y; ) &> /dev/null & spin;
	#Termux Tools Installing
	echo -e "$CC [$YY»$CC]$GG Tools Installing...";
	( gem install lolcat;pip3 install --upgrade pip;pip3 install bs4 requests mechanize passlib progressbar2 pillow termcolor speedtest speedtest-cli;pkg install nodejs -y;pkg install nodejs-lts -y;npm install readline-sync;npm install;npm install --global speed-test; ) &> /dev/null & spin;
	#Termux Tdr-Tool Updating
	echo -e "$CC [$YY»$CC]$GG Tdr-Tool Updating...$YY";
	( cd ~/Tdr-Tool/;curl https://raw.githubusercontent.com/TheDarkRoot/Tdr-Tool/master/Tdr-Tool.sh -o Tdr-Tool.sh; ) &> /dev/null & spin;

	elif [[ $pn == P || $pn == p ]]; then
	echo -e "\n$CC [$YY»$CC]$GG Updating Parrot OS theme...\n$CC [\033[33;1mi$CC]$GG Parrot OS theme for Termux.";
	( cd ~/Tdr-Tool;curl https://raw.githubusercontent.com/TheDarkRoot/ParrotOS-T/master/ParrotOS-T.sh -o ParrotOS-T.sh;chmod +x ParrotOS-T.sh;bash ParrotOS-T.sh;cd ~/Tdr-Tool;rm -rf ParrotOS-T.sh; ) &> /dev/null & spin;

	elif [[ $pn == T || $pn == t ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Updating TheDarkRoot theme...\n$CC [\033[33;1mi$CC]$GG TheDarkRoot theme for Termux.";
	( cd ~/Tdr-Tool;curl https://raw.githubusercontent.com/TheDarkRoot/TheDarkRoot-T/master/TheDarkRoot-T.sh -o TheDarkRoot-T.sh;chmod +x TheDarkRoot-T.sh;bash TheDarkRoot-T.sh;cd ~/Tdr-Tool;rm -rf TheDarkRoot-T.sh; ) &> /dev/null & spin;

	elif [[ $pn == K || $pn == k ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Updating Termux key...\n$CC [\033[33;1mi$CC]$GG Utility to add direction keys to Termux.";
	( cd ~/Tdr-Tool;curl https://raw.githubusercontent.com/TheDarkRoot/Terkey/master/Terkey.sh -o Terkey.sh;chmod +x Terkey.sh;bash Terkey.sh;cd ~/Tdr-Tool;rm -rf Terkey.sh; ) &> /dev/null & spin;

	elif [[ $pn == BASH || $pn == bash ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Tdr-Tool Updating...\n$CC [\033[33;1mi$CC]$GG Utility to add direction keys to Termux.";
	( cd ~/Tdr-Tool/;rm -rf Tdr-Tool.sh;curl https://raw.githubusercontent.com/TheDarkRoot/Tdr-Tool/master/Tdr-Tool.sh -o Tdr-Tool.sh; ) &> /dev/null & spin;

	elif [[ $pn == Q || $pn == q ]]; then
    echo -e "\n $CC [$YY»$CC]$RR Good bye...";
	sleep 0;exit;

	elif [[ $pn == 1 || $pn == 01 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading AnonSMS...\n$CC [\033[33;1mi$CC]$GG TheDarkRoot tool pack.";
	( cd ~/Tdr-Tool;rm -rf AnonSMS;git clone https://github.com/TheDarkRoot/AnonSMS.git;cd AnonSMS;chmod +x *; ) &> /dev/null & spin;

	elif [[ $pn == 2 || $pn == 02 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading Hasher...\n$CC [\033[33;1mi$CC]$GG This is a Hash Cracker.";
	( cd ~/Tdr-Tool;rm -rf Hasher;git clone https://github.com/TheDarkRoot/Hasher.git;cd Hasher;chmod +x *; ) &> /dev/null & spin;

	elif [[ $pn == 3 || $pn == 03 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading Hashgen...\n$CC [\033[33;1mi$CC]$GG Generate more 39 type hash.";
	( cd ~/Tdr-Tool;rm -rf Hashgen;git clone https://github.com/TheDarkRoot/Hashgen.git;cd Hashgen;chmod +x *; ) &> /dev/null & spin;

	elif [[ $pn == 4 || $pn == 04 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading Terpack...\n$CC [\033[33;1mi$CC]$GG TheDarkRoot termux package installer.";
	( cd ~/Tdr-Tool;rm -rf Terpack;git clone https://github.com/TheDarkRoot/Terpack.git;cd Terpack;chmod +x *;cp Terpack.sh ~; ) &> /dev/null & spin;
		
	elif [[ $pn == 5 || $pn == 05 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading Tertest...\n$CC [\033[33;1mi$CC]$GG Termux internet speed test.";
	( cd ~/Tdr-Tool;rm -rf Tertest;git clone https://github.com/TheDarkRoot/Tertest.git;cd Tertest;chmod +x *; ) &> /dev/null & spin;

	elif [[ $pn == 6 || $pn == 06 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading Tertext...\n$CC [\033[33;1mi$CC]$GG Program for creating words from letters.";
	( cd ~/Tdr-Tool;rm -rf Tertext;git clone https://github.com/TheDarkRoot/Tertext.git;cd Tertext;chmod +x *; ) &> /dev/null & spin;

	elif [[ $pn == 7 || $pn == 07 ]]; then
    echo -e "\n$CC [$YY»$CC]$GG Downloading UserID...\n$CC [\033[33;1mi$CC]$GG Search usernames on social media.";
	( cd ~/Tdr-Tool;rm -rf UserID;git clone https://github.com/TheDarkRoot/UserID.git;cd UserID;chmod +x *; ) &> /dev/null & spin;

	else
	echo -e "\n  ${YY}[${RR}⦸${YY}]${RR} Invalid Action."	
	sleep 1
	
    fi
done
