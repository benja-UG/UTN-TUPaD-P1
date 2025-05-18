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
"""