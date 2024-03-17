#!/bin/bash
# -*- coding: utf-8 -*-

# Döndürme İşlevi
function spin() {
  local pid=<span class="math-inline">\!
local delay\=0\.10
local spinner\=\( '\\033\[34;1m■■■■■■■' '\\033\[32;1m█\\033\[33;1m■■■■■■' '\\033\[33;1m■\\033\[32;1m█\\033\[33;1m■■■■■' '\\033\[33;1m■■\\033\[32;1m█\\033\[33;1m■■■■' '\\033\[33;1m■■■\\033\[32;1m█\\033\[33;1m■■■' '\\033\[33;1m■■■■\\033\[32;1m█\\033\[33;1m■■' '\\033\[33;1m■■■■■\\033\[32;1m█\\033\[33;1m■' '\\033\[33;1m■■■■■■\\033\[32;1m█' '\\033\[34;1m■■■■■■■' '\\033\[33;1m■■■■■■\\033\[32;1m█' '\\033\[33;1m■■■■■\\033\[32;1m█\\033\[33;1m■' '\\033\[33;1m■■■■\\033\[32;1m█\\033\[33;1m■■' '\\033\[33;1m■■■\\033\[32;1m█\\033\[33;1m■■■' '\\033\[33;1m■■\\033\[32;1m█\\033\[33;1m■■■■' '\\033\[33;1m■\\033\[32;1m█\\033\[33;1m■■■■■' '\\033\[32;1m█\\033\[33;1m■■■■■■' \)
while \[ "</span>(ps a | awk '{print $1}' | grep <span class="math-inline">pid\)" \]; do
for i in "</span>{spinner[@]}"
    do
      echo -ne "\r$CC [$YY↓$CC]$GG Downloading please wait...$CC 【$i$CC】";
      sleep $delay
      printf "\b\b\b\b\b\b\b\b";
    done
  done
  printf "  \b\b\b\b\b"
  printf "$WW⟫$GG Completed.\n";
  echo "";
}

# Renk Kodları
BB="\033[34;1m" # Mavi Açık
YY="\033[33;1m" # Sarı Açık
GG="\033[32;1m" # Yeşil Açık
WW="\033[0;1m"  # Beyaz Açık
RR="\033[31;1m" # Kırmızı Açık
CC="\033[36;1m" # Turkuaz Açık
MM="\033[35;1m" # Pembe Açık
B="\033[34;1m" # Mavi
Y="\033[33;1m" # Sarı
G="\033[32;1m" # Yeşil
W="\033[0;1m"  # Beyaz
R="\033[31;1m" # Kırmızı
C="\033[36;1m" # Turkuaz
M="\033[35;1m" # Pembe

# Kütüphanelerin Kurulum Kontrolü
function install_library() {
  library_name="$1"
  package_manager="$2"

  echo "Installing $library_name..."

  $package_manager install --upgrade "$library_name" --check-deps || {
    echo "Error installing $library_name"
    exit 1
  }

  echo "$library_name installed successfully"
}

# Termux Paket
