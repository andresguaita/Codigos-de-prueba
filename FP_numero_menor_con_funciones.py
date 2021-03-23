#Desarrollar un programa que solicite la carga
#de tres valores y muestre el menor.
#Desde el bloque principal del programa llamar 2 veces a dicha función
#(sin utilizar una estructura repetitiva)

def numero_menor():
    Num1=int(input("Ingrese primer numero :"))
    Num2=int(input("Ingrese segundo numero :"))
    Num3=int(input("Ingrese tercer numero :"))    
    print("Menor de los tres")
    if Num1<Num2 and Num1<Num3:
        print(Num1)
    else:
        if Num2<Num3:
            print(Num2)
        else:
            print(Num3)

numero_menor()
numero_menor()
