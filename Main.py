import sys
from Juego import Juego
from Mensajes import Mensajes
from Nave import Nave

class Main():
	
	if __name__ == "__main__":

		Juego.idioma()
		juego = Juego()

		while(1 == 1):
			print(Mensajes.mensajes.get("menu"))
			opcion=input(Mensajes.mensajes.get("opcion"))
			if(opcion == "1"):
				juego.jugar()
			elif(opcion == "2"):
				print(Mensajes.mensajes.get("instrucciones"))
			elif(opcion == "3"):
				print(Mensajes.mensajes.get("top puntajes"))
				Juego.MejoresPuntajes()
			elif(opcion == "4"):
				SystemExit()
			juego = 0
			juego = Juego()