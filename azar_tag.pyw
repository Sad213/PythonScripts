import os, random
import tkinter as tk

#buscara la carpeta que contenga las tags
def buscar(lista_tags):
    global carpetas
    errores = 0 #Control de errores por si se introduce una tag mal
    #Separamos las tags y la escribimos todas en minusculas
    #Find distingue entre mayus y minus
    tags = lista_tags.lower().split()
    parar = False
    while parar == False:
        comprobador = 0
        #Escoger carpeta al azar
        folder = random.choice(carpetas)
        folder = folder.lower()
        for i in range(len(tags)):
            if folder.find(tags[i]) == -1:#Significa que no lo ha encontrado
                comprobador = 1
                break
        if(comprobador == 0):
            a=os.listdir(folder)
            file = folder+'\\'+a[0]
            os.startfile(file)
            parar = True
        elif(errores == 1000):
            parar = True
        errores += 1
        print(errores)

global carpetas
direcion = os.getcwd()
carpetas = os.listdir(direcion)
#Dibujar menu
root = tk.Tk()
root.minsize(300,100)
root.geometry("320x100")

L1 = tk.Label(root, text="Tags")
L1.pack()
tag = tk.Entry()
tag.bind("<Return>", (lambda event: buscar(tag.get())))
tag.pack()
boton = tk.Button(root, text="test", command=lambda:buscar(tag.get()))
boton.pack()

root.mainloop()
