from AtributosBasicos import AtributosBasicos

class Disparo(AtributosBasicos):

	def __init__(self,posicionx,posiciony,direccion,vida_util_disparo,damage):
		super(Disparo, self).__init__(posicionx + self.direccionDisparo(direccion)[0], 
                                      posiciony + self.direccionDisparo(direccion)[1],
                                      1, 1, 2, direccion, "*", damage)
		self._vida_util_disparo=vida_util_disparo
	
	def getVidaUtilDisparo(self):
		return self._vida_util_disparo

	def setVidaUtilDisparo(self,vida_util_disparo): 
		self._vida_util_disparo = vida_util_disparo

	def direccionDisparo(self,direccion):
		arreglo = []
		if(direccion == 0):
			arreglo.append(1)
			arreglo.append(0)
		elif(direccion == 90):
			arreglo.append(0)
			arreglo.append(-1)
		elif(direccion == 180):
			arreglo.append(-1)
			arreglo.append(0)
		else:
			arreglo.append(0)
			arreglo.append(1)
		return arreglo