#Desarrollar un programa con dos funciones. La primer solicite
#el ingreso de un entero y muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores y muestre
#el producto de los mismos. LLamar desde el bloque del programa principal
#a ambas funciones.


def calcular_cuadrado(valor):
    cuadrado=valor*valor
    return cuadrado


def calcular_producto(valor1,valor2):
    producto=valor1*valor2
    return producto


# Programa principal

valor=int(input("Ingrese un entero:"))
print("El cuadrado es: ",calcular_cuadrado(valor))
valor1=int(input("Ingrese primer valor:"))
valor2=int(input("Ingrese segundo valor:"))
print("El producto es: ",calcular_producto(valor1,valor2))
