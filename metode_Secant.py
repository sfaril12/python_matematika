from sympy import sympify


# buatkan inputan untuk memasukan fungsi
print()
fungsi = input("masukan fungsi : ")
fungsifx = sympify(fungsi)
print ()
print("-------------------------------------------------")
print()

# buatkan inputan untuk memasukan nilai x0, x1 dan batas toleransinya
x0 = float(input("masukan nilai x0 : ")) 
x1 = float(input("masukan nilai x1 : "))
toleransi = float(input("masukan nilai toleransi: "))
biterasi = int(input("masukan batas iterasi: "))
print()

# membuat function atau tempat khusus untuk dilakukannya sebuah operasi kompleks
def secant(fungsifx, x0, x1, biterasi, toleransi):
    
    # membuat deklarasi iterasi = 0 (artinya belum ada iterasi yang dilakukan)
    iterasi = 0
    
    # membuat format headers (tampilan tabel keterangan)
    print("\niterasi |      x0       |      x1      |     f(x0)      |    f(x1)   |      x2      |     f(x2)    ")
    print("-------------------------------------------------------------------------------------------")
    
    # membuat sebuah perulangan searah 
    while True :
        
        # membuatkan sebuah operasi kompleks sesuai alur flowchart metode secant
        iterasi += 1
        fx0 = fungsifx.subs('x', x0)
        fx1 = fungsifx.subs('x', x1)
        
        # membuat operasi untuk mencari x2 sekaligus hasil substitusinya
        x2 = x1 - fx1 * (x1-x0)/(fx1-fx0)
        fx2 = fungsifx.subs('x', x2)
        
        # membuat tampilan content(isi) untuk menampilkan kalkulasi perhitungan
        print(f"{iterasi:7} | {x0:14.8f} | {x1:14.8f} | {fx0:14.8f} | {fx1:14.8f} | {x2:14.8f} | {abs(fx2):14.8f}")
        
        # membuat pengkondisian untuk  |f(x2) < toleransi
        if abs(fx2) < toleransi or iterasi == biterasi:
            break       # untuk menghentikan perulangan apabila kondisi ini terpenuhi
        else :
            x0 = x1
            x1 = x2
    return iterasi, x2  # mengeluarkan beberapa variabel penting di dalam def untuk dipakai ke langkah selanjutnya

# menampilkan hasil akhir
iterasion, hasil = secant(fungsifx, x0, x1, biterasi, toleransi)
print()
print(f"jumlah iterasi: {iterasion}")
print(f"hasil akhir x2  : {hasil}")
 
