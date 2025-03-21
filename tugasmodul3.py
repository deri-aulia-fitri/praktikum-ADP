#input dari pengguna
lambda_t = float (input("Masukkan nilai λt                     : "))
m = int(input("Masukkan nilai M                      : "))

#nilai konstanta e
e = 2.71828

n_faktorial = 1
for n in range (m + 1):
    p = (e ** (-lambda_t)) * ((lambda_t) ** n) / n_faktorial
    n_faktorial *= (n + 1)

#menampilkan hasil perhitungan untuk P(N(t)= n)
    print (f"nilai P(N(t) = {n})={p}")
