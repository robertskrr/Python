diccionario = {'one':1, 'two': 2, 'three': 3}
print(diccionario["two"])

dict1 = {}
dict1["nombre"] = "jose"
dict1["edad"] = 20
print(dict1)

# Borrar elemento
del diccionario["one"]
print(diccionario)

# Borrar todos los datos
dict1.clear()
print(dict1)

# Acceder a elemento de forma mas segura
dict1.get("ones")
dict1.get("ones", "no existe")

# Recorrer claves
for clave in diccionario.keys():
    print(clave)

# Recorer valores
for valor in diccionario.values():
    print(valor)

# Recorrer claves y valores
for clave, valor in diccionario.items():
    print(clave, valor)