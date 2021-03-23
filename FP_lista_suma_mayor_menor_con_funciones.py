#Definir por asignación una lista de enteros en el bloque principal del programa.
#Elaborar tres funciones, la primera recibe la lista y retorna la suma de
#todos sus elementos, la segunda recibe la lista y retorna el mayor
#valor y la última recibe la lista y retorna el menor.




def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))
