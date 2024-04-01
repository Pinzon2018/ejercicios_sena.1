#63. Programa que permita llenar una matriz de 3 filas y 4 columnas y luego determine: a) La suma total de todos lo valores b) El valor promedio de todos los valores ingresados.

matrix = []

for rows in range(3):
    row = []
    for elements in range(4):
        row.append(int(input(f"Elemento de la fila {rows}: ")))
    matrix.append(row)

for row in matrix:
    print(row)

suma = 0

for rows in matrix:
    for elements in rows:
        suma += elements

print(f"La suma de la matriz es de: {suma}")

prom = suma/12

print(f"El promedio de la matriz es de: {prom}")