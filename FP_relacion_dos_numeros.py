#Realiza una función llamada relacion(a, b)
#que a partir de dos números cumpla lo siguiente:

#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.

def relacion (a,b):
    if a>b:
        print("1")
    elif a<b:
        print("-1")
    else:
        print("0")

a= int(input("Ingrese primer numero "))
b= int(input("Ingrese segundo numero "))

relacion(a,b)


        
    
