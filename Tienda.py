from Oleada import Oleada
class Tienda:
	@staticmethod
	def comprar(personaje):
		costo = 0
		#SON de LA CLASE MENSJAE, PASAR DESPUES
		print("Bienvenido a la tienda, ¿qué desea comprar?: \n" + 
			  "1) Vida\n" + 
			  "2) Más Disparos\n" + 
			  "3) Vida util de la bala\n" + 
			  "4) Velocidad de la Nave\n" + 
			  "5) Daño del disparo\n" + 
			  "6) Salir\n" + 
			  "Tu Score es: " , Oleada.score)
		opcion =input()
		while (True):
			if (opcion == "1"):
				costo = 100
				print("costo: ", costo)
				if(Oleada.score >= costo ):
					Oleada.score = Oleada.score - costo
					personaje.setVida(personaje.getVida() + 1)
					print("Compra Efectuada, nuevo score: ", Oleada.score)
			elif (opcion == "2"):
				costo = 150
				print("costo: " , costo)
				if (Oleada.score >= costo):
					Oleada.score = Oleada.score - costo
					personaje.setNumDisparos(personaje.getNumDisparos() + 1)
					print("Compra Efectuada, nuevo score: ", Oleada.score)
			elif (opcion == "3"):
				costo = 100
				print("costo: ", costo)
				if (Oleada.score >= costo):
					Oleada.score = Oleada.score - costo
					personaje.setVidaUtilDisparo(personaje.getVidaUtilDisparo() + 1)
					print("Compra Efectuada, nuevo score: ", Oleada.score)
			elif (opcion == "4"):
				costo = (personaje.getVelocidad()) * 50
				print("costo: ", costo)
				if (Oleada.score >= costo):
					Oleada.score = Oleada.score - costo
					personaje.setVel(personaje.getVelocidad() + 1)
					print("Compra Efectuada, nuevo score: ", Oleada.score)
			elif (opcion == "5"):
				costo = personaje.getDamage() * 50
				print("costo: ", costo)
				if (Oleada.score >= costo):
					Oleada.score = Oleada.score - costo
					personaje.setDamage(personaje.getDamage() + 1)
					print("Compra Efectuada, nuevo score: ", Oleada.score)
			elif (opcion == "6"):
				break;
			opcion = input()
		return personaje