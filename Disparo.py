from AtributosBasicos import AtributosBasicos

class Disparo(AtributosBasicos):

	def __init__(self,posicionx,posiciony,direc,vida_util_disparo,damage):
		super(Disparo, self).__init__(posicionx + self.dirDisparo(direc)[0],posiciony + self.dirDisparo(direc)[1],1,1,2,direc,"*",damage)
		self.vida_util_disparo=vida_util_disparo
	
	def getVidaUtilDisparo(self):
		return self.vida_util_disparo

	def setVidaUtilDisparo(self,vida_util_disparo): 
		self.vida_util_disparo = vida_util_disparo

	def getArregloRadios(self):
		return self.arreglo_radios

	def dirDisparo(self,direc):
		arreglo = []
		if(direc==0):
			arreglo.append(1)
			arreglo.append(0)
		elif(direc==90):
			arreglo.append(0)
			arreglo.append(-1)
		elif(direc==180):
			arreglo.append(-1)
			arreglo.append(0)
		else:
			arreglo.append(0)
			arreglo.append(1)
		return arreglo