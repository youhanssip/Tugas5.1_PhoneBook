# Library
import os

# Untuk merujuk kepada file TXT yang digunakan untuk menyimpan data
phoneBook_file = "phoneBook.txt"

# Untuk menampilkan nomer yang ada pada file
phoneBook = {}
with open(phoneBook_file, "r") as f:
    for line in f:
        name, number = line.strip().split(":")
        phoneBook[name] = number
while True:
    print("Phone Book\n")
    # Menampilkan data Phone Book yang ada
    if phoneBook:
        print("Kontak: ")
        for name, number in phoneBook.items():
            print(f"{name}: {number}")
        print()

    # Main Menu
                                                                                
    print(",------. ,--.                               ,-----.                ,--.     ")
    print("|  .--. '|  ,---.  ,---. ,--,--,  ,---.     |  |) /_  ,---.  ,---. |  |,-.  ")
    print("|  '--' ||  .-.  || .-. ||      \| .-. :    |  .-.  \| .-. || .-. ||     /  ")
    print("|  | --' |  | |  |' '-' '|  ||  |\   --.    |  '--' /' '-' '' '-' '|  \  \  ")
    print("`--'     `--' `--' `---' `--''--' `----'    `------'  `---'  `---' `--'`--'")
    print("============================================================================")                                                               
    print("Silahkan Pilih Menu:")
    print("1. Tambahkan Kontak Baru")
    print("2. Update Kontak yang Sudah Ada")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("5. Keluar")

    pilihan = input("Silahkan Input Pilihannya (1-5): ")
    os.system('cls')
# Menambah Kontak Baru
    if pilihan == "1":
        name = input("Masukan Nama Kontak: ")
        number = input("Masukan Nomer Kontak: ")
        phoneBook[name] = number
        print(f"{name} Berhasil Ditambahkan\n")

    # Mengupdate Kontak yang Sudah Ada
    elif pilihan == "2":
        name = input("Masukan Nama Kontak: ")
        if name in phoneBook:
            number = input("Masukan Nomer Kontak: ")
            phoneBook[name] = number
            print(f"Nomor {name} Sudah Diupdate.\n")
        else:
            print(f"Nomor {name} Tidak Ditemukan.\n")

    # Menghapus Kontak yang Sudah Ada
    elif pilihan == "3":
        name = input("Masukan Nama Kontak: ")
        if name in phoneBook:
            del phoneBook[name]
            print(f"Nomor {name} Berhasil Dihapus.\n")
        else:
            print(f"Nomor {name} Tidak Ditemukan.\n")

    # Mencari Kontak
    elif pilihan == "4":
        name = input("Masukan Nama Kontak: ")
        if name in phoneBook:
            print(f"{name}: {phoneBook[name]}\n")
        else:
            print(f"{name} Tidak Ditemukan.\n")

    # Keluar dari Program
    elif pilihan == "5":
        # Menuliskan Data ke Dalam File
        with open(phoneBook_file, "w") as f:
            for name, number in phoneBook.items():
                f.write(f"{name}:{number}\n")

        print("Terimakasih Sampai Jumpa!")
        break

    # Plihan Invalid
    else:
        print("Input Invalid Silahkan Coba lagi.\n")
