#Realizar un programa que conste de una clase llamada Estudiante, que tenga como
#  atributos el nombre y la nota del estudiante. Definir los métodos para 
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
# de la nota y si ha aprobado o no.

#Ejercicio realizado por Fernando H
class Estudiante():
    def __init__(self, nombre, nota) :

        self.nombre = nombre
        self.nota = nota

    def nom(self):
        return self.nombre

    def note(self):
        return self.nota

    def aproRepro(self):
        if self.nota < 5:
            print("El estudiante ha reprobado:")
        else:
            print("El estudiante ha aprobado")


alumno = Estudiante("Pedro",9.5)

print("El nombre del estudiante es: ",alumno.nom())
print("La nota del estudiante fue de: ",alumno.note())
alumno.aproRepro()
    
#Forma en como se hizo en udemy

class Estudiante():
    def __init__(self , nombre , nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre , self.nota))
    
    def resultados(self):
        if self.nota < 7:
            print("Has REPROBADO!")
        else:
            print("Has APROBADO!")

estudiante1 = Estudiante("Daniel" , 6)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Karla" , 5)
estudiante2.imprimir()
estudiante2.resultados()