# Lectura de archivos tipo excel 
# Importar librerías
import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd 

archivoExcel = pd.read_excel('departamentos.xlsx')
n_dep= archivoExcel['Departamento']
pob=archivoExcel['Poblacion']
area=archivoExcel['Area']


def area_col():
    total_area= archivoExcel['Area'].sum()
    return total_area
    
def prom_pers_d():

    total_p=archivoExcel['Poblacion'].sum()
    prom_p=total_p/len(n_dep)
    return prom_p


def prom_area_d():

    prom_d=area_col()/len(n_dep)
    return prom_d



def numero_mayor():
    d_mayor=0
    for x in range (len(n_dep)):
        index_d= archivoExcel.loc[x,'Poblacion']
        
        if index_d>d_mayor:
            d_mayor=index_d
            
   
    return d_mayor


def numero_menor():
    d_menor= numero_mayor()
   
    for m in range (len(n_dep)):        
        index_d2= archivoExcel.loc[m,'Poblacion']
        if index_d2<d_menor:
            d_menor=index_d2
    
    return d_menor


def nombre_mayor():
    d_mayor=0
    for x in range (len(n_dep)):
        index_d= archivoExcel.loc[x,'Poblacion']
        index_n= archivoExcel.loc[x,'Departamento']        
        if index_d>d_mayor:
            d_mayor=index_d
            nombre_M=index_n
            
            
   
    return nombre_M

def nombre_menor():
    d_menor= numero_mayor()
   
    for m in range (len(n_dep)):        
        index_d2= archivoExcel.loc[m,'Poblacion']
        index_n= archivoExcel.loc[m,'Departamento']  
        if index_d2<d_menor:
            d_menor=index_d2
            nombre_m=index_n
    
    return nombre_m

def relacion_ha():
    relacion=archivoExcel['Poblacion'].sum()/archivoExcel['Area'].sum()
    return relacion

med_pob= pob.mean()
print(med_pob)
max_pob= pob.max()
print(max_pob)
    
    

print("El area total en colombia es %i km2"%(area_col()))
print("Promedio de area por departamento es %i km2"%(prom_area_d()))
print("Promedio de personas por area es %i p/km2"%(prom_pers_d()))
print("El departamento con mayor poblacion es %s con %i habitantes."%(nombre_mayor(),numero_mayor()))
print("El departamento con menor poblacion es %s con %i habitantes."%(nombre_menor(),numero_menor()))

print("En colombia hay %i habitantes por km2"%(relacion_ha()))    

fig, ax = plt.subplots()
ax.set_title("Departamento y Poblacion")
ax.set_ylabel("Departamento")
ax.set_xlabel("Poblacion")
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
#crear el gráfico
plt.barh(archivoExcel['Departamento'],archivoExcel['Poblacion'])
plt.show()
plt.pie(archivoExcel['Poblacion'],labels=archivoExcel['Departamento'])
plt.show()







 
    
    



