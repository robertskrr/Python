# Lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
# caráctter en la cadena

dict = {}
cadena = input("Cadena: ")
for caracter in cadena:
    if caracter in dict:
        dict[caracter] += 1
    else:
        dict[caracter] = 1

for campo, valor in dict.items():
    print(campo, "->", valor)