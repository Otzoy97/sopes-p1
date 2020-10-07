from fproc import makeSentences
from sentence import printSentences, sendSenteces

def main():
    url = "http://35.208.119.75/newMsg"
    while True :
        print("1. Ingresar ruta")
        print("2. Ingresar dirección")
        print("3. Ver datos")
        print("4. Enviar datos")
        iUsr = input(" > ")
        if iUsr == "exit" or iUsr == "quit":
            return
        while iUsr != "1" and iUsr != "2" and iUsr != "3" and iUsr != "4":
            print("Indique un valor válido")
            iUsr = input(" > ")
        if iUsr == "1" :
            # procesar y validar ruta, leer archivo, cargar información
            filePath = input(" > ")
            makeSentences(filePath)
        elif iUsr == "2":
            # guardar ruta del balanceador de ruta
            usrInput = input(" > ")
            print(" > Dirección : '", usrInput, "'")
            url = usrInput
        elif iUsr == "3":
            # revelar datos
            printSentences()
        elif iUsr == "4":
            # enviar datos
            sendSenteces(url)

if __name__ == "__main__":
    main()
