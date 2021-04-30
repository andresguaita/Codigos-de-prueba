# Punto 3: Se desea obtener la nómina semanal —salario neto— de los N (Leídos por teclado) empleados   de una empresa, cuyo trabajo se paga por horas y del modo siguiente

# Se desea obtener la nómina semanal —salario neto— de los N 
#(Leídos por teclado) empleados   de una empresa, cuyo trabajo se paga por horas 
#y del modo siguiente:
    


def salario(h,t):
    
    if h>35:
        horas_extras= h-35
        salario= ((h-horas_extras)*t)+(horas_extras*1.5*t)
    else:
        salario= h*t  
    
    return salario

def salario_total():
    salario_n= salario(h,t)
    salario_n= salario_n - (salario_n*0.165)
    if 2000000 <= salario_n <= 3000000:
        salario_n= salario_n -(salario_n*0.05)
    elif 3000001 <= salario_n <= 4000000:
        salario_n = salario_n - (salario_n*0.07)  
    if 4000001 <= salario_n <= 5000000:
        salario_n = salario_n - (salario_n*0.09)
    if salario_n>5000000:
        salario_n= salario_n - (salario_n*0.11)
    if salario_n <2000000:
        print("Salario menor que el minimo\n" + "porque es menor que 2 millones\n")
    
    return salario_n

def imprimir_pago_detallado():
        print("-----------DESPRENDIBLE DE PAGO DETALLADO----------- ")
        print("Nombre: ",nombre )
        print("Genero : ",genero)
        print("Modulo : ", sesion)
        print("Numeros de horas trabajadas : ",h)
        print("Pago por hora trabajada : ",t)
        horas_extras= h-35
        print("Horas extra : ", horas_extras)
        pago_extra= horas_extras*1.5*t
        print("Pago por horas extras : ",pago_extra)
        salario1=salario(h,t)
        salario_neto=salario_total()
        descuento= salario1- salario_neto
        print("Descuento del salario es : ",descuento)
        print("Salario: ",salario_total())
        

# Programa principal
Numt=int(input("Ingrese numero de trabajadores :  "))

for x in range (Numt):
    nombre=str (input("Ingrese el nombre del trabajador  : "))
    genero=str (input("Ingrese F/M(Masculino-Femenino "))
    sesion=int(input("Ingrese numero de modulo 1,2 o 3  : ")) 
    h=float(input("Ingrese cantidad de horas trabajadas : "))
    t=float(input("Ingrese la tarifa por hora :  "))
    imprimir_pago_detallado()
    print(Numt)
    horas_totales=0
    horas_totales= h+horas_totales
    print(horas_totales)
    horas_extras=0
    horas_extraT= (h-35)+horas_extras
    horas_totales_con_extra= horas_totales+horas_extraT
    pagos_total= Numt*t
    pago_extra= horas_extraT*t
    pago_total_de_la_empresa=pagos_total+pago_extra
    cantH=0
    cantM=0
    if genero=='M' or genero=='m':
        cantH=cantH+1
    elif genero=='F' or genero=='f':
        cantM=cantM+1
    sesion1=0
    sesion2=0
    sesion3=0
    if sesion==1:
        sesion1=sesion1+1
    elif sesion==2:
        sesion2=sesion2+1
    else:
        sesion3=sesion3+1
print("El total de empleados de la empresa es ",Numt)
print("El total de horas trabajadas",h )
print("El total de horas extra : ",horas_extraT)
print("Cantidad de personas por sesion 1 ,2 y 3 respectivamente  : ",sesion1,sesion2,sesion3 )
print("Cantidad de generos, masculino y femenino , respectivamente  : ",cantH,cantM)
print("Cantidad de pagos de extras : ", pago_extra)
print("Cantidad de pagos sin horas extra : ",pagos_total)
print("Cantidad de pagos totales", pago_total_de_la_empresa)