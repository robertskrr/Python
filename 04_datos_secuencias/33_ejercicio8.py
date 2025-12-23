# Guardar nombres y edades de alumnos
# Lee datos hasta que se introduzca un asterisco
# Al final muestra: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad)

nombres = []
edades = []

while True:
    nombre = input("Nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad: ")))
    if nombre == "*": break

# Calcular edad máxima
edad_max = max(edades)
# Alumnos mayores de edad
print("Alumnos mayores de edad")
print("======================")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)

# Alumnos mayores
print("Alumnos mayores")
print("================")
for nombre, edad in zip(nombres, edades):
    if edad == edad_max:
        print(nombre)
