# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.




usuario_edad = int(input("ingresa tu edad: "))

if usuario_edad >= 18:
  print("Es mayor de edad")




# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.



nota = float(input("Ingresa tu nota: "))

if nota >= 6:
  print("Aprovado")
else:
  print("Desaprovado")




# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.




num_par = float(input("Ingresa un numero par: "))

if num_par % 2 == 0:
  print("Ha ingresado un número par")
else: print("Por favor, ingrese un número par")




# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.



edad = int(input("Ingresa tu edad: "))

if edad < 12:
  print("Eres un niño")
elif edad >= 12 and edad < 18:
  print("Eres un adolescente")
elif edad >= 18 and edad < 30:
  print("Eres un adulto joven")
elif edad >= 30:
  print("Eres un adulto mayor")




# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.




clave = input("Ingresa tu contraseña: ")
clave_long = len(clave)

if clave_long >= 8 and clave_long <= 14:
  print("Ha ingresado un contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:

# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)

# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:

# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.

# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.

# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la listanumeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma:

# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]



from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

resultado = f"la media de la lista: {media}, la mediana: {mediana} y la moda: {moda}"

if media > mediana and mediana > moda:
  print(resultado)
  print("la lista de numeros tiene un sesgo positivo")
  
elif media < mediana and mediana < moda:
  print(resultado)
  print("la lista de numeros tiene un sesgo negativo")
  
elif media == mediana == moda:
  print(resultado)
  print("la lista de numeros no tiene ningun sesgo")
  
else: 
  print(resultado)
  print("Ninguno de los valores tiene un orden")




# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.



palabra = input("ingrese una frase o palabra: ")

ult_letra = palabra[-1:]

if ult_letra in "aeiou":
  palabra += "!"

print(palabra)





# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:

# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.



nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese como quiere que se muestre su nombre: \n 1: En mayusculas. \n 2: En minusculas. \n 3: Solo la primera letra en minusculas.\n")


if opcion == "1":
  nombre = nombre.upper()
  print(f"Hola, {nombre}.")
  
elif opcion == "2":
  nombre = nombre.lower()
  print(f"Hola, {nombre}.")
  
elif opcion == "3":
  nombre = nombre.title()
  print(f"Hola, {nombre}.")
  
else: print("Opcion invalida")





# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).



magnitud = int(input("Ingrese la magnitud del terremoto en escala de Richter: "))

if magnitud < 3:
  print("Muy leve (imperceptible)")

elif magnitud >= 3 and  magnitud < 4:
  print("Leve (ligeramente perceptible)")

elif magnitud >= 4 and  magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")

elif magnitud >= 5 and  magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")

elif magnitud >= 6 and  magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")

elif magnitud >= 7:
  print("Extremo (puede causar graves daños a gran escala)")






# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# NO PUSE LA TABLA

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.



hemisferio = input("Ingrese su hemisferio (N/S): ").lower()

mes = input("Ingresa el mes (nombre): ").lower()
dia = int(input("Ingresa el dia: "))


# verifica que los dias sean validos
if dia >= 1 and dia <= 31:
  # verica en que mes, dia y hemisferio se encuentra para despues imprimir por pantalla
  if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
    if hemisferio == "n":
        print("Se encuentra en invierno")
    elif hemisferio == "s":
        print("Se encuentra en verano")
        
  elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
      if hemisferio == "n":
          print("Se encuentra en primavera")
      elif hemisferio == "s":
          print("Se encuentra en otoño")
      
  elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
      if hemisferio == "n":
          print("Se encuentra en verano")
      elif hemisferio == "s":
          print("Se encuentra en invierno")
      
  elif (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
      if hemisferio == "n":
          print("Se encuentra en otoño")
      elif hemisferio == "s":
          print("Se encuentra en primavera")
          
  else:
      print("El mes no existe")
      
else: print("Dia invalido")






