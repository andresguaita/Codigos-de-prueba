#  Programa que calcula el cuadro de los primeros 100 números

#  Area de declaración de variables
cuadradoNumero=0
acumuladorSuma=0
num=1

#  Entradas
cantidadNumeros=int(input("Cantidad de Números: "))
#  Procesos
#  Ciclo para de 1 hasta 100
for num in range(cantidadNumeros+1):
    cuadradoNumero=num*num
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("El cuadrado de : ", num, "es: ", cuadradoNumero)
    print("La suma acumulada es : ", acumuladorSuma)
#  Fin del ciclo

print("La suma de los cuadrados es: ", acumuladorSuma)
    
