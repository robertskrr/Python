# Lee 5 notas de un alumno(entre 0 y 10)
# Muestra todas las notas, la nota media, la nota mas alta que ha sacado y la menor
notas = []
for indice in range(1, 6):
    while True:
        nota = int(input("Nota %d: " %indice))
        if nota >= 0 and nota <= 10: break
    notas.append(nota)

# Resultado
print("Notas: ", end="")
for nota in notas:
    print(nota, " ", end="")

print()
print("Nota media:", sum(notas)/len(notas))
print("Nota máxima:", max(notas))
print("Nota mínima:", min(notas))