# Imprimir las treinta primeras potencias de 10, es decir,
#10 elevado a 1, 10 elevado a 2, etc.
#además sumar las potencias calculadas

pot= 0
contador=0
SumaP=0

while contador<31:
    pot=10**contador
    SumaP= SumaP+pot
    print("La potencia de 10 a la ", contador ,"es: ",pot)
    contador= contador+1

print("La suma de todas las potencias es : ",SumaP)

