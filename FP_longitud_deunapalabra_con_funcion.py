#Confeccionar una función que le enviemos como parámetro un string y
#nos retorne la cantidad de caracteres que tiene.
#En el bloque principal solicitar la carga de dos nombres
#por teclado y llamar a la función dos veces.
#Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.



def largo(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")
