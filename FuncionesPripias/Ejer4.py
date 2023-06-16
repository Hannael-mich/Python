def total ():
    monto = float(input("Ingrese una cantidad: "))
    iva = float(input("Ingrese una cantidad para el iva: "))

    print (monto)
    print(iva)
    print (type(iva))

    if iva != 0:
        if iva != " ":
            totalpagar = (monto * iva) + monto
            print (totalpagar)
            return totalpagar
    else:
        totalpagar = (monto * 0.21) + monto
        print (totalpagar)
        return totalpagar
    
print("La cantidad total a pagar: ", total())