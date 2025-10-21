# Soal 3 - Fungsi & Parameter Bawaan
# Program menghitung ongkir layanan RapidSend

def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkir layanan Berkah Jaya berdasarkan kota tujuan,
    berat barang (kg), dan pilihan asuransi.
    """
    tarif_dasar = {
        "Solo": 8000,
        "Jogja": 10000,
        "Semarang": 12000,
        "Sragen": 9000
    }

    # Validasi input berat
    if berat_kg <= 0:
        return "❌ Berat harus lebih dari 0 kg."

    # Validasi kota
    if kota not in tarif_dasar:
        return "❌ Kota tidak tersedia dalam daftar."

    # Hitung total ongkir
    total = tarif_dasar[kota] + (2000 * berat_kg)
    biaya_asuransi = 3000 if asuransi else 0
    total += biaya_asuransi

    # Tampilkan hasil dalam format struk ongkir
    print("\n===== STRUK ONGKIR BERKAH JAYA =====")
    print(f"Kota Tujuan     : {kota}")
    print(f"Berat Barang    : {berat_kg} kg")
    print(f"Tarif Dasar     : Rp {tarif_dasar[kota]:,}")
    print(f"Biaya Tambahan  : Rp {2000 * berat_kg:,}")
    print(f"Asuransi        : {'Ya (Rp 3.000)' if asuransi else 'Tidak'}")
    print("-----------------------------------")
    print(f"Total Ongkir    : Rp {total:,}")
    print("===================================\n")

    return total


# 🔹 Program Utama (Input dari Pengguna)
print("=== Program Hitung Ongkir BERKAH JAYA ===")
print("Daftar kota yang tersedia: Solo, Jogja, Semarang, Sragen")

# Input dari pengguna
kota = input("Masukkan kota tujuan: ").capitalize()
berat = float(input("Masukkan berat barang (kg): "))

# Input pilihan asuransi
pilihan_asuransi = input("Apakah ingin menggunakan asuransi? (ya/tidak): ").lower()
asuransi = True if pilihan_asuransi == "ya" else False

# Panggil fungsi dan tampilkan hasil
hitung_ongkir(berat, kota, asuransi)
