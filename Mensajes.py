class Mensajes:

	mensajes= {}

	eleccion_idioma = {"opciones_idio":"IDIOMA:\n1. ESPAÑOL\n2. INGLES\n"
					   "Por favor seleccione un idioma: "}
	español = { "menu":
"""                |---------------------------------------------------------------------------------|
				|                                                                                 |
				|         *     *  *****  *****  *****  ***   ****   ***  *****  ***    ***       |
				|         **   **  *        *    *     *   *  *   *   *     *   *    * *   *      |
				|         *  *  *  *        *    *     *   *  *   *   *     *   *    * *          |
				|         *  *  *  ****     *    ****  *   *  ****    *     *   *    *  ***       |
				|         *     *  *        *    *     *   *  * *     *     *   *    *     *      |
				|         *     *  *        *    *     *   *  *  *    *     *   *    * *   *      |
				|         *     *  *****    *    *****  ***   *   *  ***    *    ***    ***       |
				|                                                                                 |
				|                                      *   *   ***                                |
				|                                      *   *  *                                   |
				|-------------------------------------  * *    **  -------------------------------|
				|                                       * *       *                               |
				|                                        *     ***                                |
				|                                                                                 |
				|                               *   *   ***   *    * *****                        |
				|                               *   *  *   *  *    * *                            |
				|                               **  *  *   *  *    * *                            |
				|                               * * *  *   *   *  *  ****                         |
				|                               *  **  *****   *  *  *                            |
				|                               *   *  *   *   *  *  *                            |
				|                               *   *  *   *    *    *****                        |
				|---------------------------------------------------------------------------------|
				1)Jugar
				2)Instrucciones
				3)Puntajes
				4)Salir""",
				"opcion":"Ingrese una opcion: ",
				"instrucciones":"INSTRUCCIONES",
				"top puntajes": "TOP PUNTAJES:",
				"fin juego":"Fin del Juego",
				"estadojuegoactual":"El juego se encuentra en Pausa, presione P para seguir jugando",
				"oleada completa":
				"""Oleada Completada, Desea visitar la tienda?
				   1)Si
				   2)No
				   3)Finalizar""",
				"datos":"|||DATOS DEL JUEGO:|||",
				"numero oleada":"|||   Oleada Numero: ",
				"vidas":"  |||   Vidas: ",
				"puntaje":"  |||   Puntaje: ",
				"meteoros restantes":"  |||   Meteoros Restantes: ",
				"estado juego":"\n|||   Estado del Juego: ",
				"cantidad turnos":"  |||   Cantidad de turnos: ",
				"dano":"  |||   Daño del disparo:",
				"velocidad nave":"\n|||   Velocidad de la nave:",
				"posicion nave":"  |||   Posicion de la nave:",
				"tamano nave":"  |||   Tamaño de la nave:",
				"numero de disparos": "\n|||   Numero de disparos maximos al tiempo:",
				"vidaudisparo":"  |||   Alcance maximo de los disparos:",
				"tienda":
				"""Bienvenido a la tienda, ¿qué desea comprar?: 
			  	   1) Vidas
			 	   2) Más Disparos
			       3) Alcance maximo de los disparos
			       4) Velocidad de la Nave
			       5) Daño del disparo
			       6) Salir
			       Tu puntaje es: """, 
			    "costo":"Costo: " ,
			    "notealcanza":"No tienes suficientes puntos",
			    "confirmar compra":"¿Esta seguro que desea comprar esta mejora?\n 1) Si \n 2) regresar",
			    "compra exitosa":"Compra Exitosa, su nuevo puntaje es: ",
			    "GameOver":"Fin del juego, Desea Ingresar su puntaje?\n1)Si 2)No: ",
                "IngreseSuNombre":"Ingrese su nombre(max 5 caracteres)"}

	ingles = { "menu":
			 """|---------------------------------------------------------------------------------|
				|                                                                                 |
				|         *     *  *****  *****  *****  ***   ****   ***  ***** *****    ***      |
				|         **   **  *        *    *     *   *  *   *   *     *   *       *   *     |
				|         *  *  *  *        *    *     *   *  *   *   *     *   *       *         |
				|         *  *  *  ****     *    ****  *   *  ****    *     *   *****    ***      |
				|         *     *  *        *    *     *   *  * *     *     *   *           *     |
				|         *     *  *        *    *     *   *  *  *    *     *   *       *   *     |
				|         *     *  *****    *    *****  ***   *   *  ***    *   *****    ***      |
				|                                                                                 |
				|                                      *   *   ***                                |
				|                                      *   *  *                                   |
				|-------------------------------------  * *    **  -------------------------------|
				|                                       * *       *                               |
				|                                        *     ***                                |
				|                                                                                 |
				|                                ***   *    *   ***  *****                        |
				|                               *   *  *    *    *   *   *                        |
				|                               *      *    *    *   *   *                        |
				|                                ***   ******    *   *****                        |
				|                                   *  *    *    *   *                            |
				|                               *   *  *    *    *   *                            |
				|                                ***   *    *   ***  *                            |
				|---------------------------------------------------------------------------------|
				1)Play
				2)Instructions
				3)Scores
				4)Exit""",
				"opcion":"Enter  option: ",
				"instrucciones":"INSTRUCTIONS",
				"top puntajes": "TOP SCORES",
				"fin juego":"Game over",
				"oleada completa": 
				"""Wave completed, Do you want to visit the store?
				   1)Yes 2)No 3)Finish""",
				"numero oleada":"Wade Number: ",
				"vidas":" Lives: ",
				"puntaje":"Score: ",
				"meteoros restantes":"Meteors remaining: ",
				"estado juego":" State Game: ",
				"cantidad turnos":"Turns Number",
				"tienda":
				"""Welcome to the store, what do you want to buy?: 
			  	   1) Life
			 	   2) More shots
			       3) Life of the bullet
			       4) Ship speed
			       5) Shot damage
			       6) Exit
			       Your Score is: """, 
			    "costo":"Cost: " ,
			    "compra exitosa":"Successful purchase",
			    "GameOver":"GameOver, Do you want to add your score?\n1)Yes 2)No: ",
                "IngreseSuNombre":"enter your username(max 5 char)"}