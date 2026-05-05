def gauss_elimination():
    # Input ukuran matriks
    n = int(input("Masukkan ukuran matriks (n x n): "))
    
    # Inisialisasi matriks augmented
    augmented_matrix = []
    
    # Input matriks koefisien A
    print(f"\nMasukkan matriks koefisien A ({n}x{n}):")
    for i in range(n):
        row = list(map(float, input(f"Baris {i+1} (pisahkan dengan spasi): ").split()))
        if len(row) != n:
            print(f"Error: Harus memasukkan {n} elemen per baris")
            return
        augmented_matrix.append(row)
    
    # Input vektor konstanta b
    print(f"\nMasukkan vektor konstanta b ({n}x1):")
    b = list(map(float, input("Elemen (pisahkan dengan spasi): ").split()))
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
    
    # Proses eliminasi Gauss
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
        
        # Eliminasi
        for r in range(col+1, n):
            factor = augmented_matrix[r][col] / augmented_matrix[col][col]
            print(f"\nLANGKAH {col+1}-2: ELIMINASI BARIS {r+1}")
            print(f"Faktor = {augmented_matrix[r][col]} / {augmented_matrix[col][col]} = {factor:.4f}")
            
            for c in range(col, n+1):
                augmented_matrix[r][c] -= factor * augmented_matrix[col][c]
            
            print_matrix(augmented_matrix)
    
    # Substitusi mundur
    solutions = [0] * n
    for i in range(n-1, -1, -1):
        solutions[i] = augmented_matrix[i][n]
        for j in range(i+1, n):
            solutions[i] -= augmented_matrix[i][j] * solutions[j]
        solutions[i] /= augmented_matrix[i][i]
    
    # Tampilkan solusi
    print("\n" + "="*50)
    print("HASIL SOLUSI:")
    for i in range(n):
        print(f"x_{i+1} = {solutions[i]:.4f}")
    print("="*50)

def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        row_str = "| "
        for j in range(n):
            row_str += f"{matrix[i][j]:8.3f} "
        row_str += f" | {matrix[i][n]:8.3f} |"
        print(row_str)
    print()


print("PROGRAM SOLVER SISTEM PERSAMAAN LINEAR")
print("METODE ELIMINASI GAUSS\n")
gauss_elimination()