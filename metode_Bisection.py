from sympy import sympify

# membuatkan inputan agar bisa memasukkan fungsi
print()
fungsi = input("masukan fungsi: ")    # untuk imput fungsi cth : x**2 + x + 2 (x**2 artinya x pangkat 2)
fo = sympify(fungsi)   
toleransi = float(input("masukan nilai toleransi: ")) #  mendeklarasikan nilai toleransi = 0,000001 (nilai default toleransi pada metode bisection)
biterasi = int(input("masukan batas iterasi: "))
print("--------------------------------------------------------")

# membuatkan inputan agar bisa memasukan nilai batas bawah dan batas atas serta kekongkretannya  dengan fungsi
while True:      
        a = float(input("masukan nilai batas bawah  (x-n): "))     
        b = float(input("masukan nilai batas atas (x-n+1): "))     
        print("--------------------------------------------------------")
        # mensubtitusikan dan menampilkan nilai xn dan xn+1 ke fungsi 
        fa = fo.subs('x',a)  
        fb = fo.subs('x',b)  
        print(f"nilai f(x-n): {fa:.4f}")
        print(f"nilai f(x-n+1): {fb:.4f}")
        print()
        
        fkondisi1 =(fa * fb)   # membuat kondisi True False agar bisa lanjut ke iterasi

        # membuat proses pengeksekusian kondisi agar mendapatkan hasil yang bisa di teruskan di iterasi
        print("cek f(x-n) x f(x-n+1) < 0")
        print("--------------------------------------------------------")
        if fa * fb < 0 : #syarat kondisi yang pertama
            print(f"hasil dari f(x-n) x f(x-n+1) : {fa:.4f} x {fb:.4f} = {fkondisi1:.4f} ---> hasil memenuhi")
            print(f"lanjut ke uji coba iterasi")
            break   # menghentikan perulangan apabila fa x fb < 0 terpenuhi
        else:
            print(f"hasil dari f(x-n) x f(x-n+1) : {fa:.4f} x {fb:.4f} = {fkondisi1:.4f} ---> hasil tidak memmenuhi")
            print("masukan ulang nilai batas bawah(x-n) dan batas atas(x-n+1)")
            print()

# membuatkan uji coba iterasi 
def Bisection(a,b,fa,fb,fo,biterasi,toleransi):
    iterasi=0
    
    # membuatkan tampilan headers(keterangan) untuk tabel
    print("\nIterasi |       xn       |      xn+1      |      f(xn)     |    f(xn+1)     |       xt       |   |f(xt)|       ")
    print("-----------------------------------------------------------------------------------------------------------------")
    
    # membuatkan alur pengkondisian kedua 
    while True :
        iterasi += 1
        xt = (a+b)/2 # rumus mencari nilai tengah metode regulafalsi
        fc = fo.subs('x',xt)
        
        # membuat tampilan contents(isi) uji coba yang diseleksi
        print(f"{iterasi:7} | {a:>14.8f} | {b:>14.8f} | {fa:>14.8f} | {fb:>14.8f} | {xt:>14.8f} | {abs(fc):>14.8f}")
    
        # membuatkan proses pengeksekusian kedua sampai f(xt) < nilai epsilon(toleransi)
        if abs(fc) < toleransi or iterasi == biterasi : # membuat syarat kondisi
            break
        
        # membuatkan kondisi untuk terjadinya proses pertukaran posisi berdasarkan nilai 0
        if fc * fa < 0 : #kondisi pertama 
            b = float(xt)
            fb = float(fc)
        else:            #kondisi kedua
            a = float(xt)
            fa = float(fc)
        
    return xt, iterasi  # mengeluarkan beberapa variabel penting di dalam def untuk dipakai ke langkah selanjutnya

# memanggil function def yang menjalankan iterasi
hasil_akhir , iterasi_akhir,  = Bisection(a,b,fa,fb,fo,biterasi,toleransi)

# menampilkan hasil akhir
print()
print(f"jumlah iterasi: {iterasi_akhir}")
print(f"hasil akhir nilai xt: {hasil_akhir}")