from AtributosBasicos import AtributosBasicos
from Opciones import Opciones
import random
class Meteoro(AtributosBasicos):
	#Atributos de instancia:
	#Los de AtributosBasicos
	#self._oleada
	def __init__(self, oleada,_rango_colision = 1, vel = 1, imagen = "O", damage = 1):
		_pos_inicial = self.generarPosicion()
		super(Meteoro, self).__init__(_pos_inicial[0], _pos_inicial[1], _rango_colision, 
                                      _rango_colision, vel, _pos_inicial[2], "O", 1)
		self._oleada = oleada
		

	def generarPosicion(self):
		eje = random.randrange(0, 2)
		margen = random.randrange(0, 2)
		especificox = random.randrange(0, Opciones.resx)
		especificoy = random.randrange(0, Opciones.resy)
		_pos_inicial = None
		if (eje == 0):
			if (margen == 1):
				_pos_inicial = [especificox, Opciones.resy, 90]
				return _pos_inicial
			else:
				_pos_inicial = [especificox, 0, 270]
				return _pos_inicial
		else:
			if (margen == 1):
				_pos_inicial = [Opciones.resx, especificoy, 180]
				return _pos_inicial
			else:
				_pos_inicial = [0, especificoy, 0]
		return _pos_inicial

	@staticmethod 
	def crearMeteoros(oleada):
		meteoro = Meteoro(oleada)
		return meteoro

	def setVida(self, vida):
		self._vida = vida 
		if (self._vida > 0):
			self._rangoColision = vida
