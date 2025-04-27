# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.


# crea una lista de numeros multiplos de 4 usando range y la funcion list
numeros = list(range(4,101, 4))

# muestra la lista
print(numeros)




# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!


# crea una lista a partir de un string
lista = list("texto")

# lo muestra
print(lista[-2])




# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []


# crea la lista vacia
lista = []

# agrega tres palabras usando el metodo append
lista.append("uno")
lista.append("dos")
lista.append("tres")

# muestra la lista
print(lista)




# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!


# uso la variable ya creada
animales = ["perro", "gato", "conejo", "pez"]

# modifica el segundo y ultimo elemento de la lista
animales[1], animales[-1] = "loro", "oso"

# la muestra
print(animales)




# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.


# se crea una lista de 5 elementos
numeros = [8,15,3,22,7]

# se borra el elemento con el mayor valor de la lista
numeros.remove(max(numeros))

# lo muestra
print(numeros)




# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.


# crea una lista de numeros del 10 al 30 saltando de 5 en 5
nums = list(range(10, 31, 5))

# muestra los dos primeros elementos usando slicing
print(nums[0:2])




# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.


autos = ["sedan", "polo", "suran", "gol"]

# modifica los valores de los elementos centrales
autos[1], autos[2] = "yamaha", "essen"

print(autos)




# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.


# se crea lista dobles
dobles = []

# agrega los valores a la lista, se podria haber hecho con un for pero lo preferi así
dobles.append(10)
dobles.append(20)
dobles.append(30)

# se muestra
print(dobles)




# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# añade otro valor a la ultima sublista
compras[2].append("jugo")

# modifica el valor del segundo elemento de la segunda sublista
compras[1][1] = "tallarines"

# borra el primer elemento de la primera sublista
compras[0].remove("pan")

# lo muestra
print(compras)




# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.


# crea la lista
lista_anidada = []

# agrega los elementos a la lista, no sabia si habia que hacerlo asi o directamente cuando de definio la variable asi que lo puse asi
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)

# lo muestra
print(lista_anidada)