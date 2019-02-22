from AtributosBasicos import AtributosBasicos
from Mensajes import Mensajes
from Nave import Nave 
import random
class Mejora(AtributosBasicos):
	_lista_mejoras = []
	
		#Atributos de instancia:
		#Atributos de AtributosBasicos
		#self._cualidad
		#self._nave
	def __init__(self, posicion_x, posicion_y,nave):
		super().__init__(posicion_x, posicion_y, 1, 1, 0, 0, "+", 0)
		self._cualidad = random.randrange(0,4)
		self._nave = nave
		Mejora._lista_mejoras.append(self)

	def calcularMejora(self):
		opcion = self._cualidad
		if(opcion == 0):
			self._nave.setVida(self._nave.getVida() + 1)
			self._nave.getMejorasActivas().append(self)
			print(Mensajes.mensajes.get("temporary life"))
		elif(opcion == 1):
			self._nave.setNumDisparos(self._nave.getNumDisparos() + 1)
			self._nave.getMejorasActivas().append(self)
			print(Mensajes.mensajes.get("temporary shots"))
		elif(opcion == 2):
			self._nave.setVidaUtilDisparo(self._nave.getVidaUtilDisparo() + 1)
			self._nave.getMejorasActivas().append(self)
			print(Mensajes.mensajes.get("temporary life bullet"))
		elif(opcion == 3):
			self._nave.setVelocidad(self._nave.getVelocidad() + 1)
			self._nave.getMejorasActivas().append(self)
			print(Mensajes.mensajes.get("temporary ship speed"))
		elif(opcion == 4):
			self._nave.setDamage(self._nave.getDamage() + 1)
			self._nave.getMejorasActivas().append(self)
			print(Mensajes.mensajes.get("temporary damage"))
		return self._nave

	def borrarMejoras(_nave):
		while(len(_nave._mejoras_activas) > 0):
			opcion = _nave._mejoras_activas.pop()._cualidad
			if(opcion == 0):
				_nave.setVida(_nave.getVida() - 1)
			elif(opcion == 1):
				_nave.setNumDisparos(_nave.getNumDisparos() - 1)
			elif(opcion == 2):
				_nave.setVidaUtilDisparo(_nave.getVidaUtilDisparo() - 1)
			elif(opcion == 3):
				_nave.setVelocidad(_nave.getVelocidad() - 1)
			elif(opcion == 4):
				_nave.setDamage(_nave.getDamage() - 1)

	