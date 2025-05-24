# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.


# funcion imprime el msj
def imprimir_hola_mundo():
  print("Hola Mundo!")

imprimir_hola_mundo()



# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.


# muestra un msj personalizado
def saludo_usuario(nombre):
  print(f"Hola {nombre}!")

# pide el nombre del usuario y muestra el msj 
nombre = input("Ingresa tu nombre: ")

saludo_usuario(nombre)



# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


# muestra un msj con la informacion personal del usuario
def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# pide y guarda la informacion del usuario
nombre, apellido = input("Ingresa tu nombre: "), input("Ingresa tu apellido: ")
edad, residencia = input("Ingresa tu edad: "), input("Ingresa tu residencia: ")

# ejecuta la funcion con los paramentros dados
informacion_personal(nombre, apellido, edad, residencia)



# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


# se importa el modulo math
import math

# se guarda el valor de pi
pi = math.pi

# la funcion calcula el area de un circulo usando el radio
def calcular_area_circulo(radio):
  return pi * radio**2

# funcion que calcula el perimetro de un circulo
def calcular_perimetro_circulo(radio):
  return 2 * pi *radio

# pide el radio al usuario
radio = float(input("Ingresa el radio: "))

# muestra un mensaje con los valores retornados por las funciones
print(f"El area es {calcular_area_circulo(radio)} y el perimetro {calcular_perimetro_circulo(radio)}")



# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
  # divide los segundos entre 3600 para obtener las horas
  horas = segundos / 3600
  return horas

# pide al usuario que ingrese los segundos
seg = float(input("Ingresa los segundos: "))

# muestra un mensaje
print(f"{segundos_a_horas(seg)}h son {seg}s")



# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.


# funcion que itera desde 1 a 11
def tabla_multiplicar(numero):
  for i in range(1, 11):
    # muestra un mensaje con la tabla de multiplicar de un numero
    print(f"{numero} x {i} = {numero * i}")

# pide al usuario un numero
num = int(input("Ingresa un numero: "))

tabla_multiplicar(num)



# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas(a, b):
  # se crea una tupla con las operaciones pedidas en el enunciado y sus resultados
  operaciones = (f"Suma: {a + b}", f"Resta: {a - b}", f"Multiplicacion: {a * b}", f"Division: {a / b}")
  return operaciones

# pide al usuario dos numeros 
a,b = int(input("Ingrese un numero: ")), int(input("Ingrese otro: "))

print(operaciones_basicas(a,b))



# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


# calcula el imc
def calcular_imc(peso, altura):
  imc = round(peso / (altura**2),2)
  return imc

# pide los parametros
peso, altura = float(input("Ingrese su peso en kg: ")), float(input("Ingrese su altura en metros: "))

# muestra un mensaje
print(calcular_imc(peso, altura))



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.


# calcula grados fahrenhit a partir de los grados celcius
def celsius_a_fahrenheit(celcius):
  fahren = (celcius * 9/5) + 32
  return fahren

# pide al usuario los grados en celcius
celcius = float(input("Ingresa los grados celcius: "))

# muestra el resultado
print(f"{celcius}°C equivalen a {celsius_a_fahrenheit(celcius)}°F")



# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.


# calcula el promedio de tres parametros
def calcular_promedio(a,b,c):
  promedio = round((a + b + c) / 3, 2)
  return promedio

# pide al usuario tres valores y los guarda
a,b,c = float(input("Ingresa el primer numero: ")), float(input("Ingresa el segundo numero: ")), float(input("Ingresa el tercer numero: "))

# muestra el promedio
print(f"El promedio es {calcular_promedio(a,b,c)}")