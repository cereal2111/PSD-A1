# Mendefinisikan fungsi untuk menghitung rata-rata nilai
def hitung_rata_nilai(nilai_ujian):
    return sum(nilai_ujian) / len(nilai_ujian)

# Meminta input dari pengguna untuk jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
data_mahasiswa = []  # Inisialisasi list untuk menyimpan data mahasiswa

# Loop untuk mengumpulkan data dari setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nData mahasiswa ke-{i+1}:")  # Menampilkan nomor mahasiswa yang sedang diinput
    nama = input("Masukkan nama mahasiswa: ")  # Meminta nama mahasiswa
    nim = input("Masukkan NIM mahasiswa: ")  # Meminta NIM mahasiswa
    jumlah_nilai = int(input(f"Masukkan jumlah nilai ujian mahasiswa: "))  # Meminta jumlah nilai ujian
    nilai_ujian = []  # Inisialisasi list untuk menyimpan nilai ujian
    # Loop untuk mengumpulkan nilai ujian dari mahasiswa
    for j in range(jumlah_nilai):
        nilai = float(input(f"Masukkan nilai ujian ke-{j+1}: "))  # Meminta nilai ujian
        nilai_ujian.append(nilai)  # Menambahkan nilai ujian ke dalam list
    data_mahasiswa.append((nama, nim, nilai_ujian))  # Menambahkan data mahasiswa ke dalam list data_mahasiswa

print("\nOUTPUT\n")

# Loop untuk menampilkan output untuk setiap mahasiswa
for data in data_mahasiswa:
    nama, nim, nilai_ujian = data  # Mendapatkan data mahasiswa dari tuple
    rata_nilai = hitung_rata_nilai(nilai_ujian)  # Menghitung rata-rata nilai ujian
    # Menampilkan informasi mahasiswa dan rata-rata nilai ujian
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Rata-rata Nilai Ujian: {rata_nilai}\n")
