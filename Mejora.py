from AtributosBasicos import AtributosBasicos
from Mensajes import Mensajes
import random
class Mejora(AtributosBasicos):
	_lista_mejoras = []
	_mejoras_activas = []

	def __init__(self, posicion_x, posicion_y):
		super().__init__(posicion_x, posicion_y, 1, 1, 0, 0, "+", 0)
		self._cualidad = random.randrange(0,4)
		Mejora._lista_mejoras.append(self)

	def calcularMejora(self, nave):
		opcion = self._cualidad
		if(opcion == 0):
			nave.setVida(nave.getVida() + 1)
			Mejora._mejoras_activas.append(self)
			print(Mensajes.mensajes.get("temporaryLife"))
		elif(opcion == 1):
			nave.setNumDisparos(nave.getNumDisparos() + 1)
			Mejora._mejoras_activas.append(self)
			print(Mensajes.mensajes.get("temporaryShots"))
		elif(opcion == 2):
			nave.setVidaUtilDisparo(nave.getVidaUtilDisparo() + 1)
			Mejora._mejoras_activas.append(self)
			print(Mensajes.mensajes.get("temporaryLifeBullet"))
		elif(opcion == 3):
			nave.setVelocidad(nave.getVelocidad() + 1)
			Mejora._mejoras_activas.append(self)
			print(Mensajes.mensajes.get("temporaryShipSpeed"))
		elif(opcion == 4):
			nave.setDamage(nave.getDamage() + 1)
			Mejora._mejoras_activas.append(self)
			print(Mensajes.mensajes.get("temporaryDamage"))
		return nave

	def BorrarMejoras(nave):
		while(len(Mejora._mejoras_activas) > 0):
			opcion = Mejora._mejoras_activas.pop()._cualidad
			if(opcion == 0):
				nave.setVida(nave.getVida() - 1)
			elif(opcion == 1):
				nave.setNumDisparos(nave.getNumDisparos() - 1)
			elif(opcion == 2):
				nave.setVidaUtilDisparo(nave.getVidaUtilDisparo() - 1)
			elif(opcion == 3):
				nave.setVelocidad(nave.getVelocidad() - 1)
			elif(opcion == 4):
				nave.setDamage(nave.getDamage() - 1)
