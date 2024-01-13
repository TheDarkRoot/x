import sys
from speedtest import Speedtest
from termcolor import colored

# Renkleri platforma göre ayarla
if sys.platform == "linux" or sys.platform == "linux2":
    BB = "\033[34;1m"  # Blue Light
    YY = "\033[33;1m"  # Yellow Light
    GG = "\033[32;1m"  # Green Light
    WW = "\033[0;1m"   # White Light
    RR = "\033[31;1m"  # Red Light
    CC = "\033[36;1m"  # Cyan Light
    MM = "\033[35;1m"  # Magenta Light
else:
    # Renkleri Windows veya diğer platformlara uyarla
    BB = "Mavi"
    YY = "Sarı"
    GG = "Yeşil"
    WW = "Beyaz"
    RR = "Kırmızı"
    CC = "Camgöbeği"
    MM = "Eflatun"

# Tertest giriş başlığı
print(colored(f"\n{BB} #######{YY} ##################{BB} #######{YY} ####################", WW))
# ... (Başlık metninin geri kalanını buraya ekleyin)

def print_speed(speed, unit):
    if unit == 'Mbps':
        if speed >= 50:
            color = GG
        elif speed >= 20:
            color = YY
        else:
            color = RR
    else:
        color = WW

    print(colored(f"{speed:.2f} {unit}", color))

def run_speed_test():
    print(colored("Bağlantı hızı testi başlıyor...", BB))
    print()

    try:
        st = Speedtest()
        st.get_best_server()

        print(colored("İndirme:", CC))
        download_speed = st.download() / 10 ** 6  # Mbps'ye dönüştür
        print_speed(download_speed, 'Mbps')

        print(colored("\nYükleme:", CC))
        upload_speed = st.upload() / 10 ** 6  # Mbps'ye dönüştür
        print_speed(upload_speed, 'Mbps')

        print(colored("\nPing:", CC))
        ping = st.results.ping
        print_speed(ping, 'ms')

        print()
        print(colored("Bağlantı hızı testi tamamlandı.\n", GG))

    except speedtest.SpeedtestException:
        print(colored("Hız testi sırasında bir hata oluştu\n", RR))

if __name__ == "__main__":
    run_speed_test()
