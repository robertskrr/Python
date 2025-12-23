# Pide cadena y carácter por teclado (validando caracter)
# y muestra cuantas veces aparece el caracter

cadena = input("Cadena: ")
while True:
    caracter = input("Caracter: ")
    if len(caracter) > 1:
        print("Introduce solo un carácter")
    if len(caracter) == 1: break

print("En la cadena", cadena, "aparecen", cadena.count(caracter), "veces el carácter", caracter)