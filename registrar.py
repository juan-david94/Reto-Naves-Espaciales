from nave import *
from registro import *

#se crean listas para almacenar como lista para visualizar los diferentes tipos de naves
lista_lanzadera = []
lista_no_tripuladas = []
lista_tripuladas = []


# Se crea funcion menu para que el usuario escoja el tipo de nave que desea registrar (funcion registrarNave)
# Funcion menu tambien se utiliza al momento de visualizar la caracteristicas del tipo de nave que el usuario desee
def menu():
    print("Selecciona la nave que desea registrar segun la opcion que corresponda (1, 2 o 3) o presione 4 para salir")
    print("1. Vehiculo lanzadera")
    print("2. Naves no Tripuladas")
    print("3. Naves Tripuladas")
    print("4. salir")


#Funcion creada para que el usuario indique las caracteristicas que el programa vaya solicitando
#Segun el tipo de nave seleccionado en el menu
def registrarNave():    
    menu()
    seleccion_nave = int(input())

    if seleccion_nave == 1:
        print("Ha seleccionado Vehiculo lanzadera")
        print("Digita las caracteristicas de la nave que desea registrar segun se vayan solicitando")
        print("Digite el nombre de la nave")
        nombre_lan = input()
        print("Digite el pais de origen de la nave")
        pais_lan = input()
        print("Digite el peso de la nave")
        peso_lan = input()
        print("Digite el empuje de la nave")
        empuje_lan = input()
        print("Digite el combustible que utiliza la nave")
        combustible_lan = input()
        print("Digite la altura de la nave")
        altura = input()

# Se crea objeto para cada nave registrada y se almacena en la lista creada para tipo de nave
        vehiculo_lanzadera = vehiculoLanzadera(nombre_lan, pais_lan, peso_lan, empuje_lan, combustible_lan, altura)
        lista_lanzadera.append(vehiculo_lanzadera)


    elif seleccion_nave == 2:
        print("Ha seleccionado naves no tripuladas")
        print("Digita las caracteristicas de la nave que desea registrar segun se vayan solicitando")
        print("Digite el nombre de la nave")
        nombre_noTrip = input()
        print("Digite el pais de origen de la nave")
        pais_noTrip = input()
        print("Digite el empuje de la nave")
        empuje_noTrip = input()
        print("Digite el desplazamiento de la nave")
        despla_noTrip = input()
        print("Digite el combustible utilizado por la nave")
        combustible_noTrip = input()
        print("Digite la funcionalidad de la nave")
        funcion_noTrip = input()

# Se crea objeto para cada nave registrada y se almacena en la lista creada para tipo de nave
        nave_no_tripulante = navesNoTripuladas(nombre_noTrip, pais_noTrip, empuje_noTrip, despla_noTrip,combustible_noTrip, funcion_noTrip)
        lista_no_tripuladas.append(nave_no_tripulante)

    elif seleccion_nave == 3:
        print("Ha seleccionado Naves Tripuladas")
        print("Digita las caracteristicas de la nave que desea registrar segun se vayan solicitando")
        print("Digite el nombre de la nave")
        nombre_trip = input()
        print("Digite el pais de origen de la nave")
        pais_trip = input()
        print("Digite el peso de la nave")
        peso_trip = input()
        print("Digite la capacidad de personas de la nave")
        capacidad_trip = input()
        print("Digite la distancia a la que orbita la nave")
        distancia_trip = input()

# Se crea objeto para cada nave registrada y se almacena en la lista creada para tipo de nave
        nave_tripulada = navesTripuladas(nombre_trip, pais_trip, peso_trip, capacidad_trip, distancia_trip)
        lista_tripuladas.append(nave_tripulada)

    elif seleccion_nave == 4:
        exit()
        

    else:
        print("Error: Seleccione la opcion correcta")