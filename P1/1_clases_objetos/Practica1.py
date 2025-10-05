#caracteristicas de la poo clases, objetos, metodos, atributos

import os
os.system("cls")

def area_rectangulo(base,altura):
    return base*altura
print(area_rectangulo(5,3))

class Rectangulo:
    def __init__(self,base2,altura2):
        self.base=base2
        self.altura=altura2
    def area(self):
        return self.base * self.altura
rect = Rectangulo(5, 3)
print(rect.area())

