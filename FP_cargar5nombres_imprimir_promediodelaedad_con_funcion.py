#Desarrollar un programa que permita cargar 5 nombres de personas y
#sus edades respectivas. Luego de realizar la carga por teclado de todos
#los datos imprimir los nombres de las personas mayores de edad
#(mayores o iguales a 18 años)
#Imprimir la edad promedio de las personas.

def cargar_datos():
    nom=[]
    ed=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nom.append(v1)
        v2=int(input("Ingrese la edad:"))
        ed.append(v2)
    return [nom,ed]


def mayores_edad(nom,ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):
        if ed[x]>=18:
            print(nom[x])


def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("Edad promedio de las personas:",promedio)
    

# bloque principal

nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades) 
