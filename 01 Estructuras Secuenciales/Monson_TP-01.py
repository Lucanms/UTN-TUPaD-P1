# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")



# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("ingresa tu nombre")
print(f"hola, {nombre}!")




# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre_completo = input("ingresa tu nombre completo")
edad = input("ingresa tu edad")
residencia = input("ingresa tu residencia")

print(f"soy {nombre_completo}, tengo {edad} años y vivo en {residencia}")





# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

radioCirculo = float(input("ingresa el radio de un circulo"))

perimetro = 2 * radioCirculo * math.pi

areaCirculo = math.pi * radioCirculo**2

print(f"el area y perimeto son {areaCirculo} y {perimetro} respectivamente")





# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seg = float(input("ingresa segundos para convertir: "))

hs = (seg / 60) / 60

hs = round(number = hs, ndigits = 6)

print(f"{seg} segundos equivales a {hs} horas")





# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("ingresa el numero de tabla que quieras saber: "))
print(f"tabla del {numero}: ")

for i in range(0,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")





# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.



num1 = float(input("ingresa un numero distinto de 0: "))
num2 = float(input("ingresa otro: "))


print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")





# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

altura = float(input("ingresa tu altura"))
peso = float(input("ingresa tu peso"))

masa = peso / altura**2

print(f"tu indice de masa corporal es {masa}")




# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = (9 / 5) * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celcius = float(input("ingresa los grados celcius"))

fahren = (9 / 5) * celcius + 32

print(f"{celcius}° celcius equivalen a {fahren}° fahrenheit")




# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("ingresa el primer numero"))
num2 = float(input("ingresa el segundo"))
num3 = float(input("ingresa el tercero"))

promedio = (num1 + num2 + num3) / 3

print(f"el promedio es de {promedio}")