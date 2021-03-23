#Calcular combinatoria

def combinatoria(x,y):
    combi= factorial(x)/factorial(y)*factorial(x-y)
    return combi

def factorial(Num):
    factor=1
    for x in range (Num):
        factor = factor*(Num-x)
    return factor

Num1=int(input("Ingrese el primer numero "))
Num2=int(input("Ingrese el segundo numero "))
print(factorial(Num1))
print(factorial(Num2))
print(combinatoria(Num1,Num2))
