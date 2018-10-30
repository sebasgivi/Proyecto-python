import msvcrt
import time
from Oleada import Oleada
from Nave import Nave
from Tienda import Tienda

class Juego:
	
	resx = 120
	resy = 30

	def __init__(self, estado_juego = True, oleada = Oleada(), personaje = Nave()):
		self._estado_juego = estado_juego
		self.oleada = oleada
		self.personaje = personaje

	def cambiarEstadoJuego(self):
		if(self.getEstadoJuego() == True):
			self.setEstadoJuego(False)
		else:
			self.setEstadoJuego(True)

	def jugar(self):
		self.oleada = Oleada()
		self.oleada.crearMeteoritos()
		self.personaje = Nave()
		while((self.personaje.gameOver()) == False):
			self.graficar()
			time.sleep(0.5)
			timeI = time.time()
			if(msvcrt.kbhit() == True):
				opcion = msvcrt.getch()
				opcion = opcion.decode("utf-8")
				if(self.getEstadoJuego() == True):
					if(opcion == "a" or opcion == "d"):
						self.personaje.setDirec(opcion)
						self.refrescar()
					elif(opcion == "w"):
						for i in range(self.personaje.getVel()):
							self.personaje.avanzar()
							self.colision()
						self.refrescar()
					elif(opcion == "f"):
						if(len(Nave.disparos)<self.personaje.getNumDisparos()):
							self.personaje.crearDisparo()
							self.refrescar()
						elif(opcion == "p"):
							self.cambiarEstadoJuego()
						else:
							self.refrescar()
					time.sleep(timeI + 1 - time.time())
				else:
					if(opcion == "p"):
						self.cambiarEstadoJuego()
			else:
				if(self.getEstadoJuego() == True):
					self.refrescar()
					time.sleep(timeI + 0.5 - time.time())
		print("Fin del Juego")
		self.personaje = Nave()
		self.oleada.meteoros = []
		Nave.disparos = []

	def setEstadoJuego(self,estado):
		self._estado_juego = estado

	def getEstadoJuego(self):
		return self._estado_juego

	def colision(self):
		pila_m = []
		pila_d = []
		for i in range(len(self.oleada.meteoros)):
			for j in range(i + 1, len(self.oleada.meteoros)):
				if(self.verificarMM(self.oleada.meteoros[i], self.oleada.meteoros[j]) == True):
					self.oleada.meteoros[i].setVida(self.oleada.meteoros[i].getVida()
											   - self.oleada.meteoros[j].getDamage())
					self.oleada.meteoros[j].setVida(self.oleada.meteoros[j].getVida()
											   - self.oleada.meteoros[i].getDamage())
					if(not i in pila_m and
					   self.oleada.meteoros[i].getVida() <= 0):
						pila_m.append(i)
					if(not j in pila_m and
					   self.oleada.meteoros[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(Nave.disparos)):
			for j in range(len(self.oleada.meteoros)):
				if(self.verificarDM(Nave.disparos[i], self.oleada.meteoros[j]) == True):
					self.oleada.meteoros[j].setVida(self.oleada.meteoros[j].getVida()
											   - Nave.disparos[i].getDamage())
					if(not i in pila_d):
						pila_d.append(i)
					if(not j in pila_m and
					   self.oleada.meteoros[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(self.oleada.meteoros)):
			if(self.verificarNM(self.personaje, self.oleada.meteoros[i])):
				self.personaje.setVida(self.personaje.getVida() - self.oleada.meteoros[i].getDamage())
				if(not i in pila_m):
					pila_m.append(i)
					self.oleada.setMeteorosDestruidos(self.oleada.getMeteorosDestruidos() + 1)
		while(len(pila_m) > 0):
			self.oleada.meteoros.remove(self.oleada.meteoros[pila_m.pop()])
		while(len(pila_d) > 0):
			Nave.disparos.remove(Nave.disparos[pila_d.pop()])
			Oleada.score+=10

	def verificarDM(self, d, m):
		arreglo_d = d.getArregloRadios()
		arreglo_m = m.getArregloRadios()
		for i in range(len(arreglo_m)):
			if(arreglo_m[i] in arreglo_d):
				return True
		return False

	def verificarMM(self, m1, m2):
		arreglo_m1 = m1.getArregloRadios()
		arreglo_m2 = m2.getArregloRadios()
		for i in range(len(arreglo_m1)):
			if(arreglo_m1[i] in arreglo_m2):
				return True
		return False

	def verificarNM(self, n, m):
		arreglo_n = n.getArregloRadios()
		arreglo_m = m.getArregloRadios()
		for i in range(len(arreglo_m)):
			if(arreglo_m[i] in arreglo_n):
				return True
		return False

	def refrescar(self):
		if(len(self.oleada.meteoros) > 0):
			vel_m = int(self.oleada.meteoros[0].getVel())
			self.oleada.setCantidadDeTurnos(self.oleada.getCantidadDeTurnos() + 1)
			for j in range(vel_m):
				for i in range(len(self.oleada.meteoros)):
					self.oleada.meteoros[i].avanzar()
				self.colision()
			if(len(Nave.disparos) > 0):
				vel_d = Nave.disparos[0].getVel()
				for j in range(vel_d):
					for i in range(len(Nave.disparos)):
						Nave.disparos[i].avanzar()
					self.colision()
			self.reducir_vu()
			if(self.personaje.getVida() == 0):
				return 0
		else:
			if(self.personaje.getVida() == 0):
				return 0
			opcion = 4
			print("Oleada Completada, Desea visitar la tienda?\n 1)Si 2)No 3)Finalizar")
			while(opcion != "1" and opcion != "2" and opcion != "3"):
				opcion = input()
				if(opcion == "1" or opcion == "2"):
					Nave.disparos = []
					if(opcion=="1"):
						self.personaje = Tienda.comprar(self.personaje)
					self.personaje.setPosicionX(60)
					self.personaje.setPosicionY(15)
					self.oleada.setNumOleada(self.oleada.getNumOleada()+1)
					self.oleada.crearMeteoritos()
				elif(opcion == "3"):
					self.personaje.setVida(0)
		return 0

	def reducir_vu(self):
		listad = []
		for i in range(len(Nave.disparos)):
			Nave.disparos[i].setVidaUtilDisparo(Nave.disparos[i].getVidaUtilDisparo() - 1)
			if(Nave.disparos[i].getVidaUtilDisparo() <= 0):
				listad.append(i)
		while(len(listad) != 0):
			Nave.disparos.remove(Nave.disparos[listad.pop()])

	def graficar(self):
		print("Oleada Numero: ",self.oleada.getNumOleada()," Vidas: ",self.personaje.getVida(),
			"Score: ",Oleada.score,"Meteoros Restantes: ",len(self.oleada.meteoros),
		" EstadoJuego: ",self.getEstadoJuego()," cantidad de turnos ",self.oleada.getCantidadDeTurnos())
		for i in range(self.resx):
			print("-",end="")
		print("\n")
		matriz = self.imprimirRadios(self.oleada.meteoros, Nave.disparos)
		matriz[self.personaje.getPosicionX()][self.personaje.getPosicionY()] = self.personaje.getImagen()
		for i in range( len(self.oleada.meteoros) ):
			matriz[self.oleada.meteoros[i].getPosicionX()][self.oleada.meteoros[i].getPosicionY()] = "O"
		for	i in range( len(Nave.disparos) ):
			matriz[Nave.disparos[i].getPosicionX()][Nave.disparos[i].getPosicionY()] = "*"
			
		for i in range(self.resy + 1):
			print("|",end="")
			for j in range(self.resx + 1):
				if matriz[j][i] == 0:
					print(".",end="")
				else:
					print(matriz[j][i],end="")
			print("|",end="")
			print("\n")
		for i in range(self.resx):
			print("-",end="")
		print("\n")
		
	def imprimirRadios(self,listam,listad):
		matriz = []
		for i in range(self.resx + 1):
			matriz.append([0] * (self.resy + 1))
		for k in range(len(listam)):
			posx_aux = listam[k].getPosicionX() - listam[k].getRadio()
			posy_aux = listam[k].getPosicionY() - listam[k].getRadio()
			for i in range(2 * listam[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux+=1
			for i in range(2 * listam[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux+=1
			for i in range(2 * listam[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux-=1
			for i in range(2 * listam[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux-=1
		for k in range(len(listad)):
			posx_aux = listad[k].getPosicionX() - listad[k].getRadio()
			posy_aux = listad[k].getPosicionY() - listad[k].getRadio()
			for i in range(2 * listad[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux+=1
			for i in range(2 * listad[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux+=1
			for i in range(2 * listad[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux-=1
			for i in range(2 * listad[k].getRadio()):
				if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux-=1
		posx_aux = self.personaje.getPosicionX() - self.personaje.getRadio()
		posy_aux = self.personaje.getPosicionY() - self.personaje.getRadio()
		for i in range(2 * self.personaje.getRadio()):
			if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
				matriz[posx_aux][posy_aux] = self.personaje.getImagen()
			posx_aux+=1
		for i in range(2 * self.personaje.getRadio()):
			if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
				matriz[posx_aux][posy_aux] = self.personaje.getImagen()
			posy_aux+=1
		for i in range(2 * self.personaje.getRadio()):
			if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
				matriz[posx_aux][posy_aux] = self.personaje.getImagen()
			posx_aux-=1
		for i in range(2 * self.personaje.getRadio()):
			if(posy_aux >= 0 and posy_aux <= self.resy and posx_aux >= 0 and posx_aux <= self.resx):
				matriz[posx_aux][posy_aux] = self.personaje.getImagen()
			posy_aux-=1
		return matriz
