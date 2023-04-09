tupla = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
"octubre", "noviembre", "diciembre")

#print(type(tupla))

#print(tupla[3])

num = int(input("Ingrese un numero de acuerdo a algun mes del año: "))

#print(type(num))

if num < 12:
    print("El mes del año que es {} de acuerdo al numero ingresado".format(tupla[num]))
else:
    print("El numero no se encuentra en el rango de los meses del año")