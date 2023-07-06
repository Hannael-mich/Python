class Coche:
    """Esta clase define el estado y el comportamiento de un coche"""
    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad = self.velocidad +self.aceleracion
        print("Hola")

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

c1 = Coche('rojo', 20) 
print(c1.color)

print(c1.ruedas)
c2 = Coche('azul', 30)
print(c2.color)
print(c2.ruedas)
4

print(c1.aceleracion)
print("La velocidad de c2 es: ",c2.velocidad)
Coche.acelera(c1)
c1.acelera()