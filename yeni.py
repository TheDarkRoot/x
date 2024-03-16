import os
import hashlib

def clear_screen():
    os.system('clear')

def main():
    # Ana menü arayüzü
    clear_screen()
    print("=" * 20)
    print("Hash İşlemleri")
    print("=" * 20)
    print("1. Hashgen")
    print("2. Hasher")
    print("0. Çıkış")
    print("=" * 20)

    choice = input("Seçiminizi giriniz: ")

    while choice not in ("0", "1", "2"):
        choice = input("Geçersiz seçim. Lütfen tekrar deneyin: ")

    if choice == "1":
        hashgen()
    elif choice == "2":
        hasher()
    else:
        exit()

def hashgen():
    # Hash algoritması seçimi
    clear_screen()
    print("=" * 20)
    print("Hashgen")
    print("=" * 20)
    algorithms = {"md5": "MD5", "sha1": "SHA-1", "sha256": "SHA-256"}
    for algo, name in algorithms.items():
        print(f"{algo}: {name}")
    algorithm = input("Hash algoritmasını seçiniz: ").lower()
    while algorithm not in algorithms:
        algorithm = input("Geçersiz algoritma. Lütfen tekrar deneyin: ").lower()

    # Metin girişi
    text = input("Metni giriniz: ")

    # Hash hesaplama
    hash_value = hashlib.new(algorithm, text.encode()).hexdigest()

    # Sonuç gösterimi
    clear_screen()
    print("=" * 20)
    print("Hash Sonucu")
    print("=" * 20)
    print(f"Algoritma: {algorithms[algorithm]}")
    print(f"Metin: {text}")
    print(f"Hash Değeri: {hash_value}")
    print("=" * 20)

    input("Devam etmek için Enter'a basın...")

def hasher():
    # Dosya seçimi
    clear_screen()
    print("=" * 20)
    print("Hasher")
    print("=" * 20)
    file_path = input("Dosya yolunu giriniz: ")

    # Hash algoritması seçimi
    algorithms = {"md5": "MD5", "sha1": "SHA-1", "sha256": "SHA-256"}
    for algo, name in algorithms.items():
        print(f"{algo}: {name}")
    algorithm = input("Hash algoritmasını seçiniz: ").lower()
    while algorithm not in algorithms:
        algorithm = input("Geçersiz algoritma. Lütfen tekrar deneyin: ").lower()

    # Hash hesaplama
    with open(file_path, "rb") as f:
        hash_value = hashlib.new(algorithm, f.read()).hexdigest()

    # Sonuç gösterimi
    clear_screen()
    print("=" * 20)
    print("Hash Sonucu")
    print("=" * 20)
    print(f"Dosya: {file_path}")
    print(f"Algoritma: {algorithms[algorithm]}")
    print(f"Hash Değeri: {hash_value}")
    print("=" * 20)

    input("Devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
