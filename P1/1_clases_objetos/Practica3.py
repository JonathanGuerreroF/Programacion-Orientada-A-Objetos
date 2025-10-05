import os

os.system("cls")

class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def get_nombre_privado(self):
        return self.__nombre
    
    def set_nombre_privado(self, nombre_privado):
        self.__nombre = nombre_privado

    def get_edad_privado(self):
        return self.__edad
    
    def set_edad_privado(self, edad_privado):
        self.__edad = edad_privado

    def get_matricula_privado(self):
        return self.__matricula
    
    def set_matricula_privado(self, matricula_privado):
        self.__matricula = matricula_privado

    def inscribirse(self):
        pass

    def estudiar(self):
        pass

alumno1=Alumnos("Ana",18,"3241240145")
print(f"\n Alumno 1 \n nombre: {alumno1.get_nombre_privado()} \n edad: {alumno1.get_edad_privado()}  \n matricula: {alumno1.get_matricula_privado()}")
alumno2=Alumnos("Paola",18,"25879123")
print(f"\n Alumno 2 \n nombre: {alumno2.get_nombre_privado()} \n edad: {alumno2.get_edad_privado()}  \n matricula: {alumno2.get_matricula_privado()}")

class Profesores:
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def get_nombre_privado(self):
        return self.__nombre
    
    def set_nombre_privado(self, nombre_privado):
        self.__nombre = nombre_privado

    def get_experiencia_privado(self):
        return self.__experiencia
    
    def set_experiencia_privado(self, experiencia_privado):
        self.__experiencia = experiencia_privado

    def get_num_profesores_privado(self):
        return self.__num_profesor
    
    def set_num_profesores_privado(self, num_privado):
        self.__num_profesor = num_privado

    def impartir(self):
        pass
    
    def evaluar(self):
        pass

maestro1=Profesores("Efrain",20,"6187651234")
print(f"\n Profesor 1 \n nombre: {maestro1.get_nombre_privado()} \n experiencia: {maestro1.get_experiencia_privado()} \n numero: {maestro1.get_num_profesores_privado()}")
maestro2=Profesores("Ervey",5,"6181237654")
print(f"\n Profesor 2 \n nombre: {maestro2.get_nombre_privado()} \n experiencia: {maestro2.get_experiencia_privado()} \n numero: {maestro2.get_num_profesores_privado()}")

class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def get_nombre_privado(self):
        return self.__nombre
    
    def set_nombre_privado(self, nombre_privado):
        self.__nombre = nombre_privado

    def get_codigo_privado(self):
        return self.__codigo
    
    def set_codigo_privado(self, codigo_privado):
        self.__codigo = codigo_privado

    def get_creditos_privado(self):
        return self.__creditos
    
    def set_atributo_privado(self, creditos_privado):
        self.__codigo = creditos_privado

    def asignar(self):
        pass

curso1=Cursos("Programacion","4321",7)
print(F"\n Curso 1 \n nombre:{curso1.get_nombre_privado()} \n codigo: {curso1.get_codigo_privado()} \n creditos: {curso1.get_creditos_privado()}")
curso2=Cursos("Ingles","1234",7)
print(F"\n Curso 2 \n nombre:{curso2.get_nombre_privado()} \n codigo: {curso2.get_codigo_privado()} \n creditos: {curso2.get_creditos_privado()}")