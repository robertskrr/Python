suma = 0

for var in range (1, 6):
    num = int(input("Número: "))
    if num % 2 == 0:
        suma += num

print("La suma de los pares es", suma)