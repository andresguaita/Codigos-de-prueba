#  Ciclo While
#  Declaración de Variables
cantidadNumeros=0
contadorRepeticiones=1
cuadradoNumero=0
acumuladorSuma=0


#  Entradas
cantidadNumeros=int(input("Cantidad de Números: "))
# Procesos
while contadorRepeticiones<=cantidadNumeros:
    cuadradoNumero=pow(contadorRepeticiones,2)
    acumuladorSuma=acumuladorSuma+cuadradoNumero
    print("El cuadrado de : ", contadorRepeticiones, "es: ", cuadradoNumero)
    print("La suma acumulada es : ", acumuladorSuma)
    contadorRepeticiones=contadorRepeticiones+1
#  Fin While

#Salida    .
print("La suma de los cuadrados es: ",acumuladorSuma)    

    