# Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de ambas
# y muestre cuanto valen al final las dos variables
a = int(input("Variable A: "))
b = int(input("Variable B: "))

aux = a
a = b
b = aux

print("Nuevo valor de A: ", a)
print("Nuevo valor de B: ", b)
