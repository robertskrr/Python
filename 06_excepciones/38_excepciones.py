while True:
    try:
        x = int(input("Número: "))
        break
    except ValueError:
        print("Debes introducir un número")