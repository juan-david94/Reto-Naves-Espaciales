from nave import *
from registrar import *
from visualizar import *
from registro import *

#En primera instancia se crea el archivo donde van a almacenar los datos de las naves
#las cuales se van a dividir en 3 hojas correspondientes a los 3 tipos de naves que se van a registrar
crear_archivo() 

while True:

    #Se pide al usuario seleccionar opcion segun solicitud que desee realizar
    print("Seleccione 1 para registrar una nave, 2 para visualizar las caracteristicas de las naves registradas o 3 para salir")
    
    solicitud = int(input())
    if solicitud == 1:
        registrarNave()
        

    elif solicitud == 2:
        visualizarNave()

    elif solicitud == 3:
        exit()

    else:
        print("Error: Seleccione la opcion correcta")

    


    

