# Un alumno desea saber cuál será su calificación final en la materia
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales
# * 30% de la calificación del examen final
# * 15% de la calificación de un trabajo final

parcial1 = float(input("Nota parcial 1: "))
parcial2 = float(input("Nota parcial 2: "))
parcial3 = float(input("Nota parcial 3: "))
examen = float(input("Nota examen: "))
trabajo = float(input("Nota trabajo: "))

nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + examen * 0.3 + trabajo * 0.15
print("Nota final: ", nota)