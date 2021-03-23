# Imprimir las treinta primeras potencias de 10, es decir,
#10 elevado a 1, 10 elevado a 2, etc.
#además sumar las potencias calculadas

pot= 0
contador=0
SumaP=0

for x in range (0,31,1):
    pot=10**x
    SumaP= SumaP+pot
    print("La potencia de 10 a la ", x ,"es: ",pot)

print("La suma de todas las potencias es : ",SumaP)


