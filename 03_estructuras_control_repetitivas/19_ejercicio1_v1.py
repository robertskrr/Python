# Crea un app que pida un número y calcule su factorial

resultado = 1
num = int(input("Número: "))

contador = 2
while contador <= num:
    resultado = resultado * contador
    contador += 1

print("El resultado es", resultado)