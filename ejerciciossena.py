#1. Programa que permita sumar 2 números.

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

suma = num1+num2

print(f"El resultado de la suma es: {suma}")

#2. Programa que permita multiplicar 3 números.

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

mult = num1*num2*num3

print(f"El resultado de la multiplicacion es: {mult}")

#3. Programa para calcular la distancia recorrida en un movimiento rectilíneo.  Recuerde que  X = V*T.

v = float(input("Digite la velocidad: "))
t = float(input("Digite el tiempo: "))

x = v*t

print(f"La distacia recorrida es de: {x}")

#4. Programa que permita calcular la edad de una persona conociendo el año actual y su año de su nacimiento.  

añoac = int(input("Año actual: "))
añona = int(input("Año de nacimiento: "))

edad = añoac-añona

print (f"Tu edad es de: {edad}")

#5. Programa para calcular el 20% de cualquier número de entrada.

num = int(input("Digite un numero: "))

print(num*0.20)

#6. Programa que permita calcular el 30%, el 60% y el 90% de un número cualquiera.    

num = int(input("Digite un numero: "))

print(num*0.30)
print(num*0.60)
print(num*0.90)

#7. Programa para calcular el área de un cuadrado.

l = float(input("Valor de los lados del cuadrado: "))

a = l**2

print(f"El area del cuadrado es {a}")

#8. Programa que permita ingresar 5 numeros y calcular el promedio.

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))
num4 = int(input("Digite un numero: "))
num5 = int(input("Digite un numero: "))

prom = (num1+num2+num3+num4+num5)/5

print(f"El promedio es {prom}")  

#9. Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.   

cantidad = int(input("Cuantos productos compro: "))
valorunit = float(input("De cuanto es el valor unitario: "))

iva = valorunit*0.16

total = valorunit+iva

print(f"El total es {total}")

#10. Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

sal_dia = 43333

dias_trab = int(input("Cuantos dias trabajo: "))

sal_sindesc = dias_trab*sal_dia

sal_pen = sal_sindesc*0.10

sal_salu = sal_sindesc*0.15

total_sal = sal_sindesc-sal_pen-sal_salu

print(f"El total del salario es de: {total_sal}")

#11. Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento.

añoac = int(input("Año actual: "))
añona = int(input("Año de nacimiento: "))

edad = añoac-añona

