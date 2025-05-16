nomor_mahasiswa=[]
nama_mahasiswa=[]
nilai_mahasiswa =[]
while True :
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    print()
    pilihan =int(input("Inputkan pilihan : "))
    if pilihan == 1 :
        no = int(input("Nomor mahasiswa : "))
        nama = (input("Nama mahasiswa : "))
        nilai = float(input("Nilai mahasiswa : "))
        nomor_mahasiswa.append(no)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("Data berhasil ditambahkan")
        print()
    elif pilihan == 2:
        no = int(input("Masukan nomor mahasiswa yang ingin dihapus : "))
        if no in nomor_mahasiswa :
            index=nomor_mahasiswa.index(no)
            deleted_item = nomor_mahasiswa.pop(index)
            deleted_item = nama_mahasiswa.pop(index)
            deleted_item = nilai_mahasiswa.pop(index)
            print("Data berhasil dihapuskan")
        else :
            print("Nomor mahasiswa tidak valid ")
        print()
    elif pilihan == 3 :
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data.\n")
        else :
            gabungan = []
            for i in range(len(nomor_mahasiswa)):
                gabungan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))
            n = len(gabungan)
            batas = n
            while batas > 1 :
                for i in range(batas - 1) :
                    batas += 1
                    if gabungan[i][2] < gabungan[i+1][2]:
                        temp = gabungan
            for data in gabungan:
                print("NIM:", data[0], "Nama:", data[1], "Nilai:", data[2])
            print()
    elif pilihan == 4 :
        print("Terima kasih ")
        break
    else :
        print("Pilihan tidak valid, silahkan coba lagi")