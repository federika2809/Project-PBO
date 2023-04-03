#Contoh Kode Program Fungsional Programming
angka = [1, 2, 3, 4, 5]

#Menghitung kuadrat dari setiap angka pada list angka
bilangan_kuadrat = map(lambda x: x**2, angka)

# Memilih angka genap pada list angka
bilangan_genap = filter(lambda x: x%2 == 0, angka)

print(list(bilangan_kuadrat)) 
print(list(bilangan_genap))
print ("\n")



#Contoh Kode Program OOP
class Mahasiswa:
    def __init__(self, nama, npm, prodi ):
        self.nama  = nama
        self.npm   = npm
        self.prodi = prodi
    
    def data_mahasiswa(self):
        print("Nama : ", self.nama)
        print("NPM  : ", self.npm)
        print("Prodi: ", self.prodi)

# Membuat objek dari class Mahasiswa
mahasiswa1 = Mahasiswa("Federika Butar Butar", 30, "Informatika")
mahasiswa2 = Mahasiswa("Wahyu Ozorah Manurung",60, "Informatika")

# Memanggil method tampilkan_data() pada objek mhs1 dan mhs2
mahasiswa1.data_mahasiswa()
print ("\n")
mahasiswa2.data_mahasiswa()
