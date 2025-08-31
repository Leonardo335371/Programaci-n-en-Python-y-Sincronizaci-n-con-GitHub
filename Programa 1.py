def buscar_valor(matriz, valor_buscar):
    # Recorre la matriz buscando el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor_buscar:
                return True, i, j  # Retorna encontrado y posición
    return False, -1, -1  # Retorna no encontrado

# Crear una matriz 3x3 con valores numéricos
matriz = [
    [4, 7, 2],
    [9, 1, 5],
    [3, 8, 6]
]

# Valor a buscar
valor_buscado = 8

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Buscar el valor
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
if encontrado:
    print(f"\nEl valor {valor_buscado} se encontró en la posición ({fila}, {columna})")
else:
    print(f"\nEl valor {valor_buscado} no se encontró en la matriz")