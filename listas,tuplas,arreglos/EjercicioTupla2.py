tupla = ("", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", "p","q", "r"
         ,"s","t","u","v","W","x","y","z")




#print(tupla[3])

num = int(input("Ingrese un numero de acuerdo a las letras del abedario: "))

print(type(num))

if num < 26:
    print("La letra es {} de acuerdo al numero ingresado".format(tupla[num]))
else:
    print("El numero no se encuentra en el rango de las letras del alfabeto")