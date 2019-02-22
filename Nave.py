from AtributosBasicos import AtributosBasicos
from Disparo import Disparo
from Opciones import Opciones


class Nave(AtributosBasicos):
	
	#Atributos de instancia:
	#Los de AtributosBasicos
	#self._numero_disparos 
	#self._imagenes 
	#self._vida_util_disparo 
	#self._lista_disparos 
	#self._mejoras_activas 
	#self._juego 
	def __init__(self,juego, posicion_x = Opciones.resx/2, posicion_y = Opciones.resy/2, 
                 vida = 3, imagenes = [">","^","<","v"], numero_disparos = 3,
                 vida_util_disparo = 10, lista_disparos = [], lista_mejoras = []):
		super(Nave, self).__init__(posicion_x, posicion_y, vida, 1, 5, 90, "^", 1)
		self._numero_disparos = numero_disparos
		self._imagenes = imagenes
		self._vida_util_disparo = vida_util_disparo
		self._lista_disparos = lista_disparos
		self._mejoras_activas = lista_mejoras
		self._juego = juego		

	def getVidaUtilDisparo(self):
		return self._vida_util_disparo

	def setVidaUtilDisparo(self, vidaUtilDisparo): 
		self._vida_util_disparo = vidaUtilDisparo

	def getMejorasActivas(self):
		return self._mejoras_activas

	def getNumDisparos(self):
		return self._numero_disparos

	def setNumDisparos(self, numero_disparos): 
		self._numero_disparos = numero_disparos
	
	def getListaDisparos(self):
		return self._lista_disparos
		
	def gameOver(self):
		if (self.getVida() == 0):
			return True
		else:
			return False

	

	def setDireccion(self, rotacion):
		arreglo = [0, 90, 180, 270]
		indice = arreglo.index(self._direccion)
		if(rotacion == Opciones._control_list[1]):
			if(indice == 3):
				self._direccion = arreglo[0]
				self._imagen = self._imagenes[0]
			else:
				self._direccion = arreglo[indice + 1]
				self._imagen = self._imagenes[indice + 1]
		else:
			if(indice == 0):
				self._direccion = arreglo[3]
				self._imagen = self._imagenes[3]
			else:
				self._direccion = arreglo[indice - 1]
				self._imagen = self._imagenes[indice - 1]

	
