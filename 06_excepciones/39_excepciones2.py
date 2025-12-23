cad = input("Número: ")
try:
    print(10 / int(cad))
except ValueError:
    print("No se puede convertir a entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Otro error")
finally:
    print("Finallyyy")