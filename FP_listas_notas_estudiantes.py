# Declarar la estructura tipo lista vacia

listaNotas=[]
Nmenor=5
Nmayor=0
posicionMenor=0
posicionMayor=0
Aprobaron=0
Reprobaron=0
Rang1=0
Rang2=0
Rang3=0
Rang4=0
Rang5=0


# Almacenar datos en la lista

for posVec in range (5):
    # Leemos la nota de un estudiante 
    notaEstudiante=float(input("Digite nota : "))
    # Adicionamos la nota a la lista 
    listaNotas.append(notaEstudiante)
    

#Imprimir la lista 
print(listaNotas)


# Declarar una variable para almacenar la suma 
sumaNotas = 0.0

# Recorrer el arreglo e ir acumulando en la variable

for x in range (len( listaNotas)):
    sumaNotas=sumaNotas+listaNotas[x]

#Suma Notas

print("Suma : ",sumaNotas)

#Calculo del promedio

promedio=sumaNotas/len(listaNotas)

#Imprimir el promedio

print("El promedio de notas es  : ", promedio)

#Numero Menor y posicion

for x in range(len(listaNotas)):
    if listaNotas[x]<Nmenor:
        Nmenor= listaNotas[x]
        posicionMenor= x
        
#Numero Mayor y posicion
    
for x in range(len(listaNotas)):
    if listaNotas[x]>Nmayor:
        Nmayor= listaNotas[x]
        posicionMayor= x

#Calculo Aprobados y Reprobados

for x in range(len(listaNotas)):
    if listaNotas[x]>=3.5:
        Aprobaron= Aprobaron + 1
        
    else:
        Reprobaron=Reprobaron +1


#Rango de notas

for x in range(len(listaNotas)):
    if 0 <= listaNotas[x] <= 1:
        Rang1= Rang1+1
    if 1.1 <= listaNotas[x] <= 2:
        Rang2= Rang2+1
    if 2.1 <= listaNotas[x] <= 3:
        Rang3= Rang3+1
    if 3.1 <= listaNotas[x] <= 4:
        Rang4= Rang4+1
    if 4.1 <= listaNotas[x] <= 5:
        Rang5= Rang5+1
      
#Imprimir Variables
        
print("La nota mayor es : ",Nmayor)
print("Y esta en la posicion : ",posicionMayor)
print("La nota menor es : ", Nmenor)
print("Y esta en la posicion : " , posicionMenor)
print("El numero de alumnos aprobados son : " , Aprobaron)
print("El numero de alumnos reprobados son : " , Reprobaron)
print("El numero de almunos entre 0 y 1 es : ",Rang1)
print("El numero de almunos entre 1.1 y 2 es : ",Rang2)
print("El numero de almunos entre 2.1 y 3 es : ",Rang3)
print("El numero de almunos entre 3.1 y 4 es : ",Rang4)
print("El numero de almunos entre 4.1 y 5 es : ",Rang5)


