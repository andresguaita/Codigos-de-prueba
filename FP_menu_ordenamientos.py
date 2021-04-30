import os

listaDesordenada=[]

 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("\nSelecciona una opción")
	print ("\t1 - Almacenar datos"),print ("\t2 - Ordenamiento Burbuja"),print ("\t3 - Ordenamiento por isercion")
	print("\t4 - Ordenamiento shell"),print("\t5 - Salir")
	
 
def cargar_datos():

    for posVec in range (5):
        
                valor=float(input("Digite un valor : "))
               
                listaDesordenada.append(valor) 

def burbuja(vector):
    n = len(vector)
  
    # Recorre todos los elementos del vector
    for i in range(n-1):
      
        
        for j in range(0, n-i-1):
  
            #Recorrer el vector de 0 a n-i-1
            #Intercambiar si el elemento encontrado es mayor
            #que el siguiente elemento
            if vector[j] > vector[j+1] :
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector

def insercion(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
       #Mueve los elementos de arr [0..i-1], que son mayores que la "key",
       #a una posición por delante de su posición actual
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)


      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value
     

while True:
    menu()
    opcion=int(input("Ingrese una opcion segun el menu "))
    if opcion==1:
        cargar_datos()
        print(listaDesordenada)
        input("Has pulsado la opción 1...\npulsa enter para continuar")
    if opcion==2:        
        print(burbuja(listaDesordenada))
        input("Has pulsado la opción 2...\npulsa enter para continuar")
        
    if opcion==3:
        print(insercion(listaDesordenada))        
        input("Has pulsado la opción 3...\npulsa enter para continuar")
    if opcion==4:
        
        nlist=listaDesordenada
        shellSort(nlist)
        print(nlist)
        
        input("Has pulsado la opción 4...\npulsa enter para continuar")
    
    elif opcion==5:
        break
    elif opcion<1 or opcion>5:
    	print ("")
    	input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

     
        
        
        