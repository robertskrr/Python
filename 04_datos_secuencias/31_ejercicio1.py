# Inicialize lista con 10 valores aleatorios y muestre en pantalla
# cada elemento con su cuadrado y su cubo
import random

lista_numeros = []
for indice in range(1, 11):
    lista_numeros.append(random.randint(1, 10))

for numero in lista_numeros:
    print(numero, " ", numero**2, " ", numero**3)