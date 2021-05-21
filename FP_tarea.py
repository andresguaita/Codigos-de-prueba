n = 0
m = 0
#tamaño de la matriz es n*m
matriz = []

n=int(input("Introduzca el numero de filas de la matriz "))
m=int(input("Introduzca el numero de columnas de la matriz "))

def cargar_datos():
    for i in range(n):
        matriz.append([])
        for j in range(m):
            k=int(input("Ingrese el valor de la matriz en fila %i y la columna %i \n"%(i,j)))
            matriz[i].append(k)
    return matriz

def sumar_filas():
    sumFila=0
    for f in range(n):
        for c in range (m):
            sumFila=sumFila+matriz[f][c]
    print("La suma de las filas son: ",sumFila)
    
def sumar_columnas():
    z=0
    r=0
    sumColumna=0
    t=m*n   
    for x in range (t):              
       sumColumna=sumColumna+matriz[z][r]
       z=z+1
       if(z==n):
            z=0
            r=r+1       
    print("La suma de las columnas es: ",sumColumna)
    
def sumar_fila_s():
    sumFila=0
    s=int(input("Ingrese la fila que desea sumar (0 a n) "))
    for f in range(n):
        for c in range (m):
            if(f==s):
                sumFila=sumFila+matriz[f][c]            
    print("La suma de las filas son: ",sumFila)
    
def sumar_columna_c():
    z=0
    r=0
    sumColumna=0
    t=m*n 
    c=int(input("Ingrese la columna que desea sumar (0 a m) "))
    for x in range (t): 
      if(r==c):        
            sumColumna=sumColumna+matriz[z][r]
      z=z+1
      if(z==n):
            z=0
            r=r+1       
    print("La suma de las columnas es: ",sumColumna)        
        
def sumar_pares():

    sumEleMat=0 
    sumEleI=0
    for f in range(n):
        for c in range(m):
            num=int(matriz[f][c])            
            if(num%2==0):
                sumEleMat=sumEleMat+matriz[f][c]
            else:
                sumEleI=sumEleI+matriz[f][c]                                                         
         
    print("La suma de los elementos pares es : ",sumEleMat)
    
def sumar_impares():

    sumEleMat=0 
    sumEleI=0
    for f in range(n):
        for c in range(m):
            num=int(matriz[f][c])            
            if(num%2==0):
                sumEleMat=sumEleMat+matriz[f][c]
            else:
                sumEleI=sumEleI+matriz[f][c]
    print("La suma de los impares son ",sumEleI)
                
def cuantos_pares_impares():

    sumEleMat=0 
    sumEleI=0
    p=0
    imp=0
    for f in range(n):
        for c in range(m):
            num=int(matriz[f][c])            
            if(num%2==0):
                sumEleMat=sumEleMat+matriz[f][c]
                p=p+1
                
            else:
                sumEleI=sumEleI+matriz[f][c]
                imp=imp+1                                              
         
    print("Los numeros pares en la matriz son : ",p)
    print("Los numero impares en la matriz son : ",imp)
    

def promedio_matriz():
    sumEleMat=0    
    t=n*m
    for f in range(n):
        for c in range(m):
            sumEleMat=sumEleMat+matriz[f][c]
    promM=sumEleMat/t
            
    print("El promedio de los numeros en la matriz es: ",promM)
    
def diagonal():
    sumD=0
    x=0
    f=0
    c=0
    while (x<m):
        sumD=sumD+matriz[f][c]
        x=x+1
        f=f+1
        c=c+1
    print(sumD)
    
                    
    
cargar_datos()
print(matriz)
diagonal()
sumar_filas()
sumar_fila_s()
sumar_columnas()
sumar_columna_c()
sumar_pares()
sumar_impares()
promedio_matriz()
cuantos_pares_impares()

        
    
          
    