print (f"Tu edad es de: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#12. Programa para determinar si un número cualquiera ingresado por el usuario es o no positivo. 

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: ")) 

if num1 > 0 and num2 > 0:
    print("Los dos son positivos")
elif num1 < 0 and num2 > 0:
    print(f"El numero {num1} es negativo y el numero {num2} es positivo")
elif num1 > 0 and num2 < 0:
    print(f"El numero {num2} es negativo y el numero {num1} es positivo")
else:
    print("Los dos son negativos")

#13. Programa para determinar cuál es mayor entre 2 números cualquiera ingresados por el usuario.

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
else:
    print(f"El numero {num2} es mayor que {num1}")


#14. Programa para saber si un estudiante del Enrique Olaya Herrera requiere refrigerio. Por disposición de la secretaria de Educación requieren refrigerio los estudiantes de grado sexto hacia abajo.

grado = int(input("Que grado esta cursando: "))

if grado <= 6:
    print ("¡Tienes refrigerio!")
else:
    print ("No tienes refrigerio")

#15. Programa para determinar la mitad de un número ingresado por el usuario es mayor o menor de 100.

num = int(input("Ingresa un numero: "))

num_d = num/2

if num_d >= 100:
    print(f"El numero {num_d} es mayor a 100")
else:
    print(f"El numero {num_d} no es mayor de 100")

#16. Programa en el cual se ingresen 2 números y luego realice las siguientes operaciones: a) Si los números son iguales restarlos b) Si los números son diferentes sumarlos. 

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 == num2:
    print(num1-num2)
else: 
    print(num1+num2)

#17. Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia.   

cod = int(input("Digite su codigo de estudiante: "))
nom = input("Digite su numbre: ")
mat = input("Digite la materia: ")

not1 = float(input("Digite la primera nota: "))
not2 = float(input("Digite la segunda nota: "))
not3 = float(input("Digite la tercera nota: "))

prom = (not1+not2+not3)/3

if prom >= 4.0:
    print(nom)
    print(cod)
    print(mat)
    print("¡Aprobo!")
else:
    print(nom)
    print(cod)
    print(mat)
    print("No aprobo")

#18. Programa para determinar cuánto pagara una persona por una compra de la cual se sabe la cantidad de artículos y el valor unitario. Se debe tener en cuenta que el almacén hace un 20% de descuento cuando la compra supera $100000. 

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 100000:
    print("El valor total con descuento es de")
    desc = prod_f*0.20
    print(prod_f-desc)
else:
    print("No tiene descuento")

#19. Programa que permita determinar el total a pagar por una compra de la cual se sabe el valor unitario y la cantidad. Se debe tener en cuenta que se realiza un descuento del 15% por compra inferiores a $20000 y del 35% por compras mayores o iguales a $20000.  

cant_prod = int(input("Cuantos productos adquirio: "))
val_un = int(input("Cuanto es el valor unitario: "))    

total = cant_prod*val_un

if total >= 20000:
    desc = total*0.35
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")
elif total < 20000: 
    desc = total*0.15
    total_f = total-desc
    print(f"El valor con descuento: {total_f}")

#20. Programa para determinar si un número cualquiera ingresado por el usuario es par o impar.(Usar operación Modulo).

num = int(input("Digite un numero: "))

if num % 2 == 0: 
    print ("El numero es par")
elif num % 2 != 0:
    print ("El numero es impar")

#21. Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”.

dia1 = int(input("Temperatura del dia 1: "))
dia2 = int(input("Temperatura del dia 2: "))
dia3 = int(input("Temperatura del dia 3: "))
dia4 = int(input("Temperatura del dia 4: "))
dia5 = int(input("Temperatura del dia 5: "))
dia6 = int(input("Temperatura del dia 6: "))
dia7 = int(input("Temperatura del dia 7: "))

dia_prom = (dia1+dia2+dia3+dia4+dia5+dia6+dia7)/7

if dia_prom > 35:
    print("Que semana tan calurosa")
    print(f"El clima promedio fue de {dia_prom:.2f}°")
elif dia_prom >= 15 and dia_prom <= 35:
    print("Que clima tan delicioso")
    print(f"El clima promedio fue de {dia_prom:.2f}°")
elif dia_prom < 15: 
    print("Que semana tan fria")
    print(f"El clima promedio fue de {dia_prom:.2f}°")

#22. Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: a) Por compras entre 10000 y 20000 el 10% b) Por compras entre 20001 y 50000 el 30% c) Por compras superiores a 50000 el 50%.

prod = int(input("Cantidad de articulos: "))
val_un = float(input("Valor unitario: "))

prod_f = prod*val_un

if prod_f >= 10000 and prod_f <= 20000:
    desc = prod_f*0.10
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 10% {total_f}")
elif prod_f >= 20001 and prod_f <= 50000:
    desc = prod_f*0.30
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 30% {total_f}")
elif prod_f > 50000:
    desc = prod_f*0.50
    total_f = prod_f-desc
    print(f"El valor final con el descuento del 50% {total_f}")
else:
    print("No tiene descuento")

# 23. Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: a) La edad debe ser menor o igual a 18 años b) La estatura debe ser mayor a 180 cm c) El peso debe ser menor o igual a 80 kg.

edad = int(input("Cual es su edad: "))
estatura = int(input("Cual es su estatura: "))
peso = int(input("Cuanto pesas: "))  

if edad <= 18 and estatura >= 180 and peso <= 80:
    print("¡Aceptado en el equipo de baloncesto!")
else:
    print("No fuiste aceptado")

#24. Programa que permita determinar si una letra es o no vocal.

letra = input("Digite un caracter: ").lower()

if letra == 'a':
    print("Es una vocal")
elif letra == 'e':
    print("Es una vocal")
elif letra == 'i':
    print("Es una vocal")
elif letra == 'o':
    print("Es una vocal")
elif letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")

#25. Programa que permita realizar los siguientes requerimientos: 1. Calcular distancia recorrida 2. Calcular tiempo 3. Calcular velocidad.

print("\t.:Menu:.")
print("1. Calcular la diatancia recorrida")
print("2. Calcular tiempo")
print("3. Calcular velocidad")
n = int(input("Eliga una opción: "))

if n == 1:
    v = float(input("Cual es la velocidad: "))
    t = float(input("Cual fue el tiempo: "))
    d = v*t
    print(f"La distancia fue {d}")
elif n == 2:
    d = float(input("Cual es la distancia: "))
    v = float(input("Cual es la velocidad: "))
    t = d/v
    print(f"El tiempo es de {t}")
elif n == 3:
    d = float(input("Cual es la distancia: "))
    t = float(input("Cual fue el tiempo: "))
    v = d/t
    print(f"La velocidad es de {v}")
else: 
    print("Error")

#26. Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú: 1. Determinar si es positivo o negativo 2. Determinar si es par o impar. El programa debe realizar las operaciones que el usuario seleccione del menú.

num = int(input("Digite un numero: "))

print("\t.:MENU:.")
print("1. Determinar si es positivo o negativo.")
print("2. Determinar si es par o impar.")

n = int(input("Elija una opción: "))

if n == 1:
    if num > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
elif n == 2:
    if num % 2 == 0:
        print("El numero es par")
    else: 
        print("El numero es impar")

#27. Programa que muestre un menú que tenga las siguientes opciones: 1. Pasa o no la materia? 2. Es mayor o menor de edad? Caso 1: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa. Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

print("\t.:MENU:.")
print("1. Pasa o no la materia")
print("2. Es mayor o menor de edad")

n = int(input("Eliga una opción: "))

if n == 1:
    nota1 = float(input("Digite la primera nota: "))
    nota2 = float(input("Digite la segunda nota: "))
    nota3 = float(input("Digite la tercera nota: "))
    prom = (nota1+nota2+nota3)/3
    if prom >= 3.0:
        print("¡Paso la materia!")
    else:
        print("No pasas la materia")
elif n == 2:
    año_ac = int(input("Año actual: "))
    año_na = int(input("Año de nacimiento: "))
    edad = año_ac-año_na
    if edad >= 18:
        print("Eres mayor de edad")
    else: 
        print("Eres menor de edad")
else:
    print("Error")

#28. Programa que permita ver los números naturales comprendidos entre 0 y 1000

for i in range(1001):
    print(i)

#29. Programa que imprima los pares de entre 0 y 200

for i in range(0, 201):
    if i%2 == 0:
        print(i)

#30. Programa que imprima los números impares entre 201 y 499

for i in range(201, 500):
    if i%2 != 0:
        print(i)

#31. Programa que permita determinar cuántos estudiantes son mayores de edad en un grupo de 20 estudiantes.

mayores = 0

for i in range(0, 20):
    edad = int(input("Cual es su edad: "))
    if edad >= 18:
        mayores+=1
print(f"Los estudiantes mayores de edad son {mayores}")

#32. Programa  que  permita  determinar  cuántos  hombres  y  mujeres  hay  en  un  curso  de  25 estudiantes.  

mujeres = 0
hombre = 0

for i in range(0,25):
    print("\t H o M")
    p = input("Hombre o Mujer: ").upper()
    if p == 'H':
        hombre+=1
    elif p == 'M':
        mujeres+=1
    else:
        print("Error")
print(f"La candidad de mujeres son {mujeres}")
print(f"La candidad de hombres son {hombre}")

#33. Programa para calcular la edad promedio de un grupo de 15 estudiantes.

lista = []

for i in range(0,15):
    edad = int(input("Cual es tu edad:"))
    lista.append(edad)
print(lista)

suma = sum(lista)

prom = suma/15

print(f"La edad promedio es de {prom}")

#34.  Programa que permita calcular la estatura promedio de un grupo de 18 estudiantes y luego tomar las siguientes decisiones: a) Si la estatura promedio es menor a 140 cm imprimir un mensaje que diga “Estudiantes muy bajos”. b) Si la estatura promedio se encuentra entre 140 y 170 cm imprimir “Estudiantes de estatura normal”. c) Si la estatura promedio es mayor de 170 cm imprimir “Estudiantes muy altos”. 

lista = []

for i in range(0,18):
    estat = int(input("Cual es su estatura en cm: "))
    lista.append(estat)
print(lista)

suma = sum(lista)
prom = suma/18

if prom < 140:
    print("Estudiantes muy bajos")
elif prom >= 140 and prom <= 170:
    print("Estudiantes de estatura normal")
elif prom > 170:
    print("Estudiantes muy altos")

#35.Programa que muestre en pantalla los múltiplos de 3 teniendo como límite el número 99.

mult = []

for i in range(1, 100):
    if i % 3 == 0:
        mult.append(i)
print(mult)       

# 36. Programa que imprima la tabla de multiplicar hasta 10 de un número cualquiera ingresado por el usuario. 

mult = int(input("De que numero quiere ver la tabla de multiplicar: "))

for i in range(0,10):
    i +=1
    tabla = mult*i
    print(f"{mult} * {i} : {tabla}")

#37. Realizar un Programa que permita visualizar en pantalla los múltiplos de 5 hasta el número 100.

mult = []

for i in range(1,101):
    if i%5==0:
        mult.append(i)
print(mult)

#38. Programa que permita determinar si un estudiante que recibe 15 notas gana o no la materia de Programación De Software. Se gana la materia si el promedio es mayor o igual a 4.0.

notas = []

for i in range(1,16):
    nota = float(input(f"Digite la nota {i}: "))
    notas.append(nota)
print(notas)

suma = sum(notas)
prom = suma/15

if prom >= 4.0:
    print(f"Pasate la materia con una nota {prom}")
else:
    print(f"No pasaste la materia por tener la nota en {prom}")

#39. Programa que encuentre el resultado de la operación potencia donde el usuario ingresa el valor de la base y el exponente. 

base = float(input("Ingrese el valor de la base: "))
expo = float(input("Ingrese el valor del exponente: "))

while expo<0:
    print("Error el exponente debe ser positivo")
    expo = float(input("Ingrese el valor del exponente: "))

ope = base**expo

print(f"El resultado de {base} elevado a la {expo} es de {ope}")

#40. Programa que calcule la suma de los N primeros números naturales, donde N es un número digitado por el usuario. 

i = 0

num = int(input("Cuantos numeros quiere sumar: "))

lista = []

while i<num:
    i+=1
    lista.append(i)
print(lista)

suma = sum(lista)

print(f"La suma de los numeros solicitados es {suma}")

#41. Programa que reciba un listado de N números ingresados por el usuario y luego determine el número mayor y el número menor de entre todos los datos ingresados.   

lista = []
i = 0
n = int(input("Cuantos numeros desea ingresar: "))

while i<n:
    num = int(input("Digite el numero: "))
    i+=1
    lista.append(num)
print(lista)
menor = min(lista)
mayor = max(lista)

print(f"El numero mayor es {mayor} y el menor es {menor}")

#42. Programa que permita obtener el cubo, la cuarta y la quinta potencia de N números ingresados por el usuario.  

def obtener_potencias(numeros):
    potencias = []
    for numero in numeros:
        potencias.append([numero**3, numero**4, numero**5])
    return potencias

def main():
    numeros = []
    continuar = True

    while continuar:
        try:
            numero = int(input("Ingrese un número o escriba 'fin' para terminar: "))
            numeros.append(numero)
        except ValueError:
            if input("¿Desea terminar? (s/n): ").lower() == 's':
                continuar = False

    if numeros:
        potencias = obtener_potencias(numeros)

        print("Potencias de los números ingresados:")
        for i, potencia in enumerate(potencias, start=1):
            print(f"Número {i}: Cubo={potencia[0]}, Cuarta={potencia[1]}, Quinta={potencia[2]}")
    else:
        print("No se han ingresado números.")

if __name__ == "__main__":
    main()

#43. Programa que permita ingresar N números y determine cuantas veces aparece el mismo número, dicho número a buscar debe solicitarse al usuario al inicio del programa.

def contar_repeticiones(numero_buscado, numeros):
    contador = 0
    for numero in numeros:
        if numero == numero_buscado:
            contador += 1
    return contador


def main():
    numero_buscado = float(input("Ingrese el número que desea buscar: "))
    numeros = []
    i = 0
    while i<numero_buscado:
            numero = float(input("Ingrese un número: "))
            numeros.append(numero)
            i+=1
    repeticiones = contar_repeticiones(numero_buscado, numeros)
    print(f"El número {numero_buscado} aparece {repeticiones} veces en la lista de números.")
if __name__ == "__main__":
    main()

#44. Programa que reciba N calificaciones de una materia, y luego calcule: a) La nota promedio b) La nota mayor c) Si El estudiante pasa o no la materia (Promedio>=40) 

cal = int(input("Cuantas notas quiere ingresar: "))
i = 0
lista_not = []

while i<cal:
    notas = float(input("Digite la nota: "))
    lista_not.append(notas)
    i += 1
print(lista_not)

suma = sum(lista_not)

prom = suma/cal

max_nota = max(lista_not)

print(f"El promedio fue de {prom}")
print(f"La nota maxima fue de {max_nota}")

if prom >= 4.0:
    print(f"Pasas la materia con {prom}")
else: 
    print(f"No pasas la materia con {prom}")

#45. Programa  que  permita  calcular  el  factorial  de  un  número.  El  factorial  corresponde  a  la multiplicación de todos los números naturales anteriores incluyendo el número ingresado. 

num = int(input("Ingresa un número: "))

factorial = 1
i = 1

if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    while i <= num:
        factorial *= i
        i += 1
    print("El factorial de", num, "es", factorial)

#46. Programa que permita calcular el valor a pagar en una caja registradora donde se reciben N productos y se ingresan los precios de uno en uno.

cant = int(input("Cuantos productos va a pagar: "))
i = 0
lista = []
while i < cant:
    prod = float(input("Digite el valor del producto: "))
    i +=1
    lista.append(prod)

total = sum(lista)

print(f"El total es de {total:.3f}")

#47. Crear un Programa que permita conocer la mayor estatura dentro un grupo de N estudiantes.  

n = int(input("Cuantos estudiantes son: "))
lista = []
i = 0 
while i < n:
    estat = float(input("Digite su estatura: "))
    lista.append(estat)
    i+= 1
max_alt = max(lista)

print(f"La mayor estatura es de {max_alt:.2f} mts")

#48. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción salir. Las opciones del menú deben permitir:       
#1. Ingresar 2 números 2. Realizar la suma 3. Realizar la resta 4. Realizar la multiplicación 5. Realizar la división 6. Salir del programa 

continuar = True

while continuar:
    print("\t.:MENU:.") 
    print("1. Ingresar 2 números")
    print("2. Realizar la suma")
    print("3. Realizar la resta")
    print("4. Realizar la multiplicación")
    print("5. Realizar la división")
    print("6. Salir del programa")
    op = int(input("Elige una opción: "))
    if op == 1:
        num1 = int(input("Digite un numero: "))
        num2 = int(input("Digite un numero: "))
    elif op == 2:
        suma = num1+num2
        print(f"El resultado de la suma es {suma}")
    elif op == 3:
        resta = num1-num2
        print(f"El resultado de la suma es {resta}")
    elif op == 4:
        mult = num1*num2
        print(f"El resultado de la suma es {mult}")
    elif op == 5:
        div = num1/num2
        print(f"El resultado de la suma es {div}")
    elif op == 6:
        continuar = False
        print("Saliste del programa")
    else: 
        print("Error")

#49. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Calcular el factorial de un número (usando un ciclo repetitivo for) 2. Calcular la potencia (usando un ciclo repetitivo while) 3. Salir 

continuar = True

while continuar:
    print("\t.:MENU:.") 
    print("1. Calcular el factorial de un número")
    print("2. Calcular la potencia")
    print("3. Salir")
    op = int(input("Elige una opción: "))
    if op == 1:
        n = int(input("Digite un numero positivo: "))
        if n < 0:
            print("Error")
            n = int(input("Digite un numero positivo: "))
        else:
            resultado = 1
            for i in range(n):
                resultado *= n
                n -= 1
        print(f"El factorial es {resultado}")
    elif op == 2:

        resultado = 1
        contador = 0

        base = float(input("Ingresa la base: "))
        exponente = int(input("Ingrese el exponente en numero positivo: "))

        while contador < exponente:
            resultado*= base
            contador+=1

        if exponente < 0: 
            print("Digite un numero positivo")
        else: 
            resultado = base**exponente
            print(f"{base} elevado a la {exponente} es: {resultado}")
    elif op == 3:
        print("Saliste del programa")
        break
    else: 
        print("Error")
        
#50. Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir:    
#1. Números pares hasta 100 (usando for) 2. Múltiplos de 4 (usando while) 3. Tabla de Multiplicar de un número hasta 10  

seguir = True
            
while seguir:
    print("\t.:MENU:.") 
    print("1. Números pares hasta 100")
    print("2. Múltiplos de 4")
    print("3. Tabla de Multiplicar de un número hasta 10")
    print("4. Salir")
    op = int(input("Elige una opción: "))
    if op == 1:
        for i in range(1, 101):
            if i%2 == 0:
                print (i)
    elif op == 2:
        i = 0
        while i < 100:
            i+=1
            if i%4 == 0:
                print(i)
    elif op == 3: 
        num = int(input("Digite un numero: "))
        for i in range(1, 11):
            tabla = num * i
            print(f"{num} * {i} : {tabla}")
    elif op == 4:
        print("Saliste del programa")
        seguir = False
    else:
        print("Error")

#51. Programa que permita almacenar 10 valores en un vector que represente las edades de 10 personas y luego muestre cada uno de los valores ingresados.

personas = 10
i = 0
lista = []

while i < personas:
    edad = int(input("Cual es su edad: "))
    i += 1
    lista.append(edad)
print(lista)

#52. Programa que permita solicitar 15 nombres, almacenarlos en un vector y luego los muestre en el orden ingresado.

personas = 15
i = 0
lista = []

while i<personas:
    nom = input("Cual es su nombre: ")
    i += 1
    lista.append(nom)
print(lista)

#53. Programa que permita sumar todos los valores ingresados en un vector de 12 posiciones, los valores deben ser ingresados por el usuario. 

i = 0
lista = []

while i<12:
    num = int(input("Digite un numero: "))
    i += 1
    lista.append(num)
suma = sum(lista)
print(f"La suma de los numeros es: {suma}")

#54. Programa que permita llenar un vector de 20 posiciones y luego determine cuantos son positivos, cuántos son negativos y cuantos son ceros.

positivos = 0
negativos = 0
ceros = 0
lista = []

for i in range(20):
    num = int(input("Digite un numero: "))
    lista.append(num)

for i in lista:
    if i > 0:
            positivos += 1
    elif i < 0:
            negativos += 1
    else:
            ceros += 1

print(f"Los numeros positivos son: {positivos}")
print(f"Los numeros negativos son: {negativos}")
print(f"Los ceros son: {ceros}")

#55. Programa que permita llenar un vector de 20 posiciones y luego le pregunte al usuario cual posición desea ver en pantalla.

lista = []

for i in range(20):
    num = int(input("Digite un numero: "))
    lista.append(num)

while True:
    pos = int(input("Ingrese la posicion que desea ver: "))
    if 0 <= pos < len(lista):
        print(f"El valor en la posición {pos} es: {lista[pos]}")
    elif pos >= 20:
        print("Saliste del programa")
        break


#56. Programa que permita llenar un vector de 18 posiciones y después mostrarlo al revés.

lista = []

for i in range(18):
    num = int(input("Digite un numero: "))
    lista.append(num)

invertida = list(reversed(lista))

print(invertida)

#57.  Programa que permita calcular la cantidad total de clientes que atienden en un mes un hotel utilizando un vector. Como entrada se debe solicitar el número de clientes que atiende el hotel cada día del mes.

mes = []

i = 0 

while i < 30:
    clientes = int(input(f"Cuantos clientes ingresaron el día {i+1}: "))
    i+=1
    mes.append(clientes)

print(mes)

total_cli = sum(mes)

print(f"El total de clientes en el mes fue de {total_cli}")

#58. Programa que permita llenar dos vectores de 12 posiciones y luego en un tercer y cuarto vector guardar la suma y resta de cada posición. Al final se deben mostrar de forma completa todas las sumas y restas realizadas. 

lista1 = []
lista2 = []

for i in range(12):
    num1 = int(input("Digite un numero para la primera lista: "))
    num2 = int(input("Digite un numero para la segunda lista: "))
    lista1.append(num1)
    lista2.append(num2)

suma_lista = [num1+num2 for num1, num2 in zip(lista1, lista2)]
resta_lista = [num1-num2 for num1, num2 in zip(lista1, lista2)]

print("Suma de listas por posicion")
for i, suma in enumerate(suma_lista):
    print(f"Posición {i+1}: {suma}")

print("Resta de listas por posicion")
for i, resta in enumerate(resta_lista):
    print(f"Posición {i+1}: {resta}")

#59. Programa que permita llenar un vector de N posiciones y luego en un segundo y tercer vector guarde el cuadrado y el cubo de cada una de las posiciones. Finalmente imprimir el contenido de todos los vectores.                            

lista = []
cuadrado = []
cubo = []

pos = int(input("Cuantas posiciones quiere en la lista: "))

for i in range(pos):
    num = int(input("Digite un numero para la lista: "))
    lista.append(num)

cuadrado_lista = [num ** 2 for num in lista]
cubo_lista = [num ** 3 for num in lista]

cuadrado.append(cuadrado_lista)
cubo.append(cubo_lista)

print(f"Los numeros de la lista la cuadrado son: \n{cuadrado}")
print(f"Los numeros de la lista al cubo son: \n{cubo}")

#60.  Programa que permita Ingresar el número de estudiantes asignados cada uno de los 20 salones de un colegio y luego satisfacer los siguientes requerimientos: a) Determinar la cantidad total de estudiantes b) Determinar el curso con mayor cantidad de estudiantes c) Determinar el curso con menor cantidad de estudiantes.

curso = []

for i in range(20):
    estu = int(input(f"Cuantos estudiantes tiene el salon {i+1}: "))
    curso.append(estu)

total_estu = sum(curso)

for i in curso:
    mas_estu = max(curso)
    i_max = curso.index(mas_estu)
    min_estu = min(curso)
    i_min = curso.index(min_estu)

print(f"La suma de todos los salones es {total_estu}")
print(f"El salon con mas estudiantes es {i_max+1} con {mas_estu} estudiantes")
print(f"El salon con menos estudiantes es {i_min+1} con {min_estu} estudiantes")

#61. Programa que permita solicitar 25 nombres y 25 apellidos y los muestre en forma de un único listado  

nom = []
apell = []

for i in range(25):
    nombre = input(f"Digite su nombre {i+1}: ")
    nom.append(nombre)

for i in range(25):
    apellido = input(f"Digite su apellido {i+1}: ")
    apell.append(apellido)

for nombre, apellido in zip(nom, apell):
    print(f"{nombre} {apellido}")

#62. Programa que permita llenar una matriz y mostrar todos los datos ingresados y su respectiva posición (fila, columna) en pantalla

rows = int(input("Cuantas filas desea en su matriz: "))
columns = int(input("Cuantas columnas desea tener en su matriz: "))

matrix = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elementos de la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)

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

