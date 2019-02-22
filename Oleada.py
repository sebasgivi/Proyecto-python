from Meteoro import Meteoro
class Oleada:
	
	score = 0
	#Atributos de instancia:
	#self._meteoros_destruidos 
	#self._num_oleada 
	#self._cantidad_de_turnos 
	#self._lista_meteoros 
	#self._juego 

	def __init__(self,juego, meteoros_destruidos = 0, num_oleada = 1, 
				 cantidad_de_turnos = 0,meteoros = []):
		self._meteoros_destruidos = meteoros_destruidos
		self._num_oleada = num_oleada
		self._cantidad_de_turnos = cantidad_de_turnos
		self._lista_meteoros = meteoros
		self._juego = juego
		
		

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

	def getListaMeteoros(self):
		return self._lista_meteoros

	def setListaMeteoros(self, lista_meteoros):
		self._lista_meteoros = lista_meteoros

	def crearOleada(self):
		for i in range(self.getNumOleada() * 1):
			meteoro = Meteoro.crearMeteoros(self)
			meteoro.setVelocidad(self.getNumOleada()/2 + 1)
			self.getListaMeteoros().append(meteoro)  
