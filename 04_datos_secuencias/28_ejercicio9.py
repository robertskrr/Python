# Programa que comprueba si una cadena contiene una subcadena introducida por teclado

cad = input("Cadena: ")
subcad = input("Subcadena: ")

if cad.find(subcad) > -1:
    print("La cadena contiene la subcadena")
else:
    print("La cadena NO contiene la subcadena")

## Otra forma de comprobarlo
if subcad in cad:
    print("La cadena contiene la subcadena")
else:
    print("La cadena NO contiene la subcadena")