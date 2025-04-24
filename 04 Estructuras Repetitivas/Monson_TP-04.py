# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for i in range(101):
  print(i)



# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# pide al usuario que ingrese un numero y lo guarda, definiendo tambien una variable contador
num = int(input("Ingrese un numero: "))
digitos = 0

# crea un bucle que se ejecuta mientras num sea mayor a 0, divide a la num por 10 y la reescribe con el nuevo valor
while num > 0:
  num //= 10
  
  # incrementa la varible contador en 1
  digitos += 1
  
# muestra el mensaje por pantalla
print(f"el numero tiene {digitos} digitos")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.


# pide al usuario que ingrese dos numeros y los guarda en su respectiva variable
num = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))

# crea el acumulador
suma = 0

# crea un bucle que empiece desde num, sumandole 1 para excluir su valor y que termina en num2, avanzando en 1
for i in range(num+1, num2, 1):
  
  # suma el valor de i a la variable suma
  suma += i
  
# imprime la variable suma
print(f"La suma de todos los numeros intermedios es: {suma}")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


# acumulador
suma = 0
# controla si el usuario quiere seguir sumando
log = 0

while True:
  # controla si el valor ingresado es un entero o no
  try:
    num = int(input("Ingresa un numero entero: "))
    suma += num
    
    log += 1
    
    # cuando log sea 2, preguntarle al usuario si quiere continuar sumando y log vuelve a 1, si la respuesta es diferente de "si", muestra la suma y termina el bucle
    
    if log == 2:
      res = input("¿quieres seguir sumando?\n").lower()
      log = 1
      
      if res != "si":
        print(f"El resultado de la suma es: {suma}")
        break
  except:
    print("El numero ingresado no es un entero, intentelo de nuevo")
  else:
    continue



# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


# importa randint de random 
from random import randint

numero_random = randint(0,9)
print(numero_random)

# pide al usuario que ingrese un numero entre 0 y 9, despues los convierte en entero
numero_usuario = int(input("Intenta adivinar un numero entre 0 y 9: "))

# defino la variable que controla el total de intentos
intentos = 1

# bucle que controla que los numeros ingresados sean validos
while True:
  try:
    
    # incrementa el numero de intentos
    intentos += 1
    
    # en este punto el usuario se habra equivocado, ahora le pide que lo intente de nuevo 
    numero_usuario = int(input("Incorrecto, intentalo de numero: "))
    
    # si numero_usuario es igual al numero_random, muestra un mensaje y el numero de intentos para despues salir del bucle
    if numero_random == numero_usuario:
      print(f"¡Correcto!, hiciste {intentos} intentos para adivinar el numero")
      break
  except: 
    print("Ingresa un numero valido")
  else: continue



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.


# muestra un mensaje e imprime los numeros pares usando un for
print(f"Numeros pares entre 100 y 0:")

for i in range(100, -2, -2):
  print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


# pide al usuario un numero e inicializa dos variables
num = int(input("Ingresa un numero entero positivo: "))
suma = contador = 0

# controla que el valor ingresado no sea negativo
while num < 0:
  num = int(input("Ingresaste un numero negativo, vuelve a intentarlo: "))


# controla que haya numero que sumar y que el numero ingresado sea entero
while contador < num:
  try:
    
    # incrementa contador y lo suma a la variable suma
    contador += 1
    suma += contador
  except:
    print("Error, ingrese un numero entero")
  else:
    continue
  
# muestra el mensaje que pide el ejercicio
print(f"La suma de todos los numeros comprendidos entre 0 y {num} es: {suma}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).


# pide 100 numeros enteros, crea el contador y las demas varibles
print("Ingresa 100 numeros enteros: ")
i = 0
positivos = negativos = pares = impares = 0

# el usuario ingresa el numero y el contador se incrementa en 1
while True:
  num = int(input())
  i += 1
  
  # controla que el numero sea positivo y tambien si es par o impar
  if num > 0:
    positivos += 1
    
    if num % 2 == 0:
      pares += 1
    else:
      impares += 1

  # controla si el numero es negativo y tambien par o impar
  elif num < 0:
    negativos += 1
    
    if num % 2 == 0:
      pares += 1
    else:
      impares += 1
  
  # cuando i sea 100 se muestra un mensaje junto con lo que se pide en el ejercicio y sale del bucle
  if i == 100:
    print("Listo, ingresaste todos los numeros")
    print(f"Cantidad de numero positivos: {positivos} \nCantidad de numeros Negativos: {negativos} \nCantidad de numero pares: {pares} \nCantidad de numeros impares: {impares}")
    break



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).


# pide los numeros y define las variables que se van a utilizar
print("Ingresa 100 numeros para calcular el preomedio: ")
i = 0
promedio = 0
suma = 0

# almacena los numeros, aumenta el contador en 1 y suma cada uno de los numeros
while True:
  
  try:
    num = int(input())
    i += 1
    suma += num
    
    # cuando el contador sea igual al valor que queres, divide la suma de todos los numeros por el contador, esto se almacena en la varible promedio
    if i == 100:
      promedio = suma / i
      
      # muestra el mensaje que pide el ejercicio
      print(f"Promedio: {promedio}")
      break
    
  except: 
    print("El valor ingresado debe ser un numero entero")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


# pide el numero que quiere inventir, guarda su longitud y define la varible del nuevo numero
num = input("Ingrese el numero que quiera invertir: ")
longitud = len(num)
new_num = ""

# itera la longitud del numero y guarda el valor de la posicion menos 1
for i in range(longitud, 0, -1):
  new_num += num[i-1]

# convierte el str en int y lo muestra por pantalla
new_num = int(new_num)
print(f"El numero invertido es: {new_num}")