#64. Programa que permita llenar una matriz cuyo número de filas y número de columnas es ingresado por el usuario. Se le debe luego preguntar al usuario que posición de la matriz desea ver (que fila y que columna) y mostrar el contenido de esa posición. Se debe repetir la pregunta tantas veces sea necesario hasta que el usuario solicite un numero de fila o número de columna mayor al asignado a la matriz.

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

continuar = True

while continuar:
    fila = int(input(f"Ingrese el numero de la fila que desea ver (0 a {rows-1}), o un numero mayor para salir: "))
    if fila >= rows:
        continuar = False
    else:
        columna = int(input(f"Ingrese el número de columna que desea ver (0 a {columns-1}), o un número mayor para salir: "))
        if columna >= columns:
            continuar = False
        else:
            if fila < 0 or columna < 0:
                print("Los índices deben ser números positivos.")
            else:
                print(f"El elemento en la fila {fila} y columna {columna} es: {matriz[fila][columna]}")

#65. Programa que permita llenar un matriz cuyo número de filas y columnas es ingresado por el usuario y luego determine cuantos números positivos, negativos y ceros fueron ingresaron.

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

negativos = 0
positivos = 0
ceros = 0

for row_position in range(rows):
    row = []
    for element in range(columns):
        num = int(input(f"Digite un numero para la fila {row_position} y la columna {element}: "))
        row.append(num)
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1
    matriz.append(row)

