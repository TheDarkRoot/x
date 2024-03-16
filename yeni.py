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
    print("1. Metin Hashleme (Hashgen)")
    print("2. Dosya Hashleme (Hasher)")
    print("3. Çıkış")
    print("=" * 20)

    choice = input("Seçiminizi giriniz (1, 2 veya 3): ")

    while choice not in ("1", "2", "3"):
        choice = input("Geçersiz seçim. Lütfen tekrar deneyin (1, 2 veya 3): ")

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
    print("Metin Hashleme (Hashgen)")
    print("=" * 20)
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256")
    print("4. Algoritma Listesi")
    print("5. Geri Dön")
    print("=" * 20)

    choice = input("Seçiminizi giriniz (1, 2, 3, 4 veya 5): ")

    while choice not in ("1", "2", "3", "4", "5"):
        choice = input("Geçersiz seçim. Lütfen tekrar deneyin (1, 2, 3, 4 veya 5): ")

    if choice == "1":
        algorithm = "md5"
        hash_text(algorithm)
    elif choice == "2":
        algorithm = "sha1"
        hash_text(algorithm)
    elif choice == "3":
        algorithm = "sha256"
        hash_text(algorithm)
    elif choice == "4":
        list_algorithms()
    else:
        main()

def hash_text(algorithm):
    # Metin girişi
    text = input("Metni giriniz: ")

    # Hash hesaplama
    hash_value = hashlib.new(algorithm, text.encode()).hexdigest()

    # Sonuç gösterimi
    clear_screen()
    print("=" * 20)
    print("Hash Sonucu")
    print("=" * 20)
    print(f"Algoritma: {algorithm.upper()}")
    print(f"Metin: {text}")
    print(f"Hash Değeri: {hash_value}")
    print("=" * 20)

    input("Devam etmek için Enter'a basın...")

def list_algorithms():
    # Tüm algoritmaların listesi
    algorithms = hashlib.algorithms_available
    clear_screen()
    print("=" * 20)
    print("Mevcut Hash Algoritmaları")
    print("=" * 20)
    for algo in algorithms:
        print(f"- {algo}")
    print("=" * 20)
    input("Devam etmek için Enter'a basın...")

def hasher():
    # Dosya yolu yerine Wordlist.txt dosyası kullanımı
    file_path = "Wordlist.txt"

    # Hash algoritması seçimi
    algorithms = {"md5": "MD5", "sha1": "SHA-1", "sha256": "SHA-256"}
    for algo, name in algorithms.items():
        print(f"{algo}: {name}")
    algorithm = input("Hash algoritmasını seçiniz: ").lower()
    while algorithm not in algorithms:
        algorithm = input("Geçersiz algoritma. Lütfen tekrar deneyin: ").lower()

    # Hash hesaplama
    with open(file_path, "r") as f:
        for word in f.readlines():
            word = word.strip()
            hash_value = hashlib.new(algorithm, word.encode()).hexdigest()
            print(f"{word}: {hash_value}")

if __name__ == "__main__":
    main()
