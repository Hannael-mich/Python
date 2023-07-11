num = int(input("Introducir un numero entero positivo"))

def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

print ("EL factorial del numero {} es {} ".format((num),factorial(num)) )  