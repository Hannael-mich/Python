import math


def raiz_cubica (x):
    return x ** (1/3)

print("Raiz cubica de 27: ", raiz_cubica(27))

def area_circulo(r):
    return math.pi *(r ** 2)

print("Area de un circulo: ", area_circulo(5))

def conversionF_C (g):
    return (g - 32) * 5/9

print("La conversion de grados f a c es: ", conversionF_C(30))

def conversionC_F (g):
    return (g * (9/5))+32

print("La conversion de grados c a f es: ", conversionC_F(30))

def r_G(r):
    return r*(180 / math.pi)

print("La conversion de radianes a grados es: ", r_G(50))

def g_R(r):
    return (r * (math.pi/180))

print("La conversion de grados a radianes es: ", g_R(50))

