#  Programa que calcula el cuadro de los primeros 100 números

#  Area de declaración de variables
cuadradoNumero=0
acumuladorSuma=0
num=1
contador=1

#  Entradas
cantidadNumeros=int(input("Cantidad de Números: "))
#  Procesos
#  Ciclo para de 1 hasta 100
while contador<=cantidadNumeros:
    cuadradoNumero= pow(contador,2)
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("El cuadrado de : ", contador, "es: ", cuadradoNumero)
    print("La suma acumulada es : ", acumuladorSuma)
    contador=contador+1
#  Fin del ciclo

print("La suma de los cuadrados es: ", acumuladorSuma)
    
