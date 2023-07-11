
def DNI(x):
    dic = {"T":0, "R":1, "W":2, "A":3, "G":4, "M":5, "Y":6, "F":7, "P":8, "D":9, 
           "X":10, "B":11, "N":12, "J":13, "Z":14, "S":15, "Q":16, "V":17, "H":18,
             "L":19, "C":20, "K":21, "E":22}
    
    dicci = dic
    
    return dicci[x]


letra = input("Introduzca una Letra Mayuscula: ")

print("La letra indroducida fue: ", DNI(letra))

def DNI(x):
    dic = {"0":"T", "1":"R", "2":"W", "3":"A", "4":"G", "5":"M", "6":"Y", "7":"F", "8":"P", "9":"D", 
           "10":"X", "11":"B", "12":"N", "13":"J", "14":"Z", "15":"S", "16":"Q", "17":"V", "18":"V",
             "19":"L", "20":"C", "21":"K", "22":"E"}
    
    dicci = dic
    
    return dicci[x]

letra = input("Introduzca un numero entre 0-22: ")

print("El numero introducido da la letra: ", DNI(letra))


print("------------------------------------")

#Segundo programa
def primeMayu(x):
    abec= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for i in abec:
        if x == i:
            print("Si es mayuscula")
            break
        if i == "Z":
            if x == "Z":
                print("Si es mayuscula")
            else:
                print("No es mayuscula")
    
palabra = input("Introduzca una palabra: ")

primeMayu(palabra[0])

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        break
    except:
        print("Ingrese un valor que sea correcto")
    finally:
        print("Ha finalizado")



