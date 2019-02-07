from Oleada import Oleada
from Mensajes import Mensajes
class Tienda:
	@staticmethod
	def comprar(personaje):
		costo = 0
		#SON de LA CLASE MENSJAE, PASAR DESPUES
		print(Mensajes.mensajes.get("tienda"), Oleada.score)
		opcion =input()
		while (True):
			if (opcion == "1"):
				costo = 100
				print(Mensajes.mensajes.get("costo"), costo)
				if( Oleada.score >= costo ):
					print(Mensajes.mensajes.get("confirmar compra"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVida(personaje.getVida() + 1)
						print(Mensajes.mensajes.get("compra exitosa"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("notealcanza"))
			elif (opcion == "2"):
				costo = 150
				print(Mensajes.mensajes.get("costo"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirmar compra"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setNumDisparos(personaje.getNumDisparos() + 1)
						print("Compra Efectuada, nuevo score: ", Oleada.score)
				else:
					print(Mensajes.mensajes.get("notealcanza"))
			elif (opcion == "3"):
				costo = 100
				print(Mensajes.mensajes.get("costo"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirmar compra"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVidaUtilDisparo(personaje.getVidaUtilDisparo() + 1)
						print("Compra Efectuada, nuevo score: ", Oleada.score)
				else:
					print(Mensajes.mensajes.get("notealcanza"))
			elif (opcion == "4"):
				costo = (personaje.getVelocidad()) * 50
				print("costo", costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirmar compra"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVel(personaje.getVelocidad() + 1)
						print("Compra Efectuada, nuevo score: ", Oleada.score)
				else:
					print(Mensajes.mensajes.get("notealcanza"))
			elif (opcion == "5"):
				costo = Disparo.getDamage() * 50
				print("costo", costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirmar compra"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setDamage(personaje.getDamage() + 1)
						print("Compra Efectuada, nuevo score: ", Oleada.score)
				else:
					print(Mensajes.mensajes.get("notealcanza"))
			elif (opcion == "6"):
				break;
			opcion = input()
		return personaje