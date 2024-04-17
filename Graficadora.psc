Algoritmo Graficadora
	Definir x1,y1,x2,y2,deltaX,deltaY,x,e,i,lista como Entero;
	Definir sup como Cadena;
	Definir ctr como Caracter;
	
	Escribir "¿Cuántas líneas desea dibujar?";
	Leer lista;
	
	Escribir "¿Desea que las líneas se superpongan?";
	Leer sup;
	sup <- Minusculas(sup);
	
	Dimension Matriz[100,100] // Matriz para graficar líneas, tamaño arbitrario.
	
	Repetir
		Segun sup
			"no":
				Para z <- 1 Hasta lista Con Paso 1
					Limpiar Pantalla;
					
					// Reiniciar valores de arreglos (Limpieza/Vaciado de Matrices)
					Para e <- 1 Hasta 30 Con Paso 1
						Para x <- 1 Hasta 50 Con Paso 1
							Matriz[e, x] <- "";
						FinPara
					FinPara
					
					// Imprimir la matriz
					Para e <- 1 Hasta 30 Con Paso 1
						Para x <- 1 Hasta 50 Con Paso 1
							ctr <- Matriz[e, x];
							Si ctr = ""
								ctr <- ".";
							FinSi
							Escribir Sin Saltar ctr," ";
						FinPara
						Escribir "";
					FinPara
					
					// Ingreso de coordenadas
					Escribir "LINEA N°",z,"";
					Escribir "Ingrese las coordenadas del punto inicial (X1,Y1)";
					Escribir Sin Saltar "X1: ";
					Leer x1;
					Escribir Sin Saltar "Y1: ";
					Leer y1;
					Si y1 <> 1
						//y1 <- 31 - y1;
					FinSi
					Escribir "Ingrese las coordenadas del punto final (X2,Y2)";
					Escribir Sin Saltar "X2: ";
					Leer x2;
					Escribir Sin Saltar "Y2: ";
					Leer y2;
					Si y2 <> 1
						//y2 <- 31 - y2;
					FinSi
					
					// Calcular la pendiente y la distancia entre los dos puntos
					deltaX <- x2 - x1;
					deltaY <- y2 - y1;
					
					// Si deltaX es 0, dibuja una línea vertical
					Si deltaX = 0
						Para i <- y1 Hasta y2 Con Paso 1
							Matriz[i, x1] <- "O";
						FinPara
						// Si deltaY es 0, dibuja una línea horizontal
					Sino
						Si deltaY = 0
							Para i <- x1 Hasta x2 Con Paso 1
								Matriz[y1, i] <- "O";
							FinPara
						Sino // Dibujar una línea diagonal
							Si deltaX > deltaY
								deltaY <- deltaY * 2;
								deltaX <- deltaX * 2;
								i <- 1
								Mientras i <= deltaX
									x <- x1 + redon(i * deltaX / deltaX);
									e <- y1 + redon(i * deltaY / deltaX);
									Matriz[e, x] <- "O";
									i <- i + 1;
								FinMientras
							Sino
								deltaY <- deltaY * 2;
								deltaX <- deltaX * 2;
								i <- 1
								Mientras i <= deltaY
									x <- x1 + redon(i * deltaX / deltaY);
									e <- y1 + redon(i * deltaY / deltaY);
									Matriz[e, x] <- "O";
									i <- i + 1;
								FinMientras
							FinSi
						FinSi
					FinSi
					
					Limpiar Pantalla;
					
					// Imprimir la matriz
					Para e <- 1 Hasta 30 Con Paso 1
						Para x <- 1 Hasta 50 Con Paso 1
							ctr <- Matriz[e, x];
							Si ctr = ""
								ctr <- ".";
							FinSi
							Escribir Sin Saltar ctr," ";
						FinPara
						Escribir "";
					FinPara
					Escribir "Presione una tecla para continuar...";
					Esperar Tecla;
				FinPara
			"si" o "sí":
				Dimension x1[lista];
				Dimension y1[lista];
				Dimension x2[lista];
				Dimension y2[lista];
				
				Para z <- 1 Hasta lista Con Paso 1
					Limpiar Pantalla;
					
					// Imprimir la matriz
					Para e <- 1 Hasta 30 Con Paso 1
						Para x <- 1 Hasta 50 Con Paso 1
							ctr <- Matriz[e, x];
							Si ctr = ""
								ctr <- ".";
							FinSi
							Escribir Sin Saltar ctr," ";
						FinPara
						Escribir "";
					FinPara
					
					// Ingreso de coordenadas
					Escribir "LINEA N°",z,"";
					Escribir "Ingrese las coordenadas del punto inicial (x1,y1)";
					Escribir Sin Saltar "X1: ";
					Leer x1[z];
					Escribir Sin Saltar "Y1: ";
					Leer y1[z];
					Si y1[z] <> 1
						//y1 <- 31 - y1;
					FinSi
					Escribir "Ingrese las coordenadas del punto final (X2,Y2)";
					Escribir Sin Saltar "X2: ";
					Leer x2[z];
					Escribir Sin Saltar "Y2: ";
					Leer y2[z];
					Si y2[z] <> 1
						//y2[z] <- 31 - y2[z];
					FinSi
					
					// Calcular la pendiente y la distancia entre los dos puntos
					deltaX <- x2[z] - x1[z];
					deltaY <- y2[z] - y1[z];
					
					// Si deltaX es 0, dibuja una línea vertical
					Si deltaX = 0
						Para i <- y1[z] Hasta y2[z] Con Paso 1
							Matriz[i, x1[z]] <- "O";
						FinPara
						// Si deltaY es 0, dibuja una línea horizontal
					Sino
						Si deltaY = 0
							Para i <- x1[z] Hasta x2[z] Con Paso 1
								Matriz[y1[z], i] <- "O";
							FinPara
						Sino // Dibujar una línea diagonal
							Si deltaX > deltaY
								deltaY <- deltaY * 2;
								deltaX <- deltaX * 2;
								i <- 1
								Mientras i <= deltaX
									x <- x1[z] + redon(i * deltaX / deltaX);
									e <- y1[z] + redon(i * deltaY / deltaX);
									Matriz[e, x] <- "O";
									i <- i + 1;
								FinMientras
							Sino
								deltaY <- deltaY * 2;
								deltaX <- deltaX * 2;
								i <- 1
								Mientras i <= deltaY
									x <- x1[z] + redon(i * deltaX / deltaY);
									e <- y1[z] + redon(i * deltaY / deltaY);
									Matriz[e, x] <- "O";
									i <- i + 1;
								FinMientras
							FinSi
						FinSi
					FinSi
					
					Limpiar Pantalla;
					
					// Imprimir la matriz
					Para e <- 1 Hasta 30 Con Paso 1
						Para x <- 1 Hasta 50 Con Paso 1
							ctr <- Matriz[e, x];
							Si ctr = ""
								ctr <- ".";
							FinSi
							Escribir Sin Saltar ctr," ";
						FinPara
						Escribir "";
					FinPara
					Escribir "Presione una tecla para continuar...";
					Esperar Tecla;
				FinPara
			De Otro Modo:
				Escribir "No se reconoce la respuesta ingresada.";
		FinSegun
	Hasta Que sup = "no" o sup = "si" o sup = "sí"
FinAlgoritmo
