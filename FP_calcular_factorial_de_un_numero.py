#Calcular los factoriales de un numero

Num= int(input("Ingrese por favor el numero que desea calcular el factorial: "))
factorial=1
for x in range(Num):
    factorial = factorial*(Num-x)

print("El factorial de ", Num , " es : ",factorial)
