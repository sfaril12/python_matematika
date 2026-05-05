def back_substitution(A, b):
    n = len(b) # Jumlah variabel / ukuran matriks
    x = [0] * n # Inisiasi solusi x dengan nilai awal 0
    
    # Proses back substitusion
    for i in range(n-1, -1, -1): # Looping
        total = 0.0 # Menyimpan jumlah A[i][j] * x[j]
        
        # Hitung kontribusi variabel yang sudah diketahui
        for j in range(i+1, n):
            total += A[i][j] * x[j]
        
        # Cek kasus khusus (pivot = 0)
        if abs(A[i][i]) < 1e-10: # Kondisi jika elemen diagonal sangat kecil 
            if abs(b[i] - total) < 1e-10:
                raise ValueError(f"Sistem memiliki solusi tak hingga (variabel bebas) pada baris {i+1}")
            else:
                raise ValueError(f"Sistem tidak konsisten pada baris {i+1}")
        
        # Rumus back substitusion
        x[i] = (b[i] - total) / A[i][i]
    
    return x

def main():
    print("PROGRAM BACK SUBSTITUTION UNTUK MATRIKS SEGITIGA ATAS")
    n = int(input("Masukkan ukuran matriks (n): ")) # Input ukuran matriks
    
    print("\nMasukkan elemen matriks A (per baris):") # Input matriks A 
    A = []
    for i in range(n):
        while True:
            row = input(f"Baris {i+1}: ").split() # Input satu baris matriks
            
            # Validasi jumlah elemen
            if len(row) != n:
                print(f"Error: Harus memasukkan {n} elemen")
                continue
            try:
                row = [float(x) for x in row] # Konversi ke float
                A.append(row)
                break
            except ValueError:
                print("Error: Masukkan harus berupa angka")
    
    print("\nMasukkan elemen vektor b:") # Input vektor b
    b = []
    while True:
        b_input = input().split()
        
        # Validasi jumlah elemen
        if len(b_input) != n:
            print(f"Error: Harus memasukkan {n} elemen")
            continue
        try:
            b = [float(x) for x in b_input]
            break
        except ValueError:
            print("Error: Masukkan harus berupa angka")
    
    # Proses dan output kodingan
    try:
        solution = back_substitution(A, b) # Panggil fungsi back subtitution
        print("\nSolusi sistem persamaan:")
        for i, val in enumerate(solution):
            print(f"x_{i+1} = {val:.4f}")  
    except ValueError as e:  # tangani error tak hingga / tidak konsisten
        print(f"\nError: {e}")
main()