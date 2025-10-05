from coches import *
import os

os.system("cls")
#Solicitar datos que posteriormente seran los atrbituos del objeto

num_coches=int(input("¿Cuantos coches tienes?"))

for i in range(0,num_coches):
    print(f"\n...Datos del automovil # {i+1}...")
    marca=input("Ingresar la marca: ").upper()
    color=input("Ingrear el color: ").upper()
    modelo=input("Ingresar el modelo: ").upper()
    velocidad=int(input("Ingresar la velocidad: "))
    caballaje=int(input("Ingresar la potencia: "))
    plazas=int(input("Ingresar el # de plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,caballaje,plazas)

    print(f"\n Coche: \n marca: {coche1.getMarca()} \n color: {coche1.getColor()} \n modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")


"""coche1=Coches("VW","Blanco","2022",220,150,5)
coche1.num_serie="B01234234A" 
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0) #No se puede dejar solo un atributo
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"


print(f"\n Coche1: \n marca: {coche1.getMarca()} \n color: {coche1.getColor()} \n modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n numero de serie: {coche1.num_serie}")

print(f"\n Coche1: \n marca: {coche2.getMarca()} \n color: {coche2.getColor()} \n modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()}")

print(f"\n Coche3: \n marca: {coche3.marca2}")

print(f"\n Coche4: \n marca: {coche4.marca2}")"""