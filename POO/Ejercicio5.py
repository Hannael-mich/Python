#Crear un programa con tres clases Universidad, con atributos nombre (Donde se 
#almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos 
#especialidad (En donde me guarda la especialidad de un estudiante). Una ultima 
#llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe 
#imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un 
#objeto llamado persona.


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre


class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.universidad = None
        self.carrera = None

    def agregar_universidad(self, universidad):
        self.universidad = universidad

    def agregar_carrera(self, carrera):
        self.carrera = carrera

    def imprimir_informacion(self):
        print("Nombre del estudiante:", self.nombre)
        print("Edad del estudiante:", self.edad)
        print("Especialidad:", self.carrera.especialidad)
        print("Universidad:", self.universidad.nombre)


# Crear objetos Universidad, Carrera y Estudiante
universidad = Universidad("Universidad Ejemplo")
carrera = Carrera("Ingeniería en Informática")
estudiante = Estudiante("Juan", 20)

# Asignar universidad y carrera al estudiante
estudiante.agregar_universidad(universidad)
estudiante.agregar_carrera(carrera)

# Imprimir la información del estudiante
estudiante.imprimir_informacion()

#Forma de como se hizo en Udemy

class Universidad():
    def __init__(self,Nombre):
        self.Nombre = Nombre

class Carerra():
    def carrera(self,especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad,Carerra):
    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}. Estudio en la Universidad {}".format(self.nombre,self.edad,self.especialidad, self.Nombre))

persona = Estudiante("Don Bosco")
persona.carrera("Sistemas")
persona.datos("Carlos", 20)