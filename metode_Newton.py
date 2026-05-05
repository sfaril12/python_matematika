from sympy import diff, sympify

# buatkan inputan untuk memasukan fungsi dan mencari turunannya sekaligus
print()
fungsifx = input("masukan fungsi f(x): ")
fungsi = sympify (fungsifx)
turunan = diff(fungsi, 'x')
print(f"fungsi turunan adalah: {turunan}")
print("-----------------------------------------------------")

# buatkan inputan untuk memasukan nilai x sembarang dan batas toleransinya
x1 = float(input("masukan nilai x1 : "))
toleransi = float(input("masukan nilai toleransi: "))
biterasi = int(input("masukan batas iterasi: "))
print()


# membuat deklarasi iterasi = 0 (artinya belum ada iterasi yang dilakukan)
iterasi = 0

# membuat format headers (tampilan tabel keterangan)
print(f"\n iterasi|       x1       |      f(x1)     |     f'(x1)     |      x2        |     |f(x2)|   ")
print("------------------------------------------------------------------------------------------------------")

# membuat function atau tempat khusus untuk dilakukannya sebuah operasi kompleks
def Newton(x1,iterasi,fungsi,turunan, biterasi,toleransi):
    
    # membuat sebuah perulangan searah 
    while True:
        
        # membuatkan sebuah operasi kompleks sesuai alur flowchart metode newton
        iterasi += 1 
        fx1 = fungsi.subs('x',x1)
        f1x1 = turunan.subs('x',x1)
        
        # membuat operasi untuk mencari x2 sekaligus hasil substitusinya
        x2 = x1 - (fx1 / f1x1)
        fx2 = fungsi.subs('x',x2)
        
        # membuat tampilan content(isi) untuk menampilkan kalkulasi perhitungan
        print(f"{iterasi:7} | {x1:>14.10f} | {fx1:>14.10f} | {f1x1:>14.10f} | {x2:>14.10f} | {abs(fx2):14.10f}")
        
        # membuat pengkondisian untuk  |f(x2) < toleransi
        if abs(fx2) < toleransi or iterasi == biterasi:
            break   # untuk menghentikan perulangan apabila kondisi ini terpenuhi
        else :
            x1 = x2
    return x2, iterasi # mengeluarkan beberapa variabel penting di dalam def untuk dipakai ke langkah selanjutnya

# membuat variabel baru untuk menampung variabel yang dikeluarkan  oleh def
hasil, jml_iterasi = Newton(x1,iterasi,fungsi,turunan, biterasi, toleransi)

# menampilkan hasil akhir
print()
print(f" jumlah iterasi : {jml_iterasi}")
print(f" hasil akhir nilai x2: {hasil}")
