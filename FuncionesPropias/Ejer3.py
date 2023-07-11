var1 = int(input("Introduzca un primer valor: "))
var2 = int(input("Introduzca un segundo valor: "))

def determinacion():
    if var1 > var2:
        print ("El primer valor es mayor al segundo")
        return 1
    elif var1 < var2:
        print ("El primer valor es menor al segundo")
        return -1
    else:
        print ("Los dos valores son iguales")
        return 0
    

print(determinacion())
