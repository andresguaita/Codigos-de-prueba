#Desarrollar un programa con dos funciones.
#La primer solicite el ingreso de un entero y
#muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores
#y muestre el producto de los mismos.
#LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    Num=int(input("Introduzca el numero del que desea calcular el cuadrado "))
    print(pow(Num,2))

def producto():
    Num1=int(input("Ingrese un numero "))
    Num2=int(input("Ingrese un numero "))
    print(Num1*Num2)

# Programa principal

cuadrado()
producto()
