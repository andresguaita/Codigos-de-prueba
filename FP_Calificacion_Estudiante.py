## Nombre de un estudiante ,Leer las notas de los tres parciales, el acumulado de inasistencia y calcular 
## La nota definitiva sabiendo que PP tiene un porcentaje del 35% , SP tiene % del 35 % y el restante 30% es para el TP .
## Imprimir la nota definitiva mas un concepto:
## Gano academicamente    fallas < 12 y Nota definitiva >=3
## Perdio academicamente  fallas <12 y Nota definitiva <3
## Perdio por inasistencia fallas >12 y nota definitiva no importa, se divide por la mitad
## Perdio academicamente y por inasistencia Fallas >12 y Nota definitiva <3 

PP=float(input("Ingrese nota primer parcial "))
SP=float(input("Ingrese nota segundo parcial "))
TP=float(input("Ingrese nota tercer parcial "))
IN=int(input("Ingrese numero de insasistencias "))

PP = (PP*35)/5
SP = (SP*35)/5
TP = (TP*30)/5

nota_def = (PP + SP + TP)
nota_def = (nota_def*5)/100 


if IN > 12 and nota_def < 3:
    print("Perdio academicamente y por inasistencia")
    
elif IN < 12 and nota_def>= 3:
    print("Gano academicamente")

else:

    if IN < 12 and nota_def < 3:
        print("Perdio academicamente")

    else :
        nota_def= nota_def/2
        print("La nota definitiva es :", nota_def)
        print("Perdio por inasistencia")

