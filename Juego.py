import msvcrt
import time
from Oleada import Oleada
from Nave import Nave
from Tienda import Tienda
from Resolution import Resolution
from Mensajes import Mensajes
from Mejora import Mejora

class Juego:
	

	def __init__(self, estado_juego = True, oleada = Oleada(), personaje = Nave()):
		self._estado_juego = estado_juego
		self._oleada = oleada
		self._personaje = personaje

	def idioma():
		print(Mensajes.eleccion_idioma.get("opciones_idio"))
		idioma = input()
		if idioma == "1":
			Mensajes.mensajes = Mensajes.español
		else:
			Mensajes.mensajes = Mensajes.ingles

	def setEstadoJuego(self):
		if(self.getEstadoJuego() == True):
			self._estado_juego = False
		else:
			self._estado_juego = True

	def jugar(self):
		self._oleada = Oleada()
		self._oleada.crearMeteoritos()
		self._personaje = Nave()
		self._oleada.crearMeteoritos()
		
		while((self._personaje.gameOver()) == False):
			if(self.getEstadoJuego()):

				self.graficar()
				opcion = input()
				if(self.getEstadoJuego() == True):
					if(opcion == "a" or opcion == "d"):
						self._personaje.setDireccion(opcion)
						self.refrescar()
					elif(opcion == "w"):
						for i in range(self._personaje.getVelocidad()):
							self._personaje.avanzar()
							self.colision()
						self.refrescar()
					elif(opcion == "f"):
						if(len(Nave.disparos) < self._personaje.getNumDisparos()):
							self._personaje.crearDisparo()
							self.refrescar()
					elif(opcion == "p"):
						self.setEstadoJuego()
						print(Mensajes.mensajes.get("estadojuegoactual"))
					else:
						self.refrescar()
				else:
					if(opcion == "p"):
						self.setEstadoJuego()
			else:
				if(self.getEstadoJuego() == True):
					self.refrescar()
		print(Mensajes.mensajes.get("GameOver"))
		if(input() == "1"):
			print(Mensajes.mensajes.get("IngreseSuNombre"),"Score ",Oleada.score)
			Juego.AgregarPuntaje()
		self._personaje = Nave()
		self._oleada.meteoros = []
		Nave.disparos = []




	def getEstadoJuego(self):
		return self._estado_juego

	def colision(self):
		pila_m = []
		pila_d = []
		for i in range(len(self._oleada.meteoros)):
			for j in range(i + 1, len(self._oleada.meteoros)):
				if(self.verificar(self._oleada.meteoros[i], self._oleada.meteoros[j]) == True):
					self._oleada.meteoros[i].setVida(self._oleada.meteoros[i].getVida()
											   - self._oleada.meteoros[j].getDamage())
					self._oleada.meteoros[j].setVida(self._oleada.meteoros[j].getVida()
											   - self._oleada.meteoros[i].getDamage())
					if(not i in pila_m and
					   self._oleada.meteoros[i].getVida() <= 0):
						pila_m.append(i)
					if(not j in pila_m and
					   self._oleada.meteoros[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(Nave.disparos)):
			for j in range(len(self._oleada.meteoros)):
				if(self.verificar(Nave.disparos[i], self._oleada.meteoros[j]) == True):
					self._oleada.meteoros[j].setVida(self._oleada.meteoros[j].getVida()
											   - Nave.disparos[i].getDamage())
					if(not i in pila_d):
						pila_d.append(i)
					if(not j in pila_m and
					   self._oleada.meteoros[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(self._oleada.meteoros)):
			if(self.verificar(self._personaje, self._oleada.meteoros[i])):
				self._personaje.setVida(self._personaje.getVida() - self._oleada.meteoros[i].getDamage())
				if(not i in pila_m):
					pila_m.append(i)
					self._oleada.setMeteorosDestruidos(self._oleada.getMeteorosDestruidos() + 1)
		while(len(pila_m) > 0):
			self._oleada.meteoros.remove(self._oleada.meteoros[pila_m.pop()])
		while(len(pila_d) > 0):
			Nave.disparos.remove(Nave.disparos[pila_d.pop()])
			Oleada.score+=10

	def verificar(self, first, second):
		arreglo_first = first.getHitBox()
		arreglo_second = second.getHitBox()
		for i in range(len(arreglo_second)):
			if(arreglo_second[i] in arreglo_first):
				return True
		return False

	def refrescar(self):
		if(len(self._oleada.meteoros) > 0):
			vel_m = int(self._oleada.meteoros[0].getVelocidad())
			self._oleada.setCantidadDeTurnos(self._oleada.getCantidadDeTurnos() + 1)
			for j in range(vel_m):
				for i in range(len(self._oleada.meteoros)):
					self._oleada.meteoros[i].avanzar()
				self.colision()
			if(len(Nave.disparos) > 0):
				vel_d = Nave.disparos[0].getVelocidad()
				for j in range(vel_d):
					for i in range(len(Nave.disparos)):
						Nave.disparos[i].avanzar()
					self.colision()
			Nave.reducir_vu()
			if(self._personaje.getVida() == 0):
				return 0
		else:
			if(self._personaje.getVida() == 0):
				return 0
			opcion = 4
			print(Mensajes.mensajes.get("oleada completa"))
			#self._personaje = Mejora.ENSAYO(self._personaje)
			while(opcion != "1" and opcion != "2" and opcion != "3"):
				opcion = input()
				if(opcion == "1" or opcion == "2"):
					Nave.disparos = []
					if(opcion=="1"):
						self._personaje = Tienda.comprar(self._personaje)
					self._personaje.setPosicionX(int(Resolution.resx/2))
					self._personaje.setPosicionY(int(Resolution.resy/2))
					self._oleada.setNumOleada(self._oleada.getNumOleada()+1)
					self._oleada.crearMeteoritos()
				elif(opcion == "3"):
					self._personaje.setVida(0)
		return 0

	def graficar(self):
		print(Mensajes.mensajes.get("datos"))
		print(Mensajes.mensajes.get("numero oleada"),self._oleada.getNumOleada(),Mensajes.mensajes.get("vidas"),self._personaje.getVida(),
			Mensajes.mensajes.get("puntaje"),Oleada.score,Mensajes.mensajes.get("meteoros restantes"),len(self._oleada.meteoros),
		    Mensajes.mensajes.get("estado juego"),self.getEstadoJuego(),Mensajes.mensajes.get("cantidad turnos"),self._oleada.getCantidadDeTurnos(),
		    Mensajes.mensajes.get("dano") ,self._personaje.getDamage(),Mensajes.mensajes.get("velocidad nave") , self._personaje.getVelocidad(),
			Mensajes.mensajes.get("posicion nave"),"(", self._personaje.getPosicionX(),",", self._personaje.getPosicionY(),")", 
			Mensajes.mensajes.get("tamano nave"), self._personaje.getMedidaHitBox(),Mensajes.mensajes.get("numero de disparos"), self._personaje.getNumDisparos(),
			Mensajes.mensajes.get("vidaudisparo"), self._personaje.getVidaUtilDisparo())
		for i in range(Resolution.resx):
			print("-",end="")
		print("\n")
		matriz = self.imprimirRadios(self._oleada.meteoros, Nave.disparos)
		matriz[self._personaje.getPosicionX()][self._personaje.getPosicionY()] = self._personaje.getImagen()
		for i in range( len(self._oleada.meteoros) ):
			matriz[self._oleada.meteoros[i].getPosicionX()][self._oleada.meteoros[i].getPosicionY()] = "O"
		for	i in range( len(Nave.disparos) ):
			matriz[Nave.disparos[i].getPosicionX()][Nave.disparos[i].getPosicionY()] = "*"
			
		for i in range(Resolution.resy + 1):
			print("|",end="")
			for j in range(Resolution.resx + 1):
				if matriz[j][i] == 0:
					print(".",end="")
				else:
					print(matriz[j][i],end="")
			print("|",end="")
			print("\n")
		for i in range(Resolution.resx):
			print("-",end="")
		print("\n")
		
	def imprimirRadios(self,listam,listad):
		matriz = []
		for i in range(Resolution.resx + 1):
			matriz.append([0] * (Resolution.resy + 1))
		for k in range(len(listam)):
			posx_aux = listam[k].getPosicionX() - listam[k].getMedidaHitBox()
			posy_aux = listam[k].getPosicionY() - listam[k].getMedidaHitBox()
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux+=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux+=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux-=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux-=1
		for k in range(len(listad)):
			posx_aux = listad[k].getPosicionX() - listad[k].getMedidaHitBox()
			posy_aux = listad[k].getPosicionY() - listad[k].getMedidaHitBox()
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux+=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux+=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux-=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux-=1
		posx_aux = self._personaje.getPosicionX() - self._personaje.getMedidaHitBox()
		posy_aux = self._personaje.getPosicionY() - self._personaje.getMedidaHitBox()
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posx_aux+=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posy_aux+=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posx_aux-=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Resolution.resy and posx_aux >= 0 and posx_aux <= Resolution.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posy_aux-=1
		return matriz
	"""def ImprimirDatosNave(self):
		print("Vidas: ",self._personaje.getVida() ,"Daño: " , self._personaje.getDamage(),
			   "Velociada: " , self._personaje.getVelocidad(),
			   "pociciones: \n         Y: ", self._personaje.getPosicionY(), 
			    "       X:", self._personaje.getPosicionX(), 
			      "MEdida hitbox: ", self._personaje.getMedidaHitBox(),
			      "numero de disparos: ", self._personaje.getNumDisparos(),"vidadisparo: ", self._personaje.getVidaUtilDisparo())
	"""
	@staticmethod
	def AgregarPuntaje():
		puntajes = open("MejoresPuntajes.txt", "a")
		datos = input()[0:5]
		datos += ""
		puntajes.write(datos+"\n"+ str(Oleada.score))
		puntajes.close()


	def MejoresPuntajes():

		puntajes = open("MejoresPuntajes.txt", "r")
		lista_pun = puntajes.readlines()

		lista_puntajes = []
		n = int(float(len(lista_pun)/2))
		y = 0
		x = 0
		while y<n:
			buscar = lista_pun[x].find("\n")
			tupla = ((lista_pun[x][:buscar]),(int(lista_pun[x+1])))
			lista_puntajes.append(tupla)
			listaBorrar = list(tupla)
			listaBorrar.clear()
			x = x + 2
			y = y + 1
		puntajes.close()
		lista_puntajes.sort(key=lambda puntajes: puntajes[1], reverse = True)
		lista_puntajes = [str(i) for i in lista_puntajes]
		puntajesTop = open("puntajesTop.txt","w")

		if len(lista_puntajes)>5:
			for x in range(5):
				puntajesTop.write(str(x+1) +" " +lista_puntajes[x]+"\n")
		else:
			for x in range(len(lista_puntajes)):
				puntajesTop.write(str(x+1) +" "+ lista_puntajes[x]+"\n")
		puntajesTop.close()

		puntajesTop = open("puntajesTop.txt","r")
		texto = puntajesTop.read()
		print(texto)
		puntajesTop.close()
