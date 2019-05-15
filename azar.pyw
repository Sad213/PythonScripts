import os, random

#Direcion en la que se ejecuta el script
direcion = os.getcwd()
#Carpetas del directorio 
items = os.listdir(direcion)
#Carpeta escogida al azar
folder = random.choice(items)
#Archivos dentro de la carpeta
a=os.listdir(folder)
#Abrir primer archivo de la carpeta
os.startfile(folder+'\\'+a[0])
