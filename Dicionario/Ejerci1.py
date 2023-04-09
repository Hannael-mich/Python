paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador",
           "Honduras": "Honduras","Nicaragua": "Managua", 
           "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
           "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

#print (paises.get(paisUsuario))
#Primera Solucion 
'''if paises.get(paisUsuario) == None :
    print("El nombre del pais solicitado no se encuentra")
else:
    print ("La capital del pais es: ",paises.get(paisUsuario))'''

pais = input ('Ingrese un pais para conocer su capital: ')
letra = pais.title() in paises

print (pais.title())


if letra == True:
    print(paises[pais.title()])
else:
    print("No se encuentra ese pais")