#Ejercicio 1

letra = input("Introduce una letra: ")

if letra.lower() == "a":
    print("Esta vocal es la A")
elif letra.lower() == "e":
    print("Esta vocal es la E")
elif letra.lower() == "i":
    print("Esta vocal es la I")
elif letra.lower() == "o":
    print("Esta vocal es la O")
elif letra.lower() == "u":
    print("Esta vocal es la U")
else:
    print ("No es vocal")

#Forma corta para detectar una vocal

if letra.lower() in "aeiou":
    print("Es una vocal, forma corta")
else:
    print("No es una vocal, forma corta")
 