
#Notas de curso de programacion

print("SISTEMA DE NOTAS DE UN CURSO DE PROGRAMACIÓN")

#Entrada

numeroEstudiantes=int(input("Digite la cantidad de estudiantes del grupo : "))

# Declarar la variable que controla el ciclo
contadorRepeteciones = 0
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0
sumaDefinitivaEstudiantes=0.0
sumaDefinitivaEstudiantesAprobaron=0.0
sumaDefinitivaEstudiantesReprobaron=0.0
promedioDefinitivaEstudiantes=0.0
promedioDefinitivaEstudiantesAprobaron=0.0
promedioDefinitivaEstudiantesReprobaron=0.0
#Proceso
#  Iniciar el ciclo

while contadorRepeteciones < numeroEstudiantes:
    #  Lectura de las notas de cada estudiante
    nombreEstudiante   = input("Digite nombre del estudiante : ")
    notaUnoEstudiante  = float(input("Digite la nota del primer parcial del estudiante : "))
    notaDosEstudiante  = float(input("Digite la nota del segundo parcial del estudiante : "))
    notaTresEstudiante = float(input("Digite la nota del tercer parcial del estudiante : "))
    #  Calcular la definitiva de cada estudiante
    notaDefinitiva = (notaUnoEstudiante+notaDosEstudiante+notaTresEstudiante)/3
    #Sumar las definitivas de los estudiantes para calcular el promedio
    sumaDefinitivaEstudiantes=sumaDefinitivaEstudiantes+notaDefinitiva
    print("1.  La definitiva es: ", notaDefinitiva)
    
    if(notaDefinitiva>=3.0):
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        #  Sumar las notas de los estudiantes que aprobaron
        sumaDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron+notaDefinitiva
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        #  Sumar las notas de los estudiantes que reprobaron
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+notaDefinitiva
    #  Incrementar la variable que controla el ciclo
    contadorRepeteciones = contadorRepeteciones+1
    
    #  Fin del ciclo
# Calcular el promedio del grupo
    
promedioDefinitivaEstudiantes=sumaDefinitivaEstudiantes/numeroEstudiantes   

if (cantidadEstudiantesAprobaron>0):
    promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/cantidadEstudiantesAprobaron 
if (cantidadEstudiantesReprobaron>0):
    promedioDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron/cantidadEstudiantesReprobaron 

print("OTROS CALCULOS")
print("2.  Cantidad de estudiantes que aprobaron : ", cantidadEstudiantesAprobaron)
print("3.  Cantidad de estudiantes que reprobaron : ", cantidadEstudiantesReprobaron)
print(f"4.  Promedio del grupo : {promedioDefinitivaEstudiantes:.2f}")
print("5.  Promedio de estudiantes que aprobaron : ", promedioDefinitivaEstudiantesAprobaron)
print(f"6.  Promedio de estudiantes que reprobaron :{promedioDefinitivaEstudiantesReprobaron:.1f} ")
