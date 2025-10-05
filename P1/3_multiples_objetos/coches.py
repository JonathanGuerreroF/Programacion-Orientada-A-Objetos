"""
1-no metodo constructor
2-que los atributos sean publicos
3-metodos acelerar y frenar no hagan nada (para que no haga nada se usa pass)
"""

import os

os.system("cls")

class Coches:
    #Metrodo constructor para poder inicializar los valores de los atrbituos a la hora de crear o instanciar el objeto de la clase
    #En python solo se puede tener un metodo constructor
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

    #Primer forma
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca

    #Segunda forma
    @property
    def marca2(self):
        return self.marca
    @marca2.setter
    def marca2(self,marca):
        self.marca=marca


    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color

    def getModelo(self):
        return self.modelo
    def setModelo(self,modelo):
        self.modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad

    def getCaballaje(self):
        return self.caballaje
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje

    def getPlazas(self):
        return self.plazas
    def setPlazas(self,plazas):
        self.plazas=plazas
        

    #Metodos o acciones o funciones que hace el objeto.

    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
coche1=Coches("VW","Blanco","2022",220,150,5)
coche1.num_serie="B01234234A" 
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0) #No se puede dejar solo un atributo
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"


print(f"\n Coche1: \n marca: {coche1.getMarca()} \n color: {coche1.getColor()} \n modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n numero de serie: {coche1.num_serie}")

print(f"\n Coche1: \n marca: {coche2.getMarca()} \n color: {coche2.getColor()} \n modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()}")

print(f"\n Coche3: \n marca: {coche3.marca2}")

print(f"\n Coche4: \n marca: {coche4.marca2}")