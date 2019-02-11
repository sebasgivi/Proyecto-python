import sys
from Juego import Juego
from Mensajes import Mensajes
from Nave import Nave
from Opciones import Opciones

class Main():
	
	if __name__ == "__main__":

		Opciones.changeLanguage()
		while(1 == 1):
			print(Mensajes.mensajes.get("menu"))
			opcion=input(Mensajes.mensajes.get("opcion"))
			if(opcion == "1"):
				juego = Juego()
				juego.jugar()
			elif(opcion == "2"):
				print(Mensajes.mensajes.get("instrucciones"))
			elif(opcion == "3"):
				print(Mensajes.mensajes.get("top puntajes"))
				Juego.MejoresPuntajes()
			elif(opcion == "4"):
				option = input(Mensajes.mensajes.get("options"))
				if(option == "1"):
					resx = input(Mensajes.mensajes.get("resx"))
					resy = input(Mensajes.mensajes.get("resy"))
					Opciones.changeOpciones(resx, resy)
				elif(option == "2"):
					up = input(Mensajes.mensajes.get("up"))
					left = input(Mensajes.mensajes.get("left"))
					right = input(Mensajes.mensajes.get("right"))
					Opciones.changeControls(up, left, right)
				elif(option == "3"):
					Opciones.changeLanguage()
			elif(opcion == "5"):
				break
			juego = 0
			juego = Juego()