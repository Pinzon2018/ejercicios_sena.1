# #52. Programa que permita solicitar 15 nombres, almacenarlos en un vector y luego los muestre en el orden ingresado.

personas = 15
i = 0
lista = []

while i<personas:
    nom = input("Cual es su nombre: ")
    i += 1
    lista.append(nom)
print(lista)