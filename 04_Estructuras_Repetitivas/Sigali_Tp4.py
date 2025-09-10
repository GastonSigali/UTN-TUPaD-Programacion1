#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range(0,100+1):
    print(cont)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))

cont = 0
num = abs(num)

if num == 0:
    cont = 1 
else:
    while num > 0:
        num = num // 10
        cont = cont + 1

print ("El número entero contiene",cont,"digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))

resultado = 0

if num1 > num2 :
    mayor = num1 - 1
    menor = num2 + 1
else:
    mayor = num2 - 1
    menor = num1 + 1

for menor in range(menor,mayor+1):
    resultado = menor + resultado

print("La suma entre los valores de ",num1, " y ",num2," es: ",resultado)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Por favor ingrese un numero entero: "))

sumatoria = 0

while num != 0 :
    sumatoria = sumatoria + num
    num = int(input("Por favor otro numero entero ( \"0\" para finalizar): "))

print(" El total de los numero es: ",sumatoria)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("Advinar el numero entre 0 y 9")
num = int(input("Ingrese el numero: "))

ACIERTO = 9
cont = 1

while not(num >= 0 and num <= 9):
    print("Error!!!, Ingreso un numero fuera de los rangos")
    num = int(input("Ingrese el numero de nuevo: "))

if num == ACIERTO:
    print("Felicitaciones!! el numero es el correcto!! ", num)
else:
    while num != ACIERTO:
        num = int(input("ERROR!!, Intente de nuevo \n Ingrese un nuevo numero: "))
        cont = cont + 1
    print("Felicitaciones!! el numero es el correcto!!",num)
    print("La  cantidad de intentos:",cont)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

NUMERO = 100
cont = 0

for cont in range(NUMERO,0 + 1, -1):
    if cont % 2 == 0:
        print(f"{cont}")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input(' Ingrese un numero para ver el resultado (entero positivo) '))

acumulador = 0

while num < 0 :
    print(" ERROR : Ingrese un numero positivo ")
    num = int(input(' Ingrese nuevamente un numero (entero positivo) '))

for cont in range(num + 1):
    acumulador = cont + acumulador

print(" La suma entre todos los numeros es: ",acumulador)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

FINAL = 100
par = 0
impar = 0
negat = 0
posit = 0




for cont in range(0,FINAL) :
    num = int(input(" Ingrese 100 números enteros "))
    

    if num >= 0:
        posit += 1
    else:
        negat += 1
    
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(" Total de números pares: ",par)
print(" Total de números impares: ",impar)
print(" Total números positivos ",posit)
print(" Total números negativos ", negat)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

FINAL = 10
suma = 0
resultado = 0

for cont in range(1,FINAL + 1):
    num = int(input(f"{cont} Ingrese un numero entero: "))
    suma += num

resultado = suma / cont

print("La media de los valores ingresados es: ",resultado)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

invertido = 0
digito = 0

num = int(input(" Ingrese Un numero para poder invertirlo: "))

num = abs(num)

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(" El numero invertido es:",invertido)