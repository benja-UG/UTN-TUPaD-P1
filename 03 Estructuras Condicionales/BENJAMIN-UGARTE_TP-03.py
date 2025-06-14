#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
""""""""""
edad = int(input("Ingresa tu edad: "))
mayor=18

if edad >= mayor:
    print ("Eres mayor de edad!")
else:
    print ("Eres menor de edad!")

"""""
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
"""
notas = int(input ("Ingresa la nota del examen: "))
minimo=6

if notas >= minimo:
    print("Aprobado")
else:
    print("Desaprobado")

"""
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
num_par = int(input("Ingresa el primer numeros pares: "))


if num_par % 2==0:
    print("Ha ingresado un número par")
else: 
    print("Ha ingresado un numero impar")

"""
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
""""
edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Eres Niño/a")
elif edad >= 12 and edad < 18:
    print("Eres Adolescente")
elif edad >= 18 and edad < 30:
    print("Eres adulto/a joven")
elif edad >= 30:
    print("Eres adulto")

"""
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
""""
contraseña = input ("Ingresa una contraseña: ")

if len(contraseña) >= 8 and (len(contraseña) <= 14) :
    print("Contraseña correcta") 
else:
    print("Error, ingrese una contraseña de entre 8 y 14 caracteres")

"""
#6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
""""
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo a la izquierda")
else:
    print("Sin sesgo")
"""""""""
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
"""""
frase = input("Ingresa una frese o palabra: ")
vocal = frase [-1]

if vocal in "aeiou":
    frase += "!"
    print(frase)
else: 
    print (frase)
    
"""

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""""
nombre = input("ingrese su nombre: ")
print("y elija algunas de las siguientes opciones:")

opciones = int(input("1. Nombre en mayúsculas \n2. Nombre en minúsculas \n3. Nombre con la primera letra mayúscula \nOpcion: "))

if opciones == 1:
    print(nombre.upper())
elif opciones == 2:
    print(nombre.lower())
elif opciones == 3:
    print (nombre.title())
else:
    print("Error, ingrese el numero 1, 2 o 3.")
"""
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños)
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese el numero de la magnitud de un terremoto: "))

if magnitud < 3:
    print(" Muy leve \n(imperceptible)")
elif magnitud >= 3 and magnitud < 4:
   print(" Leve \n(ligeramente perceptible)") 
elif magnitud >= 4 and magnitud < 5:
    print(" Moderado \n(sentido por personas, pero generalmente no causa daños)")
elif  magnitud >= 5 and magnitud < 6:
    print(" Fuerte \n(puede causar daños en estructuras débiles)")
elif  magnitud >= 6 and magnitud < 7:
    print(" Muy Fuerte \n(puede causar daños significativos)")
elif  magnitud >= 7:
    print(" Extremo \n(puede causar graves daños a gran escala)")