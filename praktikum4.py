print("===================")
print("Nama     : Siti Nur Fauziah")
print("NIM      : 312010032")
print("Kelas    : TI.20.B.1")
print("===================")

# Buat program sederhana untuk menambahkan data kedalam sehuah lits dengan rincian sebagai bberikut :
# Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
#Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
# Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
# Buat flowchart dan penjelasan programnya pada README.md.
# Commit dan push repository ke github.

nilai = []
stop = False

# Mengisi Nilai
while not stop:
    nama = input("Nama : ")
    nim  = input("NIM : ")
    tugas = input("Nilai Tugas : ")
    uts = input("Nilai UTS : ")
    uas = input("Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    nilai.append([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/n) : ")
    if (tanya == "n"):
        stop = True

    # Cetak Semua Nilai

print("****")
no = 0
x = PrettyTable()
for isi in nilai:
    no += 1
    x.field_names = (no, isi[0], isi[1], isi[2], isi[3], isi[4], isi[5])
    print(x)