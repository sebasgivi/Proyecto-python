from AtributosBasicos import AtributosBasicos
from Disparo import Disparo
class Nave(AtributosBasicos):
	"""docstring for Nave"""
	disparos = []
	def __init__(self, imagenes = [">","^","<","v"], numDisparos = 3, vidaUtilDisparo = 10):
		super(Nave, self).__init__(60,15,3,1,5,90,"^",1)
		self.numDisparos = numDisparos
		self.imagenes = imagenes
		self.vidaUtilDisparo = vidaUtilDisparo

	def getVidaUtilDisparo(self):
		return self.vidaUtilDisparo

	def setVidaUtilDisparo(self,vidaUtilDisparo): 
		self.vidaUtilDisparo = vidaUtilDisparo

	def getNumDisparos(self):
		return self.numDisparos

	def setNumDisparos(self,numDisparos): 
		self.numDisparos = numDisparos
	
	def gameOver(self):
		if (self.getVida() == 0):
			return True
		else:
			return False

	def crearDisparo(self):
		disparo = Disparo(self.getPosicionX(),self.getPosicionY(),self.getDirec(),self.getVidaUtilDisparo(),self.getDamage())
		Nave.disparos.append(disparo)

	def setDirec(self,rotacion):
		arreglo = [0,90,180,270]
		indice = arreglo.index(self.direc)
		if(rotacion == "a"):
			if(indice == 3):
				self.direc = arreglo[0]
				self.imagen = self.imagenes[0]
			else:
				self.direc = arreglo[indice + 1]
				self.imagen = self.imagenes[indice + 1]
		else:
			if(indice == 0):
				self.direc = arreglo[3]
				self.imagen = self.imagenes[3]
			else:
				self.direc = arreglo[indice - 1]
				self.imagen = self.imagenes[indice - 1]