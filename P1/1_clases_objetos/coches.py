"""
1-no metodo constructor
2-que los atributos sean publicos
3-metodos acelerar y frenar no hagan nada (para que no haga nada se usa pass)
"""

import os

os.system("cls")

class Coches:
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
coche1=Coches()
coche1.marca="VWW"
coche1.color="Blanca"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"\n Coche1: \n marca: {coche1.marca} \n color: {coche1.color} \n modelo: {coche1.modelo} \n velocidad: {coche1.velocidad} \n caballaje {coche1.caballaje} \n plazas: {coche1.plazas}")

coche2=Coches()
coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"\n Coche2: \n marca: {coche2.marca} \n color: {coche2.color} \n modelo: {coche2.modelo} \n velocidad: {coche2.velocidad} \n caballaje {coche2.caballaje} \n plazas: {coche2.plazas}")