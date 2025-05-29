# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario


def factorial(num):
  if num == 1:
    return num
  return num * factorial(num-1)

num = int(input("Ingrese un numero: "))

print(factorial(num))



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.


def fibonacci(num):
  if num == 1 or num == 0:
    return num
  return fibonacci(num - 1) + fibonacci(num - 2)

numUser = int(input("Ingrese hasta que posicion quiere que sea la serie: "))

for i in range(numUser):
  print(fibonacci(i), end=" ")



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1) . Prueba esta función en un algoritmo general.


# calcula la potencia usando recursividad
def potencia(base, exp):
  # caso base
  if exp == 0:
    return 1

  return base * potencia(base, exp - 1)

# el usuario ingresa la base y el exponente
num = float(input("Ingresa la base: "))
expt = float(input("Ingresa el exponente: "))

try:
  # lanza un error si el exponente es decimal o negativo
  if expt < 0 or not expt.is_integer():
    raise ValueError("El exponente ingresado no es valido, tiene que ser entero y positivo")

  # convierte el exponente en entero y muestra la funcion con un print
  expt = int(expt)
  print(potencia(num,expt))

# captura y muestra el error
except ValueError as e:
  print(e) 



# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 
 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# 🧠Ejemplo: 
# Convertir el número 10 a binario: 
# 10 ÷ 2 = 5 resto: 0 
# 5 ÷ 2 = 2 resto: 1 
# 2 ÷ 2 = 1 resto: 0 
# 1 ÷ 2 = 0 resto: 1 
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


def binario(num):
  # si num es 1 o 0 retorna el dicho valor como str
  if num == 1:
    return "1"
  
  if num == 0:
    return "0"
  
  # devuelve el valor de los if y le añade el resto de num entre 2 convertido en str
  return binario(num // 2) + str(num % 2)

print(binario(20))



# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.  Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
  def pal(palabra, i, f):
    if i >= f:
      return True

    if palabra[i] != palabra[f]:
      return False

    return pal(palabra, i + 1, f - 1)
  
  return pal(palabra,0, len(palabra) - 1)

palabra = input("Ingresa una palabra para verificar si un palindromo: ")

print(es_palindromo(palabra))



# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión. 

# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4) 
# suma_digitos(9) → 9 
# suma_digitos(305) → 8 (3 + 0 + 5)


def suma_digitos(n):
  if n < 10:
    return n
  
  return n%10 + suma_digitos(n//10)

num = int(input("Ingresa un numero: "))

print(suma_digitos(num))



# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.  
# Ejemplos: 
# contar_bloques(1) → 1 (1) 
# contar_bloques(2) → 3 (2 + 1) 
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)


def contar_bloques(n):
  if n == 1:
    return n
  return n + contar_bloques(n - 1)

num = int(input("Ingresa el numero de bloques: "))

print(f"Bloques necesarios: {contar_bloques(num)}")



# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.  Ejemplos: contar_digito(12233421, 2) → 3 contar_digito(5555, 5) → 4 contar_digito(123456, 7) → 0


def contar_digito(numero, digito):
  if numero % 10 == digito:
    return 1 + contar_digito(numero//10, digito)
  
  if numero < 10:
    return 1 if numero % 10 == digito else 0
  
  return contar_digito(numero//10, digito)

num, digito = int(input("Ingresa el numero: ")), int(input("Ingresa el digito: "))

print(contar_digito(num, digito))
