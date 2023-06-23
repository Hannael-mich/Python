import math

def areaCuadrado(lado1, lado2):
    area = lado1 * lado2
    return area

def areaCirculo(radio):
    area = math.pi * radio**2
    return area

lad = int(input("Introduce el primer lado: "))
lad1 = int(input("Introduce el segundo lado: "))
radio1 = float(input("Introduce el radio del circulo : "))

print(areaCuadrado(lad, lad1))
print(areaCirculo(radio1))
