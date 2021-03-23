#Dado el nombre de un mes y si el año es o no bisiesto,
#deducir el número de días del mes.

mes= str(input("Ingrese el mes "))
an=int(input("Ingrese el año "))


if mes=='febrero':
       if (an%100) == 0 and (an%400) == 0:
           print("El mes de ",mes, "tiene 29 dias")
       else:
           print("El mes de ",mes, "tiene 28 dias")

elif(mes=='abril' or mes=='junio' or mes=='septiembre' or mes=='noviembre'):
         print("El mes de ",mes, "tiene 30 dias")
else:
    print("El mes de ",mes, "tiene 31 dias")
