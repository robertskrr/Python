# Programa que comprueba si una cadena leída por teclado
# comienza por una subcadena introducida por teclado

cadena = input("Cadena: ")
subcadena = input("Subcadena: ")

if cadena.startswith(subcadena):
        print("Empieza con la subcadena")
else:
        print("NO empieza por la subcadena")