jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

usuario = int(input("Ingrese un numero de un jugador: "))

if jugadores.get(usuario) == None:
    print("Ese numero no se encuentra entre los jugadores")
else:
    print(jugadores.get(usuario))