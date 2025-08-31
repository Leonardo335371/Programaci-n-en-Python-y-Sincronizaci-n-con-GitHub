def bubble_sort_row(matrix, row_index):
    # Obtener la fila a ordenar
    row = matrix[row_index]
    n = len(row)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if row[j] > row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]

    # Actualizar la fila en la matriz
    matrix[row_index] = row


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


# Crear matriz 3x3
matrix = [
    [9, 2, 5],
    [1, 8, 3],
    [7, 4, 6]
]

# Mostrar matriz original
print("Matriz original:")
print_matrix(matrix)

# Ordenar la fila 1 (índice 0) en orden ascendente
bubble_sort_row(matrix, 1)

# Mostrar matriz con la fila ordenada
print("Matriz con la fila 1 ordenada:")
print_matrix(matrix)