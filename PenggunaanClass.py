from os import system
import sys
dict = {}

class dataMahasiswa :
    def judul():
        print('==================================')
        print('|     Daftar Nilai Mahasiswa     |')
        print('==================================')


    def menu(self):
        system('cls')
        print('=====================================')
        print('Input Data Nilai Mahasiswa'.center(40))
        print('=====================================')
        print('|    1. Tambah Data                 |')
        print('|    2. Tampilkan Data Mahasiswa    |')
        print('|    3. Ubah Data Mahasiswa         |')
        print('|    4. Hapus Data Mahasiswa        |')
        print('|    5. Selesai                     |')
        print('=====================================')
        choose = input('Pilih Menu  : ')
        if choose == '1':
            mahasiswa.tambah()
            mahasiswa.ulang()
        elif choose == '2':
            mahasiswa.tampilkan()
            mahasiswa.ulang()
        elif choose == '3':
            mahasiswa.ubah()
            mahasiswa.ulang()
        elif choose == '4':
            mahasiswa.hapus()
            mahasiswa.ulang()
        elif choose == '5':
            mahasiswa.selesai()
        else:
            print('Menu Tidak Ada')
            mahasiswa.ulang()
            
    def ulang(self):
        ulang = input('ingin ulang Y/T : ')
        if(ulang=='y' or ulang=='Y'):
            mahasiswa.menu()
        elif(ulang=='t' or ulang=='T'):
            quit()
        else:
            print('Pilih Y/T')
            mahasiswa.ulang()

    def tambah(self):
        print("Tambah Data")
        nama = input("Masukan Nama        : ")
        nim = int(input("Masukan NIM         : "))
        tugas = int(input("Nilai Tugas         : "))
        uts = int(input("Nilai UTS           : "))
        uas = int(input("Nilai UAS           : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        dict[nama] = nim, tugas, uts, uas, hasil


    def tampilkan(self):
        if dict.items():
            print("Daftar Nilai")
            print("="*73)
            print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
            print("="*73)
            i = 0 
            for y in dict.items():
                i += 1
                print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7} |".format
                (y[0][:50], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))   
                print("="*73)     
        else:
            print("Daftar Nilai")
            print("="*73)
            print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
            print("="*73)
            print("|                           TIDAK ADA DATA                               |") 
            print("="*73)

    def ubah(self):
        print("Ubah Data")
        nama = input("Masukan Nama            : ")
        if nama in dict.keys():
            nim = int(input("Masukan NIM         : "))
            tugas = int(input("Nilai Tugas         : "))
            uts = int(input("Nilai UTS           : "))
            uas = int(input("Nilai UAS           : "))
            hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35                
            dict[nama] = nim, tugas, uts, uas, hasil
        else:
            print("Nama {0} Tidak di Tentukan".format(nama))

    def hapus(self):
        print("Hapus Data")
        nama = input("Masukan Nama      : ")    
        if nama in dict.keys():
            del dict[nama]
        else:
            print("Nama {0} Tidak di Temukan".format(nama))

    

    def selesai(self):
            print("Terima Kasih")
            sys.exit()

mahasiswa = dataMahasiswa()
mahasiswa.menu()
mahasiswa.tambah()
mahasiswa.tampilkan()
mahasiswa.ubah()
mahasiswa.hapus()
mahasiswa.selesai()

