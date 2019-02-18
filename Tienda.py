from Oleada import Oleada
from Mensajes import Mensajes
class Tienda:
	@staticmethod
	def comprar(personaje):
		print(Mensajes.mensajes.get("shop"), Oleada.score)
		opcion =input()
		while (True):
			if (opcion == "1"):
				costo = 100
				print(Mensajes.mensajes.get("cost"), costo)
				if( Oleada.score >= costo ):
					print(Mensajes.mensajes.get("confirm purchase"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVida(personaje.getVida() + 1)
						print(Mensajes.mensajes.get("successful purchase"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("havent enough"))
			elif (opcion == "2"):
				costo = 150
				print(Mensajes.mensajes.get("cost"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirm purchase"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setNumDisparos(personaje.getNumDisparos() + 1)
						print(Mensajes.mensajes.get("successful purchase"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("havent enough"))
			elif (opcion == "3"):
				costo = 100
				print(Mensajes.mensajes.get("cost"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirm purchase"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVidaUtilDisparo(personaje.getVidaUtilDisparo() + 1)
						print(Mensajes.mensajes.get("successful purchase"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("havent enough"))
			elif (opcion == "4"):
				costo = (personaje.getVelocidad()) * 50
				print(Mensajes.mensajes.get("cost"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirm purchase"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setVelocidad(personaje.getVelocidad() + 1)
						print(Mensajes.mensajes.get("successful purchase"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("havent enough"))
			elif (opcion == "5"):
				costo = personaje.getDamage() * 50
				print(Mensajes.mensajes.get("cost"), costo)
				if (Oleada.score >= costo):
					print(Mensajes.mensajes.get("confirm purchase"))
					confirmarcompra = input()
					if (confirmarcompra == "1"):
						Oleada.score = Oleada.score - costo
						personaje.setDamage(personaje.getDamage() + 1)
						print(Mensajes.mensajes.get("successful purchase"), Oleada.score)
				else:
					print(Mensajes.mensajes.get("havent enough"))
			elif (opcion == "6"):
				break;
			opcion = input()
		return personaje