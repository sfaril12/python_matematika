from sympy import symbols, sympify
import sympy

# Mendefenisikan variabel simbolik x
x = symbols('x')

print("\n=== PROGRAM DERET TAYLOR ===")

# Memasukkan fungsi daa bentuk string (contoh: sin(x), exp(x), x**2
fungsi = input("Masukkan fungsi (dalam variabel x): ")
fo = sympify(fungsi) # Mengubah string menjadi ekspresi matematika SymPy

# Input parameter taylor
a = float(input("Masukkan titik pusat (a): ")) # Titik pusat (a), tempat deret taylor dikembangkan
n = int(input("Masukkan orde deret Taylor (n): ")) # Orde deret taylor  (jumlah suku pendekatan)

# Proses deret taylor
# Menghitung deret taylor dari fungsi di sekitar titik a sampai orde ke-n
# Series() menghasilkan ekspansi + 0(x^n), remove() menghilangkan 0(...)
taylor_series = fo.series(x, a, n).removeO()

# Output hasil deret
print("\n=== HASIL DERET TAYLOR ===")
print(f"Fungsi: {fungsi}")
print(f"Titik pusat: x = {a}")
print(f"Orde: {n}")
print("\nDeret Taylor:")
sympy.pprint(taylor_series) # Menampilkan bentuk matematika yang lebih rapi

# Konversi ke fungsi numerik
taylor_func = sympy.lambdify(x, taylor_series)

# Evaluasi hasil
print("\nEvaluasi:")

# Titik yang ingin diuji (x)
x_eval = float(input("Masukkan titik evaluasi (x): "))
hasil_taylor = taylor_func(x_eval) # Hitung nilai aproksimasi taylor
hasil_eksak = fo.subs(x, x_eval) #  Hitung nilai eksak dari fungsi asli
error = abs(hasil_eksak - hasil_taylor) # Hitung error absolut

# Output evaluasi
print(f"\nHasil aproksimasi Taylor: {hasil_taylor:.8f}")
print(f"Nilai eksak: {hasil_eksak:.8f}")
print(f"Error: {error:.8f}")