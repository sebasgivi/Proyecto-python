class Mensajes:

	mensajes= {}

	eleccion_idioma = {"language option":"IDIOMA:\n1. ESPAÑOL\n2. INGLES\n"
					   "Por favor seleccione un idioma: "}
	español = { "menu":
"""             |---------------------------------------------------------------------------------|
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
				4)Opciones
				5)Salir""",
				"option menu":"Ingrese una opcion: ",
				"instruction":"INSTRUCCIONES",
				"top scores": "TOP PUNTAJES:",
				"options" : "1) Cambiar Resolucion del Juego\n2) Cambiar Controles\n3) Cambiar Idioma\n",
				"end game":"Fin del Juego",
				"paused":"El juego se encuentra en Pausa, presione P para seguir jugando",
				"wave completed":
				"""Oleada Completada, Desea visitar la tienda?
				   1)Si
				   2)No
				   3)Finalizar""",
				"data":"|||DATOS DEL JUEGO:|||",
				"wave number":"|||   Oleada Numero: ",
				"lifes":"  |||   Vidas: ",
				"score":"  |||   Puntaje: ",
				"meteorites remaining":"  |||   Meteoros Restantes: ",
				"game paused":"\n|||   Juego en pausa: ",
				"number of shift":"  |||   Cantidad de turnos: ",
				"damage":"  |||   Daño del disparo:",
				"ship speed":"\n|||   Velocidad de la nave:",
				"ship position":"  |||   Posicion de la nave:",
				"number shots": "\n|||   Numero de disparos maximos al tiempo:",
				"shots life":"  |||   Alcance maximo de los disparos:",
				"shop":
				"""Bienvenido a la tienda, ¿qué desea comprar?: 
			  	   1) Vidas
			 	   2) Más Disparos
			       3) Alcance maximo de los disparos
			       4) Velocidad de la Nave
			       5) Daño del disparo
			       6) Salir
			       Tu puntaje es: """, 
			    "cost":"Costo: " ,
			    "havent enough":"No tienes suficientes puntos",
			    "confirm purchase":"¿Esta seguro que desea comprar esta mejora?\n 1) Si \n 2) regresar",
			    "successful purchase":"Compra Exitosa, su nuevo puntaje es: ",
			    "game over":"Fin del juego, Desea Ingresar su puntaje?\n1)Si 2)No: ",
                "enter your name":"Ingrese su nombre(max 5 caracteres)",
                "resx":"Ingrese la resolucion del juego en X ",
                "resy":"Ingrese la resolucion del juego en Y ",
                "move":"Avanzar ",
                "left":"Izquierda ",
                "right":"Derecha ",
                "shot":"Disparo ",
                "unrealized changes": "Los cambios no se han guardado porque asignaste la misma letra en dos controles diferentes",
                "random wave":"Desea iniciar una partida aleatoria?\n1)Si\n2)No\n ",
                "temporary life":"Mejora temporal de vida",
                "temporary shots":"Mejora temporal de Disparos",
                "temporary life bullet":"Mejora temporal de vida de la bala",
                "temporary ship speed":"Mejora temporal de velocidad de la nave",
                "temporary damage":"mejora temporal del damage de la bala",
                "put me 5":"JUEGO tERMINADO; Pongame 5.0"}

	ingles = { "menu":
"""				|---------------------------------------------------------------------------------|
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
				4)Options
				5)Exit""",
				"option menu":"Enter  option: ",
				"instructions":"INSTRUCTIONS",
				"top scores": "TOP SCORES:",
				"options" : "1) Change Game Resolution\n2) Change Game Controls\n3) Change Game Language\n",
				"end game":"Game over",
				"paused":"The game is paused, press P to continue playing",
				"wave completed": 
				"""Wave completed, Do you want to visit the store?
				   1)Yes 
				   2)No 
				   3)Finish""",
				"data":"|||DATOS DEL JUEGO:|||",
				"wave number":"|||   Wave number: ",
				"lifes":"  |||   Lifes: ",
				"score":"  |||  Score: ",
				"meteorites remaining":"  |||   Meteorites remaining: ",
				"game paused":"\n|||   Game paused: ",
				"number of shift":"  |||   Number of shift: ",
				"damage":"  |||   Shot damage:",
				"ship speed":"\n|||   Ship speed:",
				"ship position":"  |||   Ship position:",
				"number shots": "\n|||   Number of maximum shots at time:",
				"shots life":"  |||   Maximum range of shots:",
				"shop":
				"""Welcome to the store, what do you want to buy?: 
			  	   1) Life
			 	   2) More shots
			       3) Life of the bullet
			       4) Ship speed
			       5) Shot damage
			       6) Exit
			       Your Score is: """, 
			    "cost":"Cost: " ,
			    "confirm purchase":"Sure you want to buy this improvement? \n 1) Sure \n 2) Back",
			    "havent enough":"You do havent enough points ",
			    "successful purchase":"Successful purchase",
			    "game over":"GameOver, Do you want to add your score?\n1)Yes 2)No: ",
                "enter your name":"enter your username(max 5 char)",
                "resx":"Enter the resolution of the game in X ",
                "resy":"Enter the resolution of the game in Y ",
                "move":"move ",
                "left":"Left ",
                "right":"Right ",
                "shot":"Shot ",
                "unrealized changes": "The changes havent been saved because you assigned the same letter in two different controls",
                "random wave":"Do you want to start a random game?\n1)Yes\n2)No\n",
                "temporary life":"temporary improvement of life",
                "temporary shots":"temporary improvement of Shoots",
                "temporary life bullet":"temporary improvement of Life Bullet",
                "temporary ship speed":"temporary improvement of Speed",
                "temporary damage":"temporary improvement of Damage",
                "put me 5":"END GAME; Rate me 5.0"}