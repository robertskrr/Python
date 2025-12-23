lista1 = [1,2,3,4,5,6]
lista2 = ["a", "b", "c", "d", "e"]

# Recorrer ambas listas con zip en mismo for
for num, letra in zip(lista1, lista2):
    print(num," + ", letra)

# Unir listas
lista1.extend(lista2)
print(lista1)

# Insertar en indice concreto
lista2.insert(1, 100)
print(lista2)

# Añadir
lista2.append(420)
print(lista2)

# Eliminar ultimo elemento, también puedes concretar el índice con pop(i)
print(lista1.pop())

# Elimina todos los elementos con la concurrencia
lista1.remove(3)

# Ordenar lista
lista = [3, 2, 1]
lista.reverse() ## INVERSO
lista.sort() ## NORMAL

# Contar cuantos elementos hay del buscado
print("¿Cuántos 2 hay?:", lista1.count(2))

# Devuelve el índice del elemento
lista1.index(1) ## Devuelve indice 0
lista1.index(5, 3) ## A partir del índice 3 lo busca