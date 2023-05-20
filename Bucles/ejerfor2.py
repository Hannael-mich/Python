num1 = int(input("ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero mayor al primero: "))

for i in range(num1,num2+1):
    if i % 2 == 0:
        continue
    print(i)