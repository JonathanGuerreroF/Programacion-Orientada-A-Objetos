from coches import *
import os

os.system("cls")
#Solicitar datos que posteriormente seran los atrbituos del objeto

"""num_coches=int(input("¿Cuantos coches tienes? "))

for i in range(0,num_coches):
    print(f"\n...Datos del automovil # {i+1}...")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingrear el color: ").upper()
    modelo=input("Ingresar el modelo: ").upper()
    velocidad=int(input("Ingresar la velocidad: "))
    caballaje=int(input("Ingresar la potencia: "))
    plazas=int(input("Ingresar el # de plazas: "))

    coche=Coches(marca,color,modelo,velocidad,caballaje,plazas)

    print(f"\n Coche: \n marca: {coche.marca} \n color: {coche.color} \n modelo: {coche.modelo} \n velocidad: {coche.velocidad} \n caballaje {coche.caballaje} \n plazas: {coche.plazas}")"""

coche=Coches("VW","blanco","2020",200,180,4)
print(coche.color,coche.acelerar())

camion=Camiones("VW","Blanco a perlado","2020",220,180,4,2,2500)
print(camion.color,camion.acelerar())

camioneta=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
print(camioneta.color,camioneta.acelerar())