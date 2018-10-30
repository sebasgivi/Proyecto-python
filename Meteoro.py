from AtributosBasicos import AtributosBasicos
import random
class Meteoro(AtributosBasicos):

	def __init__(self, radio = 1, vel = 1,
				 imagen = "O", damage = 1):
		arreglo = self.generarPosicion()
		super(Meteoro, self).__init__(arreglo[0],arreglo[1],radio,radio,vel,arreglo[2],"O",1)

	def generarPosicion(self):
		## verificar la funcion random para python.
		##hay que usar librerias y no se si ASI es como se deba de invocarlas
		eje = random.randrange(0,2)
		margen = random.randrange(0,2)
		especificox = random.randrange(0,120)
		especificoy = random.randrange(0,30)
		arreglo = None
		if (eje == 0):
			if (margen == 1):
				arreglo = [especificox, 30, 90]
				return arreglo
			else:
				arreglo = [especificox, 0, 270]
				return arreglo
		else:
			if (margen == 1):
				arreglo = [120, especificoy, 180]
				return arreglo
			else:
				arreglo = [0, especificoy, 0]
		return arreglo

	def setVida(self, vida):
		self.vida = vida ## no esrtoy seguro pero creo que aqui va un self despues del igual tal y como lo puse
		if (self.vida > 0):
			self.radio = self.vida
