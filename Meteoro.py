from AtributosBasicos import AtributosBasicos
from Opciones import Opciones
import random
class Meteoro(AtributosBasicos):
	#Atributos de instancia:
	#Los de AtributosBasicos
	#self._oleada
	def __init__(self, oleada,_rango_colision = 1, vel = 1, imagen = "O", damage = 1):
		arreglo = self.generarPosicion()
		super(Meteoro, self).__init__(arreglo[0], arreglo[1], _rango_colision, 
                                      _rango_colision, vel, arreglo[2], "O", 1)
		self._oleada = oleada
		

	def generarPosicion(self):
		eje = random.randrange(0, 2)
		margen = random.randrange(0, 2)
		especificox = random.randrange(0, Opciones.resx)
		especificoy = random.randrange(0, Opciones.resy)
		arreglo = None
		if (eje == 0):
			if (margen == 1):
				arreglo = [especificox, Opciones.resy, 90]
				return arreglo
			else:
				arreglo = [especificox, 0, 270]
				return arreglo
		else:
			if (margen == 1):
				arreglo = [Opciones.resx, especificoy, 180]
				return arreglo
			else:
				arreglo = [0, especificoy, 0]
		return arreglo

	@staticmethod 
	def crearMeteoros(oleada):
		meteoro = Meteoro(oleada)
		return meteoro

	def setVida(self, vida):
		self._vida = vida 
		if (self._vida > 0):
			self._rangoColision = vida
