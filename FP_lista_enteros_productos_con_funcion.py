#Definir una lista de enteros por asignación en el bloque principal.
#Llamar a una función que reciba la lista y nos retorne
#el producto de todos sus elementos. Mostrar dicho producto en
#el bloque principal de nuestro programa.


def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod


# bloque principal

lista=[1, 2, 3, 4, 5]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",producto(lista))
