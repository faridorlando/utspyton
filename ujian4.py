# Soal 4 - Data Jadwal dengan List/Dict
# Program menampilkan jadwal kuliah berdasarkan hari (versi input interaktif)

def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari yang dimasukkan pengguna.
    Pencarian dilakukan dengan mengecek satu per satu isi list jadwal.
    """

    # Data jadwal disimpan dalam dictionary dengan key = hari
    jadwal = {
        "Senin": ["Pemrograman Python", "Basis Data"],
        "Selasa": ["Algoritma & Struktur Data", "Sistem Operasi"],
        "Rabu": ["Jaringan Komputer", "Kewirausahaan"],
        "Kamis": ["Pemrograman Java", "Analisis Sistem"],
        "Jumat": ["Desain UI/UX", "Etika Profesi"]
    }

    # Normalisasi input agar huruf besar/kecil tidak berpengaruh
    hari = hari.capitalize()

    # Cek apakah hari ada di data jadwal
    if hari in jadwal:
        print(f"\n📅 Jadwal kuliah hari {hari}:")
        for mata_kuliah in jadwal[hari]:
            print(f"- {mata_kuliah}")
    else:
        print("\n❌ Hari tidak ditemukan dalam jadwal.")

# 🔹 Program utama
print("=== PROGRAM JADWAL KULIAH HARIAN ===")
hari_input = input("Masukkan nama hari (misal: Senin, Selasa, dst): ")
jadwal_hari(hari_input)
