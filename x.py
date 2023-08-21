import sys
from fast_speedtest import FastSpeedtest
from termcolor import colored
import random

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

# Tertest Banner
print(f"\n{P} #######{YY} ##################{P} #######{YY} ####################")
print(f"{P}    #    ###### #####          #    ######  ####  #####")
print(f"{P}    #    #      #    #         #    #      #        #")
print(f"{P}    #    ###### #    #  ##     #    #####   ####    #")
print(f"{P}    #    #      #####          #    #           #   #")
print(f"{P}    #    #      #   #          #    #      #    #   #")
print(f"{P}    #    ###### #    #         #    ######  ####    #")
print(f"{YY}####################[{GG} TheDarkRoot{YY} ]####################\n")
print(f"{GG}0{WW}{{======================{GG} INFO {WW}=======================}}0")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Name     {CC}:{WW} Tertest{GG}                              |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Code     {CC}:{WW} Python{GG}                               |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Version  {CC}:{WW} v1.0.0 (Alpha){GG}                       |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Author   {CC}:{WW} TheDarkRoot{GG}                          |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Email    {CC}:{WW} 7H3D4RKR007@gmail.com{GG}                |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Github   {CC}:{WW} https://github.com/TheDarkRoot{GG}       |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Telegram {CC}:{WW} @TheDarkRoot (t.me/TheDarkRoot){GG}      |")
print(f"{GG}|{YY} [{CC}={YY}]{WW} Team     {CC}:{WW} TurkHackTeam (www.turkhackteam.org){GG}  |")
print(f"{GG}0{WW}{{===================================================}}0\n")

def print_speed(speed, unit):
    if unit == 'Mbps':
        if speed >= 50:
            color = 'green'
        elif speed >= 20:
            color = 'yellow'
        else:
            color = 'red'
    else:
        color = 'white'

    print(colored(f"{speed:.2f} {unit}", color))

def run_speed_test():
    print(colored("Bağlantı hızı testi başlıyor...", "blue"))
    print()

    try:
        st = FastSpeedtest()  # fast-speedtest-api'yi kullanıyoruz
        download_speed = st.download() / 10 ** 6  # Mbps cinsinden indirme hızı
        upload_speed = st.upload() / 10 ** 6  # Mbps cinsinden yükleme hızı
        ping = st.ping()  # Ping süresi

        print(colored("İndirme Hızı:", "cyan"))
        print_speed(download_speed, 'Mbps')

        print(colored("\nYükleme Hızı:", "cyan"))
        print_speed(upload_speed, 'Mbps')

        print(colored("\nPing:", "cyan"))
        print_speed(ping, 'ms')

        print()
        print(colored("Bağlantı hızı testi tamamlandı.\n", "green"))

    except Exception as e:
        print(colored(f"Bağlantı hızı testi yapılırken bir hata oluştu: {e}\n", "red"))

if __name__ == "__main__":
    run_speed_test()
