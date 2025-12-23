# Cuenta cuantas palabras tiene una frase introducida por teclado

contador = 0
posicion = 0

cadena = input("Frase: ")

## Elimino los posibles espacios a principio y final
cadena = cadena.strip()
## Busco espsacios
posicion = cadena.find(" ", posicion)
while posicion != -1:
    contador += 1
    ## No cuento los posibles espacios que haya entre las palabras
    while cadena[posicion + 1] == " ":
        posicion += 1
    posicion = cadena.find(" ", posicion + 1)

print("La frase tiene", contador + 1, "palabras")