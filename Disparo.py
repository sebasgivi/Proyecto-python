from AtributosBasicos import AtributosBasicos

class Disparo(AtributosBasicos):
	
		#Atributos de instancia
		#Los de AtributosBasicos
		#self._vida_util_disparo
		#self._nave
	def __init__(self,posicionx,posiciony,direccion,vida_util_disparo,damage,nave):
		super(Disparo, self).__init__(posicionx + self.direccionDisparo(direccion)[0], 
                                      posiciony + self.direccionDisparo(direccion)[1],
                                      1, 1, 2, direccion, "*", damage)
		self._vida_util_disparo=vida_util_disparo
		self._nave = nave
	
	def getVidaUtilDisparo(self):
		return self._vida_util_disparo

	def setVidaUtilDisparo(self,vida_util_disparo): 
		self._vida_util_disparo = vida_util_disparo

	def getNave(self):
		return self._nave

	def setNave(self,nave):
		self.nave = nave

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

	staticmethod	
	def crearDisparo(posicionX, posicionY, direccion, vidautil, damage,nave):
		disparo = Disparo(posicionX, posicionY,
                          direccion, vidautil,
                          damage,nave)
		nave.getListaDisparos().append(disparo)

	staticmethod
	def reducirVidaUtil(personaje):
		listad = []
		for i in range(len(personaje.getListaDisparos())):
			personaje.getListaDisparos()[i].setVidaUtilDisparo(personaje.getListaDisparos()[i].getVidaUtilDisparo() - 1)
			if(personaje.getListaDisparos()[i].getVidaUtilDisparo() <= 0):
				listad.append(i)
		while(len(listad) != 0):
			personaje.getListaDisparos().remove(personaje.getListaDisparos()[listad.pop()])