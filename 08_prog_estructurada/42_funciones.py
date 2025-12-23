def operar(a, b):
    return a + b

print(operar(3, 4))

def factorial(n):
    resultado = 1
    for i in range (1, n+1):
        resultado*=i
    
    return resultado

print(factorial(5))