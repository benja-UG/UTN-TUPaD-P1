"""1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  """

#print("Hola Mundo!")

###########################################################

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo
usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa
debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas
print(f…) para realizar la impresión por pantalla. """

#Nombre = input("Escribe tu Nombre: ")
#print(f"Hola {Nombre}!")

###########################################################

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de
residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si
el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy
Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si
utilizas print(f…) para realizar la impresión por pantalla"""

#Nombre = input("Describe tu Nombre: ")
#Apellido = input("Describe tu Apellido: ")
#Edad = input("Escribe tu Edad: ")
#Residencia = input("Ingresa lugar donde resides: ")

#print(f"Mi Nombre es {Nombre} {Apellido}, tengo {Edad} y vivo en {Residencia}")

###########################################################

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su
área y su perímetro."""

#Radio = float(input("Introduzca el numero de radeo: "))
#pi = 3.14159
#Area = pi * (Radio**2)
#Perimetro = 2 * Radio * pi
#print("El area es: ", Area)
#print("Perimetro es: ", Perimetro)

###########################################################

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por
pantalla a cuántas horas equivale. """

#segundos = int(input("Introduce los segundos para calcular: "))
#division = (segundos/3600)
#print(f"({segundos}) equivale a {division:.2f} horas")

###########################################################

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""

#numero = int(input("Ingresa un numero para ver su tabla de multiplicacion: "))
#for i in range(1, 11):
#    print(f"{numero} x {i} = ", int(numero * i))

###########################################################
"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

#N1 = int(input("Ingresa un numero entero: "))
#N2 = int(input("Ingresa un segundo numero entero: "))

#if N1 == 0 or N2 == 0:
#    print("error, tienen que ser mayores a 0")
#else:
#    print("Suma =", N1 + N2)
#    print("Resta =", N1 - N2)
#    print("Multiplicacion =", N1 * N2)
#    print("Division =", N1/N2)

###########################################################

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
𝐼𝑀𝐶 = Peso en kg/ (altura en m)2"""

#altura = float(input("Indica tu estatura en Metros: "))
#peso = float(input("Indica tu peso en kg: "))
#imc = peso / (altura ** 2)
#print(f"Tu resultado de IMC es: {imc:.2f}")

###########################################################

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 95 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32"""

#celsius = int(input("Introduzca un valor en grados celsius: "))
#Fahrenheit = (9/5 * celsius) + 32
#print(f"La conversion de celsius a Fahrenheit es: {Fahrenheit}")

###########################################################

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el
promedio de dichos números"""

#N1= int (input ("ingresa un numero: "))
#N2= int (input ("ingrsa un segundo numero: "))
#N3= int (input ("ingresa un tercer numero: "))

#promedio= (N1+N2+N3) / 3

#print(f"el promedio de los tres valores es: {promedio:.2f}")