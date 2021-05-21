import os

listaNotas=[]
sumaNotas = 0.0
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
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("\nSelecciona una opción")
	print ("\t1 - Almacenar datos"),print ("\t2 - Sumar datos"), ("\t3 - Promedio de los datos")
	print("\t4 - Numero menor de los datos"),print("\t5 - Numero mayor de los datos"),print("\t6 Aprobados y Reprobados"),print("\t7 Rango de notas")
	print ("\t8 - Salir")
 
 
while True:
    menu()
    opcion=int(input("Ingrese una opcion segun el menu "))
    if opcion==1:
        for posVec in range (5):
    
            notaEstudiante=float(input("Digite nota : "))
           
            listaNotas.append(notaEstudiante)
        print(listaNotas)
        input("Has pulsado la opción 1...\npulsa enter para continuar")
    if opcion==2:
        for x in range (len( listaNotas)):
            sumaNotas=sumaNotas+listaNotas[x]
        print("Suma : ",sumaNotas)
        input("Has pulsado la opción 2...\npulsa enter para continuar")
    if opcion==3:
        promedio=sumaNotas/len(listaNotas)
        print("El promedio de notas es  : ", promedio)
        input("Has pulsado la opción 3...\npulsa enter para continuar")
    if opcion==4:
        for x in range(len(listaNotas)):
            if listaNotas[x]<Nmenor:
                Nmenor= listaNotas[x]
                posicionMenor= x
        print("La nota menor es : ", Nmenor)
        print("Y esta en la posicion : " , posicionMenor)
        input("Has pulsado la opción 4...\npulsa enter para continuar")
    if opcion==5:
        for x in range(len(listaNotas)):
            if listaNotas[x]>Nmayor:
                Nmayor= listaNotas[x]
                posicionMayor= x
        print("La nota mayor es : ",Nmayor)
        print("Y esta en la posicion : ",posicionMayor)
        input("Has pulsado la opción 5...\npulsa enter para continuar")
    if opcion==6:
        for x in range(len(listaNotas)):
            if listaNotas[x]>=3.5:
                Aprobaron= Aprobaron + 1
                
            else:
                Reprobaron=Reprobaron +1
        print("El numero de alumnos aprobados es : " , Aprobaron)
        print("El numero de alumnos reprobados es : " , Reprobaron)
        input("Has pulsado la opción 6...\npulsa enter para continuar")
    if opcion==7:
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
        print("El numero de almunos entre 0 y 1 es : ",Rang1)
        print("El numero de almunos entre 1.1 y 2 es : ",Rang2)
        print("El numero de almunos entre 2.1 y 3 es : ",Rang3)
        print("El numero de almunos entre 3.1 y 4 es : ",Rang4)
        print("El numero de almunos entre 4.1 y 5 es : ",Rang5)
        input("Has pulsado la opción 7...\npulsa enter para continuar")
    
    elif opcion==8:
        break
    elif opcion<1 or opcion>8:
    	print ("")
    	input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

     
        
        
        