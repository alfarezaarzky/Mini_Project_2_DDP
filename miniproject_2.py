# Muhammad Rizky Alfa Reza Basyah
# 2509116086
# Sistem Informasi C
# Mini Project 2

data_parkir = {}

users = {
    "manager": {"password": "12345", "role": "manager"},
    "karyawan": {"password": "99990", "role": "karyawan"}
}
def login():
    print("---Login Sistem Parkir---")
    username = input("masukkan usernamee: ")
    password = input("masukkan password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil sebagai {users[username]['role']}")
        return users[username]["role"]
    else:
        print("Username atau password salah")

def tambah_data():
    try:
        no_plat = input("Masukkan nomor plat kendaraan: ")
        jenis_kendaraan = input("Masukkan jenis kendaraan: ")
        waktu_masuk = input("Masukkan waktu masuk kendaraan: ")
        data_parkir[no_plat] = {"jenis": jenis_kendaraan, "waktu": waktu_masuk}
        print("data kendaraan berhasil ditambahkann")
    except Exception as error:
        print("Terjadi kesalahan saat menambah data:", error)

def lihat_data():
    print("---Daftar Parkir Kendaraan---")
    if not data_parkir:
        print("Belum ada data kendaraan.")
    else:
        for no_plat, info in data_parkir.items():
            print(f"{no_plat} | {info['jenis']} | {info['waktu']}")

def ubah_data():
    try:
        no_plat = input("Masukkan nomor plat kendaraan yang ingin diubah: ")
        if no_plat in data_parkir:
            jenis_kendaraan = input("Masukkan jenis kendaraan baru: ")
            waktu_masuk = input("Masukkan waktu masuk baru: ")
            data_parkir[no_plat] = {"jenis": jenis_kendaraan, "waktu": waktu_masuk}
            print("Data kendaraan berhasil diubah")
        else:
            print("Data kendaraan tidak ditemukan")
    except Exception as error:
        print("Terjadi kesalahan saat mengubah data:", error)

def hapus_data():
    try:
        no_plat = input("Masukkan nomor plat kendaraan yang ingin dihapus: ")
        if no_plat in data_parkir:
            del data_parkir[no_plat]
            print("Data kendaraan berhasil dihapus")
        else:
            print("Data kendaraan tidak ditemukan")
    except Exception as error:
        print("Terjadi kesalahan saat menghapus data:", error)

role = login()
if role:
    while True:
        print("---Menu Parkir Kendaraan---")
        print("1. Lihat data kendaraan")
        if role == "karyawan":
            print("2. tambah data kendaraan")
            print("3. Ubah data kendaaran")
            print("4. hapus data kendaran")
            print("5. Keluar")
        else:
            print("2. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            lihat_data()
        elif pilihan == "2" and role == "karyawan":
            tambah_data()
        elif pilihan == "3" and role == "karyawan":
            ubah_data()
        elif pilihan == "4" and role == "karyawan":
            hapus_data()
        elif (pilihan == "5" and role == "karyawan") or (pilihan == "2" and role == "manager"):
            print("selesai")
            break
        else:
            print("Pilihan tidak valid")
