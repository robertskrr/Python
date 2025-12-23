# Algoritmo que muestre la tabla de multiplicar de un número introducido

tabla = int(input("Número: "))

for num in range (1, 11):
    print("%d * %d = %d" % (num, tabla, num * tabla))