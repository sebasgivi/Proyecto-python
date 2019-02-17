from Mensajes import Mensajes
class Opciones:

	resx = 100
	resy = 15
	_controlList = ["w", "a", "d", "f"]

	def changeControls(move, left, right, shot):
		Opciones._controlList = []
		Opciones._controlList.append(move)
		Opciones._controlList.append(left)
		cancelar_cambio = 0
		if (move == left):
			cancelar_cambio = 1 
		Opciones._controlList.append(right)
		if (move == right) or (left == right):
			cancelar_cambio = 1
		Opciones._controlList.append(shot)
		if (move == shot) or (left == shot) or (right == shot):
			cancelar_cambio = 1
		if (cancelar_cambio == 1):

			Opciones._controlList = ["w", "a", "d", "f"]
			print(Mensajes.mensajes.get("unrealized changes"))
	def getControlList():
		return Opciones._controlList

	def changeResolution(resx, resy):
		Opciones.resx = int(resx)
		Opciones.resy = int(resy)

	def changeLanguage():
		print(Mensajes.eleccion_idioma.get("language option"))
		idioma = input()
		if idioma == "1":
			Mensajes.mensajes = Mensajes.español
		else:
			Mensajes.mensajes = Mensajes.ingles


