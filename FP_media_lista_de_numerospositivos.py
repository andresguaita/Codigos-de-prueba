# Determinar la media de una lista indefinida de números positivos,
#terminando con un número negativo.

contador=0
SumNum=0
Media=0
fin=1

while fin>0:

    Num=int(input("Ingrese el numero : "))
    if Num>0:
        SumNum= SumNum+Num
        contador= contador +1
    else:
        fin=-1
    
Media= SumNum/contador
print("La media en esta lista de numeros es : ", Media)



    
        
    
