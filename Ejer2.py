#Ejercicio 2

num = int(input("Introduzca un numero: "))

if num > 0:
    print("El numero entero es: ", num)
else:
    print ("El numero entero es: ",num*-1)

if num > 0:
    print("El valor absoluto de {} es: {}".format(num, num))
else:
    print("El valor absoluto de {} es: {}".format(num, abs(num)))
