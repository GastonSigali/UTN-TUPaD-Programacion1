# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su Nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con 
# los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre2 = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
edad = input("Ingrese su Edad: ")
pais = input("Ingrese su residencia: ")

print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {pais}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

radio = int(input("Ingrese el radio de un circulo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

hora = 3600
segundos = float(input("Ingrese la cantidad de segundos: "))
total =  segundos / hora
print(f"La cantidad de segundos ingresados equivale a {total} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

multiplo = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
total = multiplo * 1
print(f"{multiplo} X 1 = {total}" )
total = multiplo * 2
print(f"{multiplo} X 2 = {total}" )
total = multiplo * 3
print(f"{multiplo} X 3 = {total}" )
total = multiplo * 4
print(f"{multiplo} X 4 = {total}" )
total = multiplo * 5
print(f"{multiplo} X 5 = {total}" )
total = multiplo * 6
print(f"{multiplo} X 6 = {total}" )
total = multiplo * 7
print(f"{multiplo} X 7 = {total}" )
total = multiplo * 8
print(f"{multiplo} X 8 = {total}" )
total = multiplo * 9
print(f"{multiplo} X 9 = {total}" )
total = multiplo * 10
print(f"{multiplo} X 10 = {total}" )

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, 
# dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un primer número que no sea 0: "))
num2 = int(input("Ingrese un segundo número que no sea 0: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es: {suma}")
division = num1 / num2
print(f"La división de {num1} y {num2} es: {division}")
multi =  num1 * num2
print(f"La multiplicación de {num1} y {num2} es: {multi}")
resta =  num1 - num2
print(f"La resta de {num1} y {num2} es: {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = float(input("Ingrese por favor su altura: "))
peso = float(input("Ingrese por favor su peso: "))
imc = peso / (altura ** 2)
print(f"El indice de masa corporal es el siguiente: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:

celsius = int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = int(celsius * (9 / 5) + 32)
print(f"La equivalencia en grados fahrenheit es: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = int(input("por favor ingrese el primer número para hacer su promedio: "))
num2 = int(input("por favor ingrese el segundo número para hacer su promedio: "))
num3 = int(input("por favor ingrese el tercer número para hacer su promedio: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de lo tres números ingresados es:{promedio}")
