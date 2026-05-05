def gauss_jordan_elimination():
    # Input ukuran matriks (jumlah variabel)
    n = int(input("Masukkan ukuran matriks (n x n): "))
    
    # Membuat list kosong untuk matriks (A | b)
    augmented_matrix = []
    
    # Input matriks koefisien A
    print(f"\nMasukkan matriks koefisien A ({n}x{n}):")
    for i in range(n):
        row = list(map(float, input(f"Baris {i+1} (pisahkan dengan spasi): ").split())) #input setiap baris, lalu ubah ke float
        
        # Validasi jumlah elemen
        if len(row) != n:
            print(f"Error: Harus memasukkan {n} elemen per baris")
            return
        augmented_matrix.append(row)
    
    # Input vektor konstanta b
    print(f"\nMasukkan vektor konstanta b ({n}x1):")
    b = list(map(float, input("Elemen (pisahkan dengan spasi): ").split()))
    
    # Validasi jumlah elemen  b
    if len(b) != n:
        print(f"Error: Harus memasukkan {n} elemen")
        return
    
    # Gabungkan matriks A dan vektor b
    for i in range(n):
        augmented_matrix[i].append(b[i])
    
    # Tampilkan sistem awal
    print("\n" + "="*50)
    print("SISTEM PERSAMAAN AWAL:")
    print_matrix(augmented_matrix)
    
    # Proses eliminasi Gauss-Jordan
    for col in range(n):
        # Pivoting
        max_row = col
        for r in range(col+1, n):
            if abs(augmented_matrix[r][col]) > abs(augmented_matrix[max_row][col]):
                max_row = r
        
        # Tukar baris jika diperlukan
        if max_row != col:
            augmented_matrix[col], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[col]
            print(f"\nLANGKAH {col+1}-1: PIVOTING")
            print(f"Baris {col+1} ditukar dengan baris {max_row+1}")
            print_matrix(augmented_matrix)
        
        # Normalisasi baris pivot
        pivot = augmented_matrix[col][col]
        
        # Jika pivot = 0, maka tidak bisa diselesaikan
        if pivot == 0:
            print("Matriks singular, tidak dapat diselesaikan")
            return
        
        # Membuat pivot menjadi 1
        for j in range(col, n+1):
            augmented_matrix[col][j] /= pivot
            
        print(f"\nLANGKAH {col+1}-2: NORMALISASI BARIS {col+1}")
        print(f"Baris {col+1} dibagi dengan {pivot:.4f}")
        print_matrix(augmented_matrix)
        
        # Eliminasi untuk semua baris (termasuk di atas pivot)
        for r in range(n):
            if r == col:  
                continue   # Lewati baris pivot
                
            factor = augmented_matrix[r][col]
            print(f"\nLANGKAH {col+1}-3: ELIMINASI BARIS {r+1}")
            print(f"Faktor = {factor:.4f} * Baris {col+1}")
            
            # Operasi baris elementer
            for c in range(col, n+1):
                augmented_matrix[r][c] -= factor * augmented_matrix[col][c]
            
            print_matrix(augmented_matrix)
    
    # Tampilkan solusi langsung dari kolom terakhir
    print("\n" + "="*50)
    print("HASIL SOLUSI:")
    for i in range(n):
        print(f"x_{i+1} = {augmented_matrix[i][n]:.4f}")
    print("="*50)

# Fungsi untuk menampilkan matriks augmented dengan format rapi
def print_matrix(matrix):
    n = len(matrix)    
    for i in range(n):
        row_str = "| "
        
        # Menampilkan matriks A
        for j in range(n):
            row_str += f"{matrix[i][j]:8.3f} "
        
        # Menampilkan kolom B
        row_str += f" | {matrix[i][n]:8.3f} |"
        print(row_str)
    print()


print("PROGRAM SOLVER SISTEM PERSAMAAN LINEAR")
print("METODE ELIMINASI GAUSS-JORDAN\n")
gauss_jordan_elimination()