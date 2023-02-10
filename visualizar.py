from registrar import *
from nave import *

# Se crea funcion para visualizar las caracteristicas de la nave seleccionada en el menu
# almacenadas en las listas creadas en el archivo registrar.py
# las cuales se van iterando segun el numero de naves registradas
def visualizarNave():
    menu()
    seleccion_nave = int(input())

    if seleccion_nave == 1:
    
        print(" ")
        for a in lista_lanzadera:
            a.visualizarLanzadera()
    
    elif seleccion_nave == 2:
        print(" ")
        for a in lista_no_tripuladas:
            a.visualizarNotripuladas()

    elif seleccion_nave == 3:
        print(" ")
        for a in lista_tripuladas:
            a.visualizarTripuladas()
            