for row in matriz:
    print(row)

print(f"Los numeros positivos son: {positivos}")
print(f"Los numeros negativos son: {negativos}")
print(f"Los ceros son: {ceros}")


#66. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario, donde se busque un valor (Ingresado por el usuario) y al encontrarlo muestre su posición (fila, columna).

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

num_buc = int(input("Que numero quiere buscar en la matriz: "))

fal = False

for row_position in range(rows):
    for elements in range(columns):
        if matriz[row_position][elements] == num_buc:
            print(f"El valor {num_buc} se encuentra en la fila {row_position} y la columna {elements}")
            fal = True
            break
    if fal:
        break

if not fal:
    print(f"\nEl valor {fal} no se encuentra en la matriz.")

#67. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario y luego calcule la suma de cada una de sus filas (una x una).

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

for row_position in range(rows):
    suma_fila = sum(matriz[row_position])
    print(f"La suma de la fila {row_position} es {suma_fila}")

#68. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario y luego calcule la suma de cada una de sus columnas (una x una)   

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

sum_f = int(input("Que fila quiere sumar: "))
suma = 0

for row_position in range(rows):
    for elements in range(columns):
        if (row_position==(sum_f-1)):
            print(matriz[row_position][elements])
            suma += matriz[row_position][elements]
print (f"La suma de la fila {row_position} es {suma}")

#69. Programa que permita llenar una matriz cuadrada de 5 filas y 5 columnas y luego calcule la suma de su diagonal principal. La diagonal principal de una matriz cuadrada es aquella donde el número de fila es igual al número de columna) 

matriz = []

for row_position in range(5):
    row = []
    for elements in range(5):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

suma = 0

for row_position in range(5):
    suma += matriz[row_position][row_position]

print(f"La suma de la diagonal es {suma}")

#70. Programa que permita llenar una matriz cuadrada de 5 filas y 5 columnas y luego calcule la suma de los valores por encima y por debajo de su diagonal principal. 

matriz = []

for row_position in range(5):
    row = []
    for elements in range(5):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

suma_u = 0
suma_d = 0

for row_position in range(5):
    for elements in range(5):
        if row_position < elements:
            suma_u += matriz[row_position][elements]
        elif row_position > elements:
            suma_d += matriz[row_position][elements]

print(f"\nLa suma de los valores por encima de la diagonal principal es: {suma_u}")
print(f"La suma de los valores por debajo de la diagonal principal es: {suma_d}")

