import random



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
    
  

vector = []
for x in range (10):
    r= random.randint(1, 20)
    vector.append(r)
  
print("El vector sin ordenar es : ",vector)
print("El victor ordenado es : ",burbuja(vector))




