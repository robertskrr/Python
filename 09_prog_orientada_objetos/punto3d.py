from punto import Punto
## HERENCIA
class Punto3d(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z