# 1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

nuevos_precios = {"Naranja": 1200, "Manzana": 1500, "Pera": 2300}

precios_frutas.update(nuevos_precios)



# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

nuevos_precios = {"Banana": 1330, "Manzana": 1700, "Melón": 2800}

precios_frutas.update(nuevos_precios)

print(precios_frutas)




# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = list(precios_frutas.keys())

print(frutas)



# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:

contactos = {}

num = int(input("¿Cuantos contactos quiere agregar?: "))

for i in range(num):
  nombre = input("\nIngrese el nombre del contacto: ")
  contactos[nombre] = input("Ingrese su numero: ")

persona = input("\nIngrese el nombre de la persona para ver su numero: ")


try:
  if persona not in contactos:
    raise ValueError("el contacto no existe")
  
  print(f"El numero de {persona} es {contactos[persona]}")
  
except ValueError as e:
  print(e)



# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

from collections import Counter

frase = input("Ingresa una frase: ")

palabras = frase.replace(",", "").replace(".", "").split()

palabras_unicas = set(palabras)

conteo = Counter(palabras)

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", dict(conteo))




# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
  alumno = input("Ingresa el nombre del alumno: ")
  notas = []
  
  print("Ingresa sus notas")
  
  for i in range(3):
    notas.append(float(input()))

  alumnos[alumno] = tuple(notas)
  
  
print(f"Lista de alumnos: {alumnos}")

for alumno in alumnos:
  promedio = round(sum(alumnos[alumno]) / 3, 2)
  print(f"El promedio de {alumno} es: {promedio}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial_1 = {3,2,7,4,10,5,8}
parcial_2 = {7,8,5,2,9}

print(f"Estudiantes que aprobaron los dos parciales: {parcial_1.intersection(parcial_2)}")
print(f"Estudiantes que aprobaron solo un parcial: {parcial_1.symmetric_difference(parcial_2)}")
print(f"Estudiantes que aprobaron al menos un parcial: {parcial_1.union(parcial_2)}")



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.


productos = {}

while True:
  print("\n1. Consultar stock de un producto\n2. Agregar producto\n3. Lista de productos\n4. Salir\n")
  op = input("Ingrese el numero de la operacion: ")

  if op == "1":
    producto = input("Ingrese el nombre del producto : ")
    
    if producto not in productos:
      print("Lo sentimos, el producto no existe, lo agregaremos en breve")
      productos[producto] = 1
      continue
    
    if productos[producto] == 1:
      print(f"Hay solo una unidad de {producto}")
      continue
    
    print(f"Hay {productos[producto]} unidades del producto")

  elif op == "2":
    producto = input("Ingrese el nombre del producto: ")
    
    if producto in productos:
      print("El producto ya existe, pero aumentaremos su stock")
      productos[producto] += 1

    else:
      print("Producto agregado")
      productos[producto] = 1
      
  elif op == "3":
    print(productos)

  elif op == "4":
    print("La ejecucion termino")
    break
  
  else:
    print("Opcion invalida")
    continue


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
  ("lunes", "10:00"): "Reunión",
  ("lunes", "6:00"): "Otra Reunión",
  ("miercoles", "20:00"): "Clase de ingles"
}


def consultarAgenda(dia, hora):
  clave = (dia.lower(), hora)
  actividad = agenda.get(clave)

  if actividad:
      print(f"El {dia} a las {hora} tenés: {actividad}.")
  else:
      print(f"No hay actividades programadas el {dia} a las {hora}.")
      
      
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
  "Argentina": "Buenos aires",
  "Peru": "Lima",
  "Chile": "Santiago de Chile"
}

capitales = {}

def nuevoDiccionario(diccionario):
  for pais, capital in diccionario.items():
    capitales[capital] = pais
  
nuevoDiccionario(paises)
print(capitales)