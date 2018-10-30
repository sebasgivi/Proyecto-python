import math
class AtributosBasicos:
	_direcciones = [0, 90, 180, 270]
	def __init__ (self,PosicionX,PosicionY,vida,radio,vel,direc,imagen,damage):
		self.posicionX = PosicionX
		self.posicionY = PosicionY
		self.vida = vida
		self.radio = radio
		self.vel = vel
		self.direc = direc
		self.imagen = imagen
		self.damage = damage
		self.arreglo_radios = self.sacarRadios(self.radio)

	def getDamage(self):
		return self.damage

	def setDamage(self,damage): 
		self.damage = damage

	def avanzar(self):
		dir_aux = self.getDirec()
		if(dir_aux == 0):
			self.setPosicionX(self.getPosicionX() + 1)
		elif(dir_aux == 90):
			self.setPosicionY(self.getPosicionY() - 1)
		elif(dir_aux == 180):
			self.setPosicionX(self.getPosicionX() - 1)
		else:
			self.setPosicionY(self.getPosicionY() + 1)

		self.arreglo_radios = self.sacarRadios(self.radio)

	def getPosicionY(self):
		return self.posicionY

	def setPosicionY(self,posicion):
		if (posicion < 0):
			self.posicionY = 30
		elif (posicion > 30):
			self.posicionY = 0
		else:
		    self.posicionY = posicion

	def getPosicionX(self):
		return self.posicionX

	def setPosicionX(self,posicion): 
		if (posicion < 0):
		   self.posicionX = 120
		elif (posicion > 120):
			self.posicionX = 0
		else:
			self.posicionX = posicion

	def getVel (self):
		return self.vel

	def setVel (self,velocidad):
		self.vel = velocidad

	def getDirec (self):
		return self.direc

	def getImagen (self):
		return self.imagen

	def sacarRadios (self,radio):
		arreglo_radios = []
		posx_aux = self.getPosicionX() - radio
		posy_aux = self.getPosicionY() - radio
		for i in range(2 * self.radio):
			if(posx_aux < 120 and posy_aux < 30 and posx_aux > 0 and posy_aux > 0):
				arreglo_radios.append(posy_aux * 120 + posx_aux)
			posx_aux+=1
		for i in range(2 * self.radio):
			if(posx_aux < 120 and posy_aux < 30 and posx_aux > 0 and posy_aux > 0):
				arreglo_radios.append(posy_aux * 120 + posx_aux)
			posy_aux +=1
		for i in range(2 * self.radio):
			if(posx_aux < 120 and posy_aux < 30 and posx_aux > 0 and posy_aux > 0):
				arreglo_radios.append(posy_aux * 120 + posx_aux)
			posx_aux -=1
		for i in range(2 * self.radio):
			if(posx_aux < 120 and posy_aux < 30 and posx_aux > 0 and posy_aux > 0):
				arreglo_radios.append(posy_aux * 120 + posx_aux)
			posy_aux -=1

		return arreglo_radios


	def setVida (self,vida):
		self.vida = vida

	def getVida (self):
		return self.vida

	def setRadio (self,radio):
		self.radio = radio

	def getRadio (self):
		return self.radio

	def getArregloRadios(self):
	  return self.arreglo_radios