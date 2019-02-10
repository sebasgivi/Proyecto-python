from Meteoro import Meteoro
class Oleada:
	meteoros = []
	score = 0
	def __init__(self, meteoros_destruidos = 0,
				 num_oleada = 1, cantidad_de_turnos = 0):
		self._meteoros_destruidos = meteoros_destruidos
		self._num_oleada = num_oleada
		self._cantidad_de_turnos = cantidad_de_turnos


	def crearMeteoritos(self):
		for i in range(self.getNumOleada() * 1):
			meteoro = Meteoro()
			meteoro.setVelocidad(self.getNumOleada()/2 + 1)
			Oleada.meteoros.append(meteoro)  

	def getNumOleada(self):
		return self._num_oleada

	def setNumOleada(self, oleada):
		self._num_oleada = oleada

	def getMeteorosDestruidos(self):
		return self._meteoros_destruidos

	def setMeteorosDestruidos(self, meteoros_destruidos):
		self._meteoros_destruidos = meteoros_destruidos

	def getCantidadDeTurnos(self):
		return self._cantidad_de_turnos

	def setCantidadDeTurnos(self, cantidad_de_turnos):
		self._cantidad_de_turnos = cantidad_de_turnos