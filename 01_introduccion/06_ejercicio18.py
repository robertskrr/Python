# Pedir el nombre y los dos apellidos de una persona
# y mostrar las iniciales

nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

inicial = nombre[0]
inicial += apellido1[0]
inicial += apellido2[0]

# Método upper para mayusculas
inicial = inicial.upper()
print("Iniciales:", inicial)