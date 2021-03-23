#  Librerías usadas en el programa
import random

#  Leer N, generar aleatorios y calcular suma y promedio

#  Area de definición de variables
cantidadNumeros=0
contadorRepeticionesWhile=0
numero=0
acumuladorSuma=0
promedioNumerosAleatorios=0.0

# Variables segunda parte del ejercicio
acumuladorPositivos=0
acumuladorNegativos=0
contadorPositivos=0
contadorNegativos=0
promedioPositivos=0.0
promedioNegativos=0.0

#  Variable tercera parte del ejercicio
mayorPositivo=0
mayorNegativo=0
menorPositivo=1000
menorNegativo=0


# Entradas
cantidadNumeros=int(input("Cantidad de Números: "))

#Procesos
#Ciclo While
while contadorRepeticionesWhile<cantidadNumeros:
    numero=random.randint(-1000,1000)
    acumuladorSuma=acumuladorSuma+numero
    #  Segunda parte del ejercicio 
    if numero>0:  # Cálculo para números positivos
        print("Número Positivo: ",numero)
        acumuladorPositivos=acumuladorPositivos+numero
        contadorPositivos=contadorPositivos+1
        #  Tercera parte del ejercicio
        #  Identificar el mayor de los positivos
        if numero>mayorPositivo:
            mayorPositivo=numero
            
        #  Identifcar el menor de los positivos
        if numero<menorPositivo:
            menorPositivo=numero
        #  Fin Tercera parte del ejercicio                
            
    else:# Cálculo para números negativos
        print("Número Negativo: ",numero)
        acumuladorNegativos=acumuladorNegativos+numero
        contadorNegativos=contadorNegativos+1
    # Fin de la sengunda parte del ejercicio    
    contadorRepeticionesWhile=contadorRepeticionesWhile+1
# Fin del ciclo
#  Cálculo de los promedios      
promedioNumerosAleatorios=acumuladorSuma/contadorRepeticionesWhile
promedioPositivos=acumuladorPositivos/contadorPositivos  
promedioNegativos=acumuladorNegativos/contadorNegativos

# Salidas de todos los números
print("Suma de Numeros Aleatorios: ", acumuladorSuma)   
print("Promedio de Numeros Aleatorios: ", promedioNumerosAleatorios)   
 
# Salidas de todos los números positivos
print("Cantidad Números Positivos: ",contadorPositivos)
print("Suma de Numeros Positivos: ", acumuladorPositivos)   
print("Promedio de Numeros Positivos: ", promedioPositivos)   
    
# Salidas de todos los números negativos
print("Cantidad Números Negativos: ",contadorNegativos)
print("Suma de Numeros Negativos: ", acumuladorNegativos)   
print("Promedio de Numeros Negativos: ", promedioNegativos)   
    
#  Imprimir mayor de los positivos y menor de los positivos
print("Mayor de los positivos: ", mayorPositivo)   
print("Menor de los Positivos: ", menorPositivo)   
