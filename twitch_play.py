import socket
import pyautogui
import threading

mensaje = ""
#Credenciales de twitch
usuario = "controler213"
contra = "oauth:#"
canal = "nadie213"

#Conectarse al chat
SERVER = "irc.twitch.tv"
PORT = 6667
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + contra + "\n" +
	  "NICK " + usuario + "\n" +
	  "JOIN #" + canal + "\n").encode())

#Enviar mensajes
def enviarmensaje(irc, mensaje):
    mensajeTemp = "PRIVMSG #" + canal + " :" + mensaje
    irc.send((mensajeTemp + "\n").encode())
        
#Controles de juego
def controles():
    global mensaje
    while True:
        if "up" in mensaje.lower():
            pyautogui.keyDown('up')
            mensaje = ""
            pyautogui.keyUp('up')
        elif "a" in mensaje.lower():
            pyautogui.keyDown('a')
            mensaje = ""
            pyautogui.keyUp('a')
        elif "b" in mensaje.lower():
            pyautogui.keyDown('s')
            mensaje = ""
            pyautogui.keyUp('s')
        elif "up" in mensaje.lower():
            pyautogui.keyDown('up')
            mensaje = ""
            pyautogui.keyUp('up')
        elif "down" in mensaje.lower():
            pyautogui.keyDown('down')
            mensaje = ""
            pyautogui.keyUp('down')
        elif "left" in mensaje.lower():
            pyautogui.keyDown('left')
            mensaje = ""
            pyautogui.keyUp('left')
        elif "right" in mensaje.lower():
            pyautogui.keyDown('right')
            mensaje = ""
            pyautogui.keyUp('right')
        else:
            pass

#Lo relacionado con el chat de twitch
def twitch():
    #unirse al chat
    def unirsealchat():
        conectado = True

        while conectado:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for leer in readbuffer_join.split("\n")[0:-1]:
                conectado = procesocompletado(leer)

    def procesocompletado(leer):
	#El ultimo mensaje del handshake
        if ("End of /NAMES list" in leer):
	#Mensaje que se envia al chat al conectarse
            enviarmensaje(irc, "Mando conectado")
            return False
        else:
            return True

    unirsealchat()

    def extraermensaje(leer):
        global mensaje
        try:
            mensaje =(leer.split(":",2))[2]
        except:
            mensaje = ""
        return mensaje

    def Console(leer):
        if "PRIVMSG" in leer:
            return False
        else:
            return True

    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for leer in readbuffer.split("\r\n"):
            if leer == "":
                continue
            #Si se esta inactivo te desconecta, de esta manera no
            elif "PING" in leer and Console(leer):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                continue
            else:
                mensaje = extraermensaje(leer)


if __name__ =='__main__':
    t1 = threading.Thread(target = twitch)
    t1. start()
    t2 = threading.Thread(target = controles)
    t2. start()
