datos = open("listamacs.txt","r")
datosfiltrados = open("filtrados.txt","a+")#Si no esta creado no crea el archivo
#La opcion "a+" no extrai las mac pero no se porque no las filtraba
datosfiltrados.close()

def comprobar(dato):
    datosfiltrados = open("filtrados.txt","r+")
    test = datosfiltrados.read().split()#Lista de las macs filtradas
    if dato in test:
        pass
    else:
        datosfiltrados.write(dato + "\n")
        datosfiltrados.close()
            
for line in datos:
    dato = line.split()
    #len(dato)
    #4 SSID|MAC|-#|dBm
    #3 Name|Address|Signal o MAC|-#|dBm
    #2 zona #:
    #1 0.0.0.0.0.0
    if len(dato) == 4:
        comprobar(dato[1])
    elif len(dato) == 3 and dato[1] != "Address":
        comprobar(dato[0])
            
datosfiltrados.close()
datos.close()
