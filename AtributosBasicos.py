import math
from Opciones import Opciones
class AtributosBasicos:
	_direcciones = [0, 90, 180, 270]
	def __init__ (self, posicion_x, posicion_y, vida, medida_hitbox,
                  velocidad,direccion,imagen,damage):
		self._posicion_x = posicion_x
		self._posicion_y = posicion_y
		self._vida = vida
		self._medida_hitbox = medida_hitbox
		self._velocidad = velocidad
		self._direccion = direccion
		self._imagen = imagen
		self._damage = damage
		self._area_hitbox = self.calcularHitBox()

	def getDamage(self):
		return self._damage

	def setDamage(self,damage): 
		self._damage = damage

	def getPosicionY(self):
		return int(self._posicion_y)

	def setPosicionY(self,posicion):
		if (posicion < 0):
			self._posicion_y = Opciones.resy   #CAMBIAR POR INTERFAZ.
		elif (posicion > Opciones.resy):
			self._posicion_y = 0
		else:
		    self._posicion_y = posicion

	def getPosicionX(self):
		return int(self._posicion_x)

	def setPosicionX(self,posicion):       #CAMBIAR POR INTERFAZ.
		if (posicion < 0):
		   self._posicion_x = Opciones.resx
		elif (posicion > Opciones.resx):
			self._posicion_x = 0
		else:
			self._posicion_x = posicion

	def getVelocidad (self):
		return self._velocidad

	def setVelocidad (self,velocidad):
		self._velocidad = velocidad

	def getDireccion (self):
		return self._direccion

	def getImagen (self):
		return self._imagen

	def setVida (self,vida):
		self._vida = vida

	def getVida (self):
		return self._vida

	def setMedidaHitBox (self, medida_hitbox):
		self._medida_hitbox = medida_hitbox

	def getMedidaHitBox (self):
		return self._medida_hitbox

	def getHitBox(self):
	  return self._area_hitbox

	def avanzar(self):
		dir_actual = self.getDireccion()
		if(dir_actual == 0):
			self.setPosicionX(self.getPosicionX() + 1)
		elif(dir_actual == 90):
			self.setPosicionY(self.getPosicionY() - 1)
		elif(dir_actual == 180):
			self.setPosicionX(self.getPosicionX() - 1)
		else:
			self.setPosicionY(self.getPosicionY() + 1)

		self._area_hitbox = self.calcularHitBox()

	def calcularHitBox (self):
		hit_box = []
		posx_aux = self.getPosicionX() - self._medida_hitbox
		posy_aux = self.getPosicionY() - self._medida_hitbox
		for i in range(2 * self._medida_hitbox):
			if(posx_aux < Opciones.resx and posy_aux < Opciones.resy and posx_aux > 0
               and posy_aux > 0):
				hit_box.append(posy_aux*Opciones.resx + posx_aux)
			posx_aux+=1
		for i in range(2 * self._medida_hitbox):
			if(posx_aux < Opciones.resx and posy_aux < Opciones.resy and posx_aux > 0
               and posy_aux > 0):
				hit_box.append(posy_aux*Opciones.resx + posx_aux)
			posy_aux +=1
		for i in range(2 * self._medida_hitbox):
			if(posx_aux < Opciones.resx and posy_aux < Opciones.resy and posx_aux > 0
               and posy_aux > 0):
				hit_box.append(posy_aux*Opciones.resx + posx_aux)
			posx_aux -=1
		for i in range(2 * self._medida_hitbox):
			if(posx_aux < Opciones.resx and posy_aux < Opciones.resy and posx_aux > 0
               and posy_aux > 0):
				hit_box.append(posy_aux*Opciones.resx + posx_aux)
			posy_aux -=1

		return hit_box