def input_data():
    n = int(input("Masukkan jumlah praktikan: "))
    data = []
    for i in range(n):
        print(f"\nPraktikan ke-{i+1}")
        nama = input("Nama           : ")
        nim = input("NIM            : ")
        pretest = float(input("Nilai Pretest  : "))
        postest = float(input("Nilai Postest  : "))
        tugas = float(input("Nilai Tugas    : "))
        bonus = float(input("Nilai Bonus    : "))
        data.append([nama, nim, pretest, postest, tugas, bonus])
    return data
    
def hitung_rata2(data, kolom):
    total = 0
    for d in data:
        total += d[kolom]
    rata = total / len(data)
    return rata

def hitung_nilaiakhir(data):
    for x in data:
        nilai_akhir = 0.25 * x[2] + 0.25 * x[3] + 0.5 * x[4] + x[5]
        x.append(nilai_akhir)
def urutan_nilaiakhir(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][6] < data[j + 1][6]:  
                data[j], data[j + 1] = data[j + 1], data[j]
def beri_peringkat(data):
    i = 1
    for d in data:
        d.append(i)
        i += 1
def tampilkan_tabel(data):
    print("-" * 53)
    print(f"{"Nama":<14} | {"NIM":<8}  | {"Nilai Akhir"} | {"Peringkat"}|")
    print("-" * 53)
    for d in data:
        print(f"{d[0]:<15}|{d[1]:<10}| {d[6]:<12.2f}| {d[7]}        |   ")
data = input_data()

rata_pretest = hitung_rata2(data, 2)
rata_postest = hitung_rata2(data, 3)
rata_tugas = hitung_rata2(data, 4)

hitung_nilaiakhir(data)
urutan_nilaiakhir(data)
beri_peringkat(data)
tampilkan_tabel(data)

rata_akhir = hitung_rata2(data, 6)
print("-" * 53)
print(f"Rata-rata Akhir|           |{rata_akhir:.2f}       |          |  ")
print("-" * 53)
