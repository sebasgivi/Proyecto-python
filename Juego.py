from Oleada import Oleada
from Nave import Nave
from Tienda import Tienda
from Opciones import Opciones
from Mensajes import Mensajes
from Mejora import Mejora
from Disparo import Disparo
import random

class Juego:
	

	def __init__(self, pause = True, oleada = Oleada(), personaje = Nave()):
		self._pause = pause
		self._oleada = oleada
		self._personaje = personaje

	def setPause(self):
		if(self.getPause() == True):
			self._pause = False
		else:
			self._pause = True

	def jugar(self):
		self._oleada = Oleada()
		if(input(Mensajes.mensajes.get("random wave")) == "1"):
			self.randomWave()
		self._oleada.crearOleada()
		self._personaje = Nave()
		control_list = Opciones.getControlList()

		while((self._personaje.gameOver()) == False):
				self.graficar()
				opcion = input()
				if(self.getPause() == True):
					if(opcion == control_list[1] or opcion == control_list[2]):
						self._personaje.setDireccion(opcion)
						self.refrescar()
					elif(opcion == control_list[0]):
						for i in range(self._personaje.getVelocidad()):
							self._personaje.avanzar()
							self.colision()
						self.refrescar()
					elif(opcion == control_list[3]):
						if(len(self._personaje.getListaDisparos()) < self._personaje.getNumDisparos()):
							Disparo.crearDisparo(self._personaje.getPosicionX(),self._personaje.getPosicionY(),
						    					 self._personaje.getDireccion(),self._personaje.getVidaUtilDisparo(),
						    					 self._personaje.getDamage(),self._personaje)
							self.refrescar()
					elif(opcion == "p"):
						self.setPause()
						
					else:
						self.refrescar()
				else:
					
					if(opcion == "p"):
						self.setPause()

		print(Mensajes.mensajes.get("game over"))
		if(input() == "1"):
			print(Mensajes.mensajes.get("enter your name"),"Score ",Oleada.score)
			Juego.agregarPuntaje()
		lista = []
		self._personaje = Nave()
		self._oleada.setListaMeteoros(lista) 
		




	def getPause(self):
		return self._pause

	def colision(self):
		pila_m = []
		pila_d = []
		pila_mejoras = []
		for i in range(len(self._oleada.getListaMeteoros())):
			for j in range(i + 1, len(self._oleada.getListaMeteoros())):
				if(self.verificar(self._oleada.getListaMeteoros()[i], self._oleada.getListaMeteoros()[j]) == True):
					self._oleada.getListaMeteoros()[i].setVida(self._oleada.getListaMeteoros()[i].getVida()
											   - self._oleada.getListaMeteoros()[j].getDamage())
					self._oleada.getListaMeteoros()[j].setVida(self._oleada.getListaMeteoros()[j].getVida()
											   - self._oleada.getListaMeteoros()[i].getDamage())
					if(not i in pila_m and
					   self._oleada.getListaMeteoros()[i].getVida() <= 0):
						pila_m.append(i)
					if(not j in pila_m and
					   self._oleada.getListaMeteoros()[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(self._personaje.getListaDisparos())):
			for j in range(len(self._oleada.getListaMeteoros())):
				if(self.verificar(self._personaje.getListaDisparos()[i], self._oleada.getListaMeteoros()[j]) == True):
					self._oleada.getListaMeteoros()[j].setVida(self._oleada.getListaMeteoros()[j].getVida()
											   - self._personaje.getListaDisparos()[i].getDamage())
					if(not i in pila_d):
						pila_d.append(i)
					if(not j in pila_m and
					   self._oleada.getListaMeteoros()[j].getVida() <= 0):
						pila_m.append(j)

		for i in range(len(self._oleada.getListaMeteoros())):
			if(self.verificar(self._personaje, self._oleada.getListaMeteoros()[i])):
				self._personaje.setVida(self._personaje.getVida() - self._oleada.getListaMeteoros()[i].getDamage())
				if(not i in pila_m):
					pila_m.append(i)
					self._oleada.setMeteorosDestruidos(self._oleada.getMeteorosDestruidos() + 1)
		pila_m.sort()
		while(len(pila_m) > 0):
			self._oleada.getListaMeteoros().remove(self._oleada.getListaMeteoros()[pila_m.pop()])
		while(len(pila_d) > 0):
			self._personaje.getListaDisparos().remove(self._personaje.getListaDisparos()[pila_d.pop()])
			Oleada.score+=10
		for i in range(len(Mejora._lista_mejoras)):
			if(self.verificar(self._personaje, Mejora._lista_mejoras[i])):
				Mejora._lista_mejoras[i].calcularMejora()
				if(not i in pila_mejoras):
					pila_mejoras.append(i)
		while(len(pila_mejoras) > 0):
			Mejora._lista_mejoras.remove(Mejora._lista_mejoras[pila_mejoras.pop()])

	def verificar(self, first, second):
		arreglo_first = first.getHitBox()
		arreglo_second = second.getHitBox()
		for i in range(len(arreglo_second)):
			if(arreglo_second[i] in arreglo_first):
				return True
		return False

	def refrescar(self):
		if(len(self._oleada.getListaMeteoros()) > 0):
			vel_m = int(self._oleada.getListaMeteoros()[0].getVelocidad())
			self._oleada.setCantidadDeTurnos(self._oleada.getCantidadDeTurnos() + 1)
			if(self._oleada.getCantidadDeTurnos() % 8 == 0):
				Mejora(random.randrange(0, Opciones.resx),
                       random.randrange(0, Opciones.resy),self._personaje)
			for j in range(vel_m):
				for i in range(len(self._oleada.getListaMeteoros())):
					self._oleada.getListaMeteoros()[i].avanzar()
				self.colision()
			if(len(self._personaje.getListaDisparos()) > 0):
				vel_d = self._personaje.getListaDisparos()[0].getVelocidad()
				for j in range(vel_d):
					for i in range(len(self._personaje.getListaDisparos())):
						self._personaje.getListaDisparos()[i].avanzar()
					self.colision()
			Disparo.reducirVidaUtil(self._personaje)
			if(self._personaje.getVida() == 0):
				return 0
		else:
			if(self._personaje.getVida() == 0):
				return 0
			opcion = 4
			Mejora.borrarMejoras()
			print(Mensajes.mensajes.get("wave completed"))
			while(opcion != "1" and opcion != "2" and opcion != "3"):
				opcion = input()
				if(opcion == "1" or opcion == "2"):
					self._personaje.getListaDisparos().clear()
					if(opcion=="1"):
						self._personaje = Tienda.comprar(self._personaje)
					self._personaje.setPosicionX(int(Opciones.resx/2))
					self._personaje.setPosicionY(int(Opciones.resy/2))
					self._oleada.setNumOleada(self._oleada.getNumOleada()+1)
					self._oleada.crearOleada()
					Mejora._lista_mejoras = []
					self._oleada.setCantidadDeTurnos(0)
				elif(opcion == "3"):
					self._personaje.setVida(0)
		return 0

	def graficar(self):
		print(Mensajes.mensajes.get("data"))
		print(Mensajes.mensajes.get("wave number"),self._oleada.getNumOleada(),Mensajes.mensajes.get("lifes"),self._personaje.getVida(),
			Mensajes.mensajes.get("score"),Oleada.score,Mensajes.mensajes.get("meteorites remaining"),len(self._oleada.getListaMeteoros()),
		    Mensajes.mensajes.get("game paused"),not(self.getPause()),Mensajes.mensajes.get("number of shift"),self._oleada.getCantidadDeTurnos(),
		    Mensajes.mensajes.get("damage") ,self._personaje.getDamage(),Mensajes.mensajes.get("ship speed") , self._personaje.getVelocidad(),
			Mensajes.mensajes.get("ship position"),"(", self._personaje.getPosicionX(),",", self._personaje.getPosicionY(),")",Mensajes.mensajes.get("number shots"), self._personaje.getNumDisparos(),
			Mensajes.mensajes.get("shots life"), self._personaje.getVidaUtilDisparo())
		for i in range(Opciones.resx):
			print("-",end="")
		print("\n")
		matriz = self.imprimirRadios(self._oleada.getListaMeteoros(), self._personaje.getListaDisparos())
		matriz[self._personaje.getPosicionX()][self._personaje.getPosicionY()] = self._personaje.getImagen()
		for i in range( len(self._oleada.getListaMeteoros()) ):
			matriz[self._oleada.getListaMeteoros()[i].getPosicionX()][self._oleada.getListaMeteoros()[i].getPosicionY()] = "O"
		for	i in range( len(self._personaje.getListaDisparos()) ):
			matriz[self._personaje.getListaDisparos()[i].getPosicionX()][self._personaje.getListaDisparos()[i].getPosicionY()] = "*"
			
		for i in range(Opciones.resy + 1):
			print("|",end="")
			for j in range(Opciones.resx + 1):
				if matriz[j][i] == 0:
					print(".",end="")
				else:
					print(matriz[j][i],end="")
			print("|",end="")
			print("\n")
		for i in range(Opciones.resx):
			print("-",end="")
		print("\n")
		if (not(self.getPause()) == True):
			print(Mensajes.mensajes.get("paused"))
		
	def imprimirRadios(self,listam,listad):
		matriz = []
		for i in range(Opciones.resx + 1):
			matriz.append([0] * (Opciones.resy + 1))
		for k in range(len(listam)):
			posx_aux = listam[k].getPosicionX() - listam[k].getMedidaHitBox()
			posy_aux = listam[k].getPosicionY() - listam[k].getMedidaHitBox()
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux+=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux+=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "O"
				posx_aux-=1
			for i in range(2 * listam[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "O"
				posy_aux-=1
		for k in range(len(listad)):
			posx_aux = listad[k].getPosicionX() - listad[k].getMedidaHitBox()
			posy_aux = listad[k].getPosicionY() - listad[k].getMedidaHitBox()
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux+=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux+=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "*"
				posx_aux-=1
			for i in range(2 * listad[k].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "*"
				posy_aux-=1
		for l in range(len(Mejora._lista_mejoras)):
			posx_aux = Mejora._lista_mejoras[l].getPosicionX() - Mejora._lista_mejoras[l].getMedidaHitBox()
			posy_aux = Mejora._lista_mejoras[l].getPosicionY() - Mejora._lista_mejoras[l].getMedidaHitBox()
			for i in range(2 * Mejora._lista_mejoras[l].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "+"
				posx_aux+=1
			for i in range(2 * Mejora._lista_mejoras[l].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "+"
				posy_aux+=1
			for i in range(2 * Mejora._lista_mejoras[l].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "+"
				posx_aux-=1
			for i in range(2 * Mejora._lista_mejoras[l].getMedidaHitBox()):
				if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
					matriz[posx_aux][posy_aux] = "+"
				posy_aux-=1
		posx_aux = self._personaje.getPosicionX() - self._personaje.getMedidaHitBox()
		posy_aux = self._personaje.getPosicionY() - self._personaje.getMedidaHitBox()
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posx_aux+=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posy_aux+=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posx_aux-=1
		for i in range(2 * self._personaje.getMedidaHitBox()):
			if(posy_aux >= 0 and posy_aux <= Opciones.resy and posx_aux >= 0 and posx_aux <= Opciones.resx):
				matriz[posx_aux][posy_aux] = self._personaje.getImagen()
			posy_aux-=1
		return matriz
	
	@staticmethod
	def agregarPuntaje():
		puntajes = open("MejoresPuntajes.txt", "a")
		puntajes2 = open("MejoresPuntajes.txt", "r")
		listaPuntajes = puntajes2.readlines()
		datos = input()[0:5]
		datos += ""
		if (len(listaPuntajes)==0):
			puntajes.write(datos+"\n"+ str(Oleada.score))
		else:
			puntajes.write("\n"+datos+"\n"+ str(Oleada.score))
				
		puntajes2.close()
		puntajes.close()



	def mejoresPuntajes():

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

	def historialJugadores():
		historial = open("MejoresPuntajes.txt", "r")
		lista_his = historial.readlines()
		imprimir_historial = open("historial.txt", "w")
		lista_historial = []
		n = int(float(len(lista_his)/2))
		y = 0
		x = 0
		while y<n:
			buscar = lista_his[x].find("\n")
			tupla = ((lista_his[x][:buscar]),(int(lista_his[x+1])))
			lista_historial.append(tupla)
			listaBorrar = list(tupla)
			listaBorrar.clear()
			x = x + 2
			y = y + 1
		lista_historial = [str(i) for i in lista_historial]
		for x in range(len(lista_historial)):
			imprimir_historial.write(lista_historial[x]+"\n")
		historial.close()
		imprimir_historial.close()
		imprimir_historial = open("historial.txt", "r")
		texto = imprimir_historial.read()
		print(texto)
		imprimir_historial.close()

	def randomWave(self):
		self._oleada = Oleada(random.randrange(0, 10), random.randrange(1, 10),
                              random.randrange(0, 10))
		self._personaje = Nave(random.randrange(0, Opciones.resx),
                               random.randrange(0, Opciones.resy),
                               random.randrange(0, 3))
		Oleada.score = random.randrange(0, 1000)
