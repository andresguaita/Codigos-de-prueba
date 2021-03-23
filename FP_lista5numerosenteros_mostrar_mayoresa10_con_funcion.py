#Confeccionar una función que cargue por teclado una lista de 5 enteros y
#la retorne. Una segunda función debe recibir una lista y mostrar
#todos los valores mayores a 10. Desde el bloque principal del
#programa llamar a ambas funciones.



def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


# bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)
