lista = ['1','2','3','4','5','6']

def agregar():

    pal = input("Desea introducir un valor s para aceptar: ")
    while( pal == "s"):
        valor = input ("Agregar un valor: ")
        lista.append(valor)
        pal = input("Desea introducir un valor s para aceptar: ")
        
agregar()

print(lista)

def pares ():
    listpar = []
    for i in range(len(lista)):
    #for i in lista:
        print(type(i))
        if i % 2 == 0:
            listpar.append(i)
    print (listpar)

pares()



def impar ():
    listim = []
    for i in range(len(lista)):
        if (i % 2 != 0):
            listim.append(i)
    print (listim)

impar()
        


