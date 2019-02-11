from Mensajes import Mensajes
class Opciones:

	resx = 100
	resy = 15
	_controlList = ["w", "a", "d"]

	def changeControls(up, left, right):
		Opciones._controlList = []
		Opciones._controlList.append(up)
		Opciones._controlList.append(left)
		Opciones._controlList.append(right)

	def getControlList():
		return Opciones._controlList

	def changeResolution(resx, resy):
		Opciones.resx = int(resx)
		Opciones.resy = int(resy)

	def changeLanguage():
		print(Mensajes.eleccion_idioma.get("opciones_idio"))
		idioma = input()
		if idioma == "1":
			Mensajes.mensajes = Mensajes.español
		else:
			Mensajes.mensajes = Mensajes.ingles


