#Realizar un programa en el cual se declaren dos valores enteros por teclado 
#utilizando el método __init__. Calcular después la suma, resta, multiplicación y 
#división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
#Llamar a la clase Calculadora.


class Calculadora():
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def suma(self):
        sum = self.valor1 +self.valor2
        print("El valor de la suma de {} con {} es:"
              .format(self.valor1, self.valor2), sum)
        
    def resta(self):
        rest = self.valor1 -self.valor2
        print("El valor de la resta de {} con {} es:"
              .format(self.valor1, self.valor2), rest)
    
    def multiplicacion(self):
        mult = self.valor1 *self.valor2
        print("El valor de la multiplicacion de {} con {} es:"
              .format(self.valor1, self.valor2), mult)


    def divicion(self):
        div = self.valor1 /self.valor2
        print("El valor de la divicion de {} con {} es:"
              .format(self.valor1, self.valor2), div)

valor1 = int(input("Ingrese un valor entero: "))
valor2 = int(input("Ingrese un segundo valor entero: "))

valores = Calculadora(valor1, valor2)

valores.suma()
valores.resta()
valores.multiplicacion()
valores.divicion()

#Forma como se realizo el programa en udemy
class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el Primer Valor: "))
        self.num2 = int(input("Ingrese el Segundo Valor: "))
    
    def suma(self):
        self.suma = self.num1 + self.num2
        print( "La suma da como resultado: ",self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print("La resta da como resultado: ",self.resta)

    def multi(self):
        self.multi = self.num1 * self.num2
        return "La multiplicacion da como resultado: ",self.multi

    def division(self):
        self.division = self.num1 / self.num2
        return "La division da como resultado: ",self.division

calcular = Calculadora()
calcular.suma()
calcular.resta()
print(calcular.multi())
print(calcular.division())