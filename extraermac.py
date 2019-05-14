datos = open("listamacs.txt","r")
datosfiltrados = open("filtrados.txt","a+")#Si no esta creado no crea el archivo
#Opcion a+ lectura y escritura del fichero y si no esta creado se crea
global lista
#Se crea una lista con las posibles MAC que contenga filtrados.txt
lista = datosfiltrados.read().split()

#Funcion que comprueba si la MAC esta repetida y de no ser la añade al fichero
#y a la lista
def comprobar(dato):
    global lista
    if dato in lista:
        pass
    else:
        datosfiltrados.write(dato + "\n")
        lista += [dato]

#Obtiene las MACs y se las pasa a la funcion comprobar        
for line in datos:
    dato = line.split()
    #len(dato)
    #4 SSID|MAC|-#|dBm
    #3 Name|Address|Signal o MAC|-#|dBm
    #2 zona #:
    #1 0.0.0.0.0.0
    if len(dato) == 4 and "MOVISTAR" not in dato[0] \
    and "ONO" not in dato[0] and "MiFibra" not in dato[0]:
        comprobar(dato[1])
    elif len(dato) == 3 and dato[1] != "Address":
        comprobar(dato[0])

datosfiltrados.close()
datos.close()
