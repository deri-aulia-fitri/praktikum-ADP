#Daftar Menu Paket Makanan
print("                          WELCOME TO GOLDEN WINGS                                     ")
print("-----------------------------------------------=--------------------------------")
print("                             LIST PAKET MAKANAN                                            ")
print("--------------------------------------------------------------------------------")
print("PAKET                               MENU                               HARGA                                       ")
print("Biasa Aja Sih               Nasi Goreng, Es Teh                      Rp. 20.000                ")
print("Biasa Aja                   Ayam Bakar,  Es Jeruk                    Rp. 35.000                ")
print("Biasa                       Ayam Saos Padang, Es jeruk               Rp. 40.000              ")
print("Luar Biasa                  Ayam Lada Hitam, Lemon Tea               Rp. 45.000  ")
print("luar Biasa Sekali           Ayam Pedas 1 ekor, Lemon Tea             Rp. 110.000 ")
print("--------------------------------------------------------------------------------")

#Masukkan Detail Pemesanan 
# print("                            DETAIL PEMESANAN ANDA                                 ") 
nama = input("Nama:")
alamat = input("Alamat:")
nomor_telepon = int(input("nomor_telepon:"))
pesanan = input("Paket yang ingin dipesan:")
jumlah = int(input("jumlah paket yang ingin dipesan:"))

#Harga Tiap Paket
biasa_aja_sih     = 20000
biasa_aja         = 35000
biasa             = 40000
luar_biasa        = 45000
luar_biasa_sekali = 110000

#menentukan pesanan dan harga
if pesanan == "biasa aja sih":
    p = ("Nasi Goreng, Es Teh")
    harga =jumlah*biasa_aja_sih
elif pesanan == "biasa aja":
    p = ("Ayam Bakar, Es Jeruk")
    harga = jumlah*biasa_aja
elif pesanan == "biasa":
    p = ("Ayam Saos Padang, Es jeruk")
    harga = jumlah*biasa
elif pesanan == "luar biasa":
    p = ("Ayam Lada Hitam, Lemon Tea")
    harga = jumlah*luar_biasa
else :
    p = ("Ayam Pedas 1 ekor, Lemon Tea")
    harga = jumlah*luar_biasa_sekali



#menentukan pajak
pajak = harga*(10/100)

#menetukan harga setelah pajak
harga_total = harga + pajak

#menetukan biaya pengiriman
if harga < 150000 :
    biaya_pengiriman = 25000
else :
    biaya_pengiriman = 0

#menentukan total biaya
total_biaya = biaya_pengiriman + harga_total  
print()
print ()

#menampilkan struk pemesanan
print("                              ****STRUK PEMESANAN****                 ")
print("Nama                                                         :", nama)
print("alamat                                                       :", alamat)
print("nomor telepon                                                :", nomor_telepon )
print("paket yang ingin dipesan                                     :", pesanan)
print("jumlah yang dipesan                                          :", jumlah )
print("harga sebelum pajak                                          :", harga)
print("pajak                                                        :", pajak )
print("harga setelah pajak                                          :", harga_total)
print("biaya pengiriman                                             :", biaya_pengiriman)
print("total akhir                                                  :", total_biaya)




