indicador = False

for var in range(1, 6):
    num = int(input("Número: "))
    if num % 2 == 0:
        indicador = True

if indicador:
    print("Has introducido algún número par")
else:
    print("No has introducido ningún número par")