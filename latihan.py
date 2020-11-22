print("Membuat list dengan 5 element")
list_saya = [1, 2, 3, 4, 5] # menurut index mulai dari nol
print(list_saya)

print("Menampilakn element ke 3")
print(list_saya[2])

print("Ambil nilai element ke 2 sampai element ke 4")
print(list_saya[1:4])

print("Ambil element terakhir")
print(list_saya[-1])

print("ubah element ke 4 dengan nilai lainnya")
list_saya[3] = 7
print(list_saya)

print("Ubah element ke 4 sampai dengan elemen terakhir")
list_saya[3:5] = [27, 77]
print(list_saya)

print("Ambil 2 bagian dari list pertama (A) dan jadikan list ke dua (B)")
data_saya = list_saya[0:2]
print(data_saya)

print("Tambah list B dengan nilai string")
data_saya.append("SN Fauziah")
print(data_saya)

print("Tambah list B dengan 3 nilai")
data_saya.extend(["Uci", 27, 99])
print(data_saya)

print("gabungkan list B dengan list A")
gabungan = data_saya + list_saya
print(gabungan)