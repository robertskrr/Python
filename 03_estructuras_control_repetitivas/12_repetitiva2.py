secreto = "asdasd"
clave = input("Clave: ")

while clave != secreto:
    print("Clave incorrecta!")
    otra = input("¿Quieres introducir otra clave (S/N)?: ")
    if otra.upper() == "N":
        break
    clave = input("Clave: ")

if clave == secreto:
    print("Bienvenido")

print("Programa finalizado")