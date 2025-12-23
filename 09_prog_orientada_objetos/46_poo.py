from punto import Punto

punto1 = Punto()
punto1.x = 3
punto1.y = 4

punto2 = Punto(5, 7)

print(punto1.mostrar())
print(punto2.mostrar())
print(punto1.distancia(punto2))