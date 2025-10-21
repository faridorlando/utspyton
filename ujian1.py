# Program: Menghitung Total Setoran Mingguan Koperasi

print("=" * 40)
print("   PROGRAM HITUNG SETORAN MINGGUAN")
print("=" * 40)

# Input 3 setoran
a = int(input("Masukkan setoran minggu ke-1: "))
b = int(input("Masukkan setoran minggu ke-2: "))
c = int(input("Masukkan setoran minggu ke-3: "))

print("-" * 40)

# Validasi input
if a <= 0 or b <= 0 or c <= 0:
    print("❌ Input tidak valid. Semua setoran harus lebih dari 0.")
else:
    total = a + b + c
    print(f"Total setoran: Rp {total:,}")  # format ribuan
    
    # Klasifikasi total
    if total < 300_000:
        print("Keterangan: 🔹 Rendah")
    elif total < 600_000:
        print("Keterangan: 🔸 Sedang")
    else:
        print("Keterangan: 🔺 Tinggi")

print("=" * 40)
print("Terima kasih telah menggunakan program ini!")
