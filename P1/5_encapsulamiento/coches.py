"""
1-no metodo constructor
2-que los atributos sean publicos
3-metodos acelerar y frenar no hagan nada (para que no haga nada se usa pass)
"""

import os

os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas

    #Primer forma
    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca

    #Segunda forma
    @property
    def marca2(self):
        return self.__marca
    @marca2.setter
    def marca2(self,marca):
        self.__marca=marca


    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getCaballaje(self):
        return self.__caballaje
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    def setPlazas(self,plazas):
        self.__plazas=plazas
        

    #Metodos o acciones o funciones que hace el objeto.

    def acelerar(self):
        return "Estas acelerando"
    
    def frenar(self):
        return "Estas frenando"


