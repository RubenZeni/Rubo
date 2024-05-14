//============================ ALGORITMO PRINCIPAL ============================//
Algoritmo TrabajosPracticos
	
	Limpiar Pantalla;
	Escribir "Antes de comenzar ejecución, por favor amplíe el tamaño de la ventana de la consola -si es posible-, esto se debe a que la interfaz del programa es un poco más grande que el tamaño predeterminado de la ventana.";
	Escribir "";
	Escribir "Puede Maximizar la ventana o simplemente ampliar los bordes o esquinas de la misma, en caso que no sea posible puede intentar reducir el tamaño de CTRL + (Rueda hacia abajo) o CTRL + (Tecla -).";
	Escribir "";
	Escribir "Una vez que haya realizado este paso o si desea continuar, presione cualquier tecla...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Definir Menu_TP,Menu_TP1_S,Menu_TP2_S como Entero;
	
	Repetir
		Menu_S <- Menu;
		Segun Menu_S
			1:
				Repetir
					Menu_TP1_S <- Menu_TP1;
				Hasta Que Menu_TP1_S = 100 o Menu_TP1_S = 1
			2:
				Repetir
					Menu_TP2_S <- Menu_TP2;
				Hasta Que Menu_TP2_S = 100 o Menu_TP2_S = 1
		FinSegun
	Hasta Que Menu_S = 0 o Menu_TP1_S = 1 o Menu_TP2_S = 1
	
	Escribir "Gracias por ejecutar mi código!";
	Escribir "Que tenga un buen día :)";
	Escribir "";
	Escribir "Presione una tecla para finalizar la ejecución...";
	Esperar Tecla;
	
	Limpiar Pantalla;
	
FinAlgoritmo
//==============================================================================//


//=============================== MENU PRINCIPAL ===============================//
Funcion Menu_S <- Menu
	
	Definir op como Entero;
	
	Repetir
		
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "|     Universidad Autónoma De Entre Ríos       |";
		Escribir "|      Facultad de Ciencia y Tecnología        |";
		Escribir "| Licenciatura en Sistemas de Información (TM) |";
		Escribir "|             Alumno: Rubén Zeni               |";
		Escribir "|         Profesora: Fernanda Gavet            |";
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "|               Trabajo Práctico               |";
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "";
		Escribir "Seleccione el trabajo práctico que desee explorar:";
		Escribir "";
		Escribir "1. Trabajo Práctico N° 1: Entender el Problema";
		Escribir "";
		Escribir "2. Trabajo Práctico N° 2: Estrategia";
		Escribir "";
		Escribir "0. SALIR";
		Leer Menu_S;
		
		Si Menu_S <> 1 y Menu_S <> 2 y Menu_S <> 0
			Escribir "La opción seleccionada no es válida.";
			Escribir "";
			Escribir "Presione una tecla para continuar...";
			Esperar Tecla;
			Limpiar Pantalla;
			op <- 1;
		SiNo
			op <- 0;
		FinSi
		
		Limpiar Pantalla;
		
	Hasta Que op = 0
	
FinFuncion
//==============================================================================//


//================================ MENU del TP1 ================================//
Funcion Menu_TP1_S <- Menu_TP1
	
	Definir op como Entero;
	Definir Seleccion,Resolucion2_S como Real;
	
	Repetir
		
		Marco_TP1;
		Escribir "Seleccione el ejercicio/archivo que desee explorar:";
		Escribir "";
		Escribir "1. Catetos_Hipotenusa.psc";
		Escribir "2. HorasValor_Sueldo.psc";
		Escribir "3. AB_MayorAB.psc";
		Escribir "4. Palabra_Palindromo.psc";
		Escribir "5. SieteCalificaciones_Promedio.psc";
		Escribir "6. CuatroNumeros_3enLista.psc";
		Escribir "7. Monto_Total.psc";
		Escribir "8. Numero3Digitos_Armstrong.psc";
		Escribir "";
		Escribir "100. VOLVER";
		Escribir "0. SALIR";
		Leer op;
		
		Limpiar Pantalla;
		Marco_TP1;
		
		Según op
	1:
		Escribir "Enunciado:";
		Escribir "Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Catetos_Hipotenusa;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	2:
		Escribir "Enunciado:";
		Escribir "Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que sueldo percibe dicho operario.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				HorasValor_Sueldo;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	3:
		Escribir "Enunciado:";
		Escribir "Dados dos valores A y B distintos, determinar cuál es el mayor.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				AB_MayorAB;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	4:
		Escribir "Enunciado:";
		Escribir "Determinar si una palabra cualquiera es un palíndromo (capicúa); por ejemplo: Neuquen.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Palabra_Palindromo;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	5:
		Escribir "Enunciado:";
		Escribir "Dadas las calificaciones de 7 exámenes finales de un estudiante determinar el promedio.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				SieteCalificaciones_Promedio;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	6:
		Escribir "Enunciado:";
		Escribir "Dada una lista de 4 números determinar si el Nº 3 se encuentra en dicha lista.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				CuatroNumeros_3enLista;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	7:
		Escribir "Enunciado:";
		Escribir "Calcular el valor a cancelar de un producto de un monto ingresado, el programa debe mostrar cómo se presenta en una factura, subtotal (cantidad por precio), IVA (del subtotal) y total a pagar (la suma del subtotal + el IVA). Use de IVA el 21%.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Monto_Total;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	8:
		Escribir "Enunciado:";
		Escribir "Escriba un programa que permita el ingreso de un número de tres dígitos y determine si es un número Armstrong (ej. 153, 371). Como el número que se ingresa posee 3 dígitos, la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Numero3Digitos_Armstrong;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	100:
		Menu_TP1_S <- 100;
	0:
		Menu_TP1_S <- 1;
	De Otro Modo:
		Escribir "La opción seleccionada no es válida.";
		Escribir "";
		Escribir "Presione una tecla para continuar al menú principal...";
		Esperar Tecla;
		Limpiar Pantalla;
FinSegun

Limpiar Pantalla;

Hasta Que op = 0 o op = 100

FinFuncion	
//==============================================================================//


//================================ MENU del TP2 ================================//
Funcion Menu_TP2_S <- Menu_TP2
	
	Definir op como Entero;
	Definir Seleccion,Resolucion2_S como Real;
	
	Repetir
		
		Marco_TP2;
		Escribir "Seleccione el ejercicio/archivo que desee explorar:";
		Escribir "";
		Escribir "1. DosNumerosPositivos_PrimosRelativos.psc";
		Escribir "2. ValoresNumericos_Rango.psc";
		Escribir "3. Instruccion_EscuchaSpotify.psc";
		Escribir "4. Instruccion_BañarPerro.psc";
		Escribir "5. Instruccion_NotaManuscrita.psc";
		Escribir "6. Instruccion_AuxilioRiesgo.psc";
		Escribir "";
		Escribir "100. VOLVER";
		Escribir "0. SALIR";
		Leer op;
		
		Limpiar Pantalla;
		Marco_TP2;
		
		Según op
	1:
		Escribir "Enunciado:";
		Escribir "Determinar si dos números enteros positivos son primos relativos (esto es si no tienen divisores comunes con excepción del número 1).";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				DosNumerosPositivos_PrimosRelativos;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	2:
		Escribir "Enunciado:";
		Escribir "Dada una lista de valores numéricos, hallar su rango, es decir, la diferencia entre su valor máximo y su valor mínimo.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				ValoresNumericos_Rango;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	3:
		Escribir "Enunciado:";
		Escribir "Indique como escucha su canción favorita en Spotify.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Instruccion_EscuchaSpotify;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	4:
		Escribir "Enunciado:";
		Escribir "Escriba en forma imperativa las instrucciones que le daría a una persona para bañar a un perro/a.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Instruccion_BañarPerro;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	5:
		Escribir "Enunciado:";
		Escribir "Escriba en forma imperativa las instrucciones a seguir para escribir una nota manuscrita.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Instruccion_NotaManuscrita;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	6:
		Escribir "Enunciado:";
		Escribir "Escriba las instrucciones a seguir para pedir auxilio ante una situación de riesgo.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Instruccion_AuxilioRiesgo;
				Resolucion2_S <- Resolucion2;
			Hasta Que Resolucion2_S = 0
		FinSi
	100:
		Menu_TP2_S <- 100;
	0:
		Menu_TP2_S <- 1;
	De Otro Modo:
		Escribir "La opción seleccionada no es válida.";
		Escribir "";
		Escribir "Presione una tecla para continuar al menú principal...";
		Esperar Tecla;
		Limpiar Pantalla;
FinSegun

Limpiar Pantalla;

Hasta Que op = 0 o op = 100

FinFuncion	
//==============================================================================//


//================================ MARCO de TP 1 ===============================//
Funcion Marco_TP1
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "|     Universidad Autónoma De Entre Ríos       |";
	Escribir "|      Facultad de Ciencia y Tecnología        |";
	Escribir "| Licenciatura en Sistemas de Información (TM) |";
	Escribir "|             Alumno: Rubén Zeni               |";
	Escribir "|         Profesora: Fernanda Gavet            |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "| Trabajo Práctico N°1 | Entender El Problema  |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "";
FinFuncion
//==============================================================================//


//================================ MARCO de TP 2 ===============================//
Funcion Marco_TP2
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "|     Universidad Autónoma De Entre Ríos       |";
	Escribir "|      Facultad de Ciencia y Tecnología        |";
	Escribir "| Licenciatura en Sistemas de Información (TM) |";
	Escribir "|             Alumno: Rubén Zeni               |";
	Escribir "|         Profesora: Fernanda Gavet            |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "|      Trabajo Práctico N°2 | Estrategia       |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "";
FinFuncion
//==============================================================================//


//================================ RESOLUCIÓN 1 ===============================//
Funcion Resolucion1_S <- Resolucion1
	Escribir "";
	Escribir "¿Desea ver la resolución del problema? (SI/NO)";
	Leer op;
	
	op <- Minusculas(op);
	
	Segun op
		"si" o "sí":
			Resolucion1_S <- 1;
		"no": 
			Resolucion1_S <- 0;
	FinSegun
FinFuncion
//==============================================================================//


//================================ RESOLUCIÓN 2 ===============================//
Funcion Resolucion2_S <- Resolucion2
	Escribir "";
	Escribir "¿Desea volver a ver la resolución del problema? (SI/NO)";
	Leer op;
	
	op <- Minusculas(op);
	
	Segun op
		"si" o "sí":
			Resolucion2_S <- 1;
		"no": 
			Resolucion2_S <- 0;
	FinSegun
FinFuncion
//==============================================================================//


//=================================== TP N°1 ==================================//

Funcion Catetos_Hipotenusa
	Definir C1,C2,Hip como Real;
	
	Escribir "Ingrese la longitud del primer cateto."
	Leer C1;
	Escribir "Ingrese la longitud del segundo cateto."
	Leer C2;
	
	Hip <- Raiz((C1^2)+(C2^2));
	
	Escribir "La longitud de la hipotenusa es de ",Hip,".";
FinFuncion

//------------------------------------------------------------------------------//

Funcion HorasValor_Sueldo
	Definir Hs como Entero;
	Definir Val,Sueldo como Real;
	
	Escribir "Ingrese la cantidad de horas trabajadas por el operario.";
	Leer Hs;
	Escribir "Ingrese el valor de 1 hora de trabajo (en AR$)";
	Leer Val;
	
	Sueldo <- Hs*Val;
	
	Escribir "El operario percibe un sueldo de AR$",Sueldo,".";
FinFuncion

//------------------------------------------------------------------------------//

Funcion AB_MayorAB
	Definir A,B como Real;
	
	Escribir "Ingrese el primer valor.";
	Leer A;
	Escribir "Ingrese el segundo valor.";
	Leer B;
	
	Si A<>B
		Si A>B
			Escribir "El mayor es el ",A;
		SiNo
			Escribir "El mayor es el ",B;
		FinSi
	SiNo
		Escribir "Ambos valores son iguales.";
	FinSi
FinFuncion

//------------------------------------------------------------------------------//

Funcion Palabra_Palindromo
	Definir Palabra1,Palabra2,Letra como Cadena;
	Definir Long como Entero;
	
	Escribir "Ingrese una palabra.";
	Leer Palabra1;
	Escribir "Ingrese la misma palabra, invertida.";
	Leer Palabra2;
	
	Si Palabra1 = Palabra2
		Escribir "La palabra es un palíndromo.";
	SiNo
		Escribir "La palabra no es un palíndromo.";
	FinSi
FinFuncion

//------------------------------------------------------------------------------//

Funcion SieteCalificaciones_Promedio
	Definir C1,C2,C3,C4,C5,C6,C7 como Entero;
	Definir Promedio como Real;
	
	Escribir "Ingrese la calificación de cada parcial, uno a uno."
	Leer Sin Saltar C1,C2,C3,C4,C5,C6,C7;
	
	Promedio <- (C1+C2+C3+C4+C5+C6+C7)/7;
	
	Escribir "La nota promedio de sus parciales es de ",Promedio,".";
FinFuncion

//------------------------------------------------------------------------------//

Funcion CuatroNumeros_3enLista
	Definir Num1,Num2,Num3,Num4 como Entero;
	Definir Pos como Caracter;
	
	Escribir "Ingrese los cuatro números, uno a uno.";
	Leer Num1,Num2,Num3,Num4;
	
	Si Num1 = 3 o Num2 = 3 o Num3 = 3 o Num4 = 3
		Escribir "El N°3 se encuentra en la lista.";
	SiNo
		Escribir "El N°3 no se encuentra en la lista.";
	FinSi
FinFuncion

//------------------------------------------------------------------------------//

Funcion Monto_Total
	Definir Monto,Cantidad,subTotal,IVA,Total como Real;
	
	Escribir "Ingrese el monto del producto.";
	Leer Monto;
	Escribir "Ingrese la cantidad que desea comprar.";
	Leer Cantidad;
	
	subTotal <- Monto*Cantidad;
	IVA <- (subTotal*21)/100;
	Total <- subTotal+IVA;
	
	Escribir "Subtotal a pagar: $",subTotal,".";
	Escribir "Descuento IVA (21%): $",IVA,".";
	Escribir "Total a pagar: $",Total,".";
FinFuncion

//------------------------------------------------------------------------------//

Funcion Numero3Digitos_Armstrong
	Definir Num1,Dig1,Dig2,Dig3,Calculo como Entero;
	
	Num1 <- 1111;
	
	Mientras Num1 < 100 | Num1 > 999
		Escribir "Ingrese un número de tres dígitos.";
		Leer Num1;
		
		Si Num1 < 100 | Num1 > 999
			Escribir "El número debe contener sólo tres dígitos.";
		FinSi
	FinMientras
	
	Dig3 <- Num1 mod 10;
	Dig2_aux <- trunc(Num1/10);
	Dig2 <- Dig2_aux mod 10;
	Dig1 <- trunc(Dig2_aux/10);
	Calculo <- ((Dig3^3)+(Dig2^3)+(Dig1^3));
	
	Escribir "La suma de cada dígito elevado al cubo es igual a ",Calculo;
	
	Si Calculo = Num1
		Escribir "El número ingresado es un Número Armstrong.";
	SiNo
		Escribir "El número ingresado no es un Número Armstrong.";
	FinSi
FinFuncion

//==============================================================================//


//=================================== TP N°2 ==================================//

Funcion DosNumerosPositivos_PrimosRelativos
	Definir Num1,Num2,Lim Como Entero;
	
	Escribir "Ingrese el primer número.";
	Leer Num1;
	
	Escribir "Ingrese el segundo número.";
	Leer Num2;
	
	Lim <- Num1;
	Si Num2 > Lim
		Lim <- Num2;
	FinSi
	
	Para i<-2 Hasta Lim con Paso 1
		Si Num1 MOD i = 0
			Si Num2 MOD i = 0
				Escribir "Los números ingresados no son primos relativos, ambos son divisibles por ",i,".";
				i <- Lim;
			SiNo
				Si i = Lim
					Escribir "Los números son primos relativos, no poseen divisores comunes a excepción del 1.";
				FinSi
			FinSi
		SiNo
			Si i = Lim
				Escribir "Los números son primos relativos, no poseen divisores comunes a excepción del 1.";
			FinSi
		FinSi
	FinPara
FinFuncion

//------------------------------------------------------------------------------//

Funcion ValoresNumericos_Rango
	Definir N1,N2,N3,N4,N5,Max,Min,Rango como Entero;
	
	Escribir "Ingrese 5 valores numéricos, uno a uno."
	Leer N1,N2,N3,N4,N5;
	
	Max <- N1;
    Min <- N1;
	
    Si N2 > Max
        Max <- N2;
    FinSi
    Si N3 > Max
        Max <- N3;
    FinSi
    Si N4 > Max
        Max <- N4;
    FinSi
    Si N5 > Max
        Max <- N5;
    FinSi
	
    Si N2 < Min
        Min <- N2;
    FinSi
    Si N3 < Min
        Min <- N3;
    FinSi
    Si N4 < Min
        Min <- N4;
    FinSi
    Si N5 < Min
        Min <- N5;
    FinSi
	
	Rango <- Max-Min;
	
	Escribir "";
	Escribir "Rango: ",Rango;
FinFuncion

//------------------------------------------------------------------------------//

Funcion Instruccion_EscuchaSpotify
	Definir PasoCompletado_S,disp como Entero;
	Definir int,op como Cadena;
	
	Escribir "A continuación se indicará cómo escuchar tu canción favorita en Spotify, paso a paso.";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "¿Qué tipo de dispositivo utilizarás para escuchar la canción?";
	Escribir "Selecciona una de las siguientes opciones:";
	Escribir "1. Ordenador portátil o de escritorio.";
	Escribir "2. Tableta.";
	Escribir "3. Celular/Smartphone.";
	Escribir "4. Otro.";
	Leer disp;
	
	Escribir "¿Se encuentra tu dispositivo conectado a Internet?";
	Leer int;
	int <- Minusculas(int);
	
	Si int = "no"
		Escribir "Intenta conectar tu dispositivo a Internet";
		Escribir "¿Has logrado establecer la conexión?";
		Leer int
		int <- Minusculas(int);
		Si int = "no"
			Escribir "Lamentablemente para poder realizar la tarea principal se requiere de una conexión estable a Internet, por lo que no podrás continuar. Intenta de nuevo cuando puedas conectar tu dispositivo a Internet.";
		FinSi
	SiNo
		Limpiar Pantalla;
	FinSi
	
	Si int <> "no"
		Escribir "1. Abre la aplicación de Spotify en tu dispositivo.";
		Escribir "¿Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir Sin Saltar "Asegúrate de tener la aplicación de Spotify descargada e instalada en tu dispositivo";
			Si disp <> 3
				Escribir Sin Saltar " o de poder ingresar a través de un navegador web";
			FinSi
			Escribir ", luego vuelve a intentar el primer paso.";
			Escribir "";
			Escribir "Cuando hayas logrado ejecutar la aplicación o ingresar a la web presiona cualquier tecla para continuar...";
			Esperar Tecla;
		FinSi
		Escribir "";
		
		Escribir "2. Inicia sesión en tu cuenta de Spotify.";
		Escribir "¿Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir "Verifica tus credenciales de inicio de sesión o crea una cuenta de Spotify si no tienes una.";
			Escribir "";
			Escribir "Cuando hayas logrado iniciar sesión en tu cuenta presiona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "3. Utiliza el buscador para encontrar la canción que quieres escuchar.";
		Escribir "¿Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir Sin Saltar "Utiliza la barra de búsqueda, en la aplicación suele encontrarse en";
			Si disp <> 3
				Escribir Sin Saltar " el panel a la izquierda de la pantalla, comúnmente entre Inicio y Tu Biblioteca, en la web igual.";
			SiNo
				Escribir Sin Saltar " la parte inferior de la pantalla, comúnmente entre Inicio y Tu biblioteca.";
			FinSi
			Escribir " El ícono de búsqueda es una lupa.";
			Escribir "";
			Escribir "Cuando hayas logrado realizar la búsqueda presiona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "4. Selecciona la canción de la lista de resultados.";
		Escribir "¿Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir "Busca la canción en la lista de resultados, si no está a simple vista recuerda que puedes deslizar (pueden existir distintas versiones de la canción que buscas).";
			Escribir "";
			Escribir "Si la canción que buscas no aparece en la lista, recuerda revisar tu ortografía, podría estar mal escrito.";
			Escribir "Si esto no funciona puedes intentar buscar la canción por el nombre de artista, álbum o incluso playlist.";
			Escribir "";
			Escribir "Cuando hayas logrado seleccionar la canción preciona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "5. Disfruta tu canción favorita en Spotify!";
		Escribir "Presione cualquier tecla para finalizar...";
		Esperar Tecla;
	FinSi
FinFuncion
//------------------------------------------------------------------------------//

Funcion Instruccion_BañarPerro
	Escribir "A continuación se muestran los pasos para bañar a un perro/a.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "Antes de comenzar, deberás preparar odo lo necesario para poder realizar esta tarea.";
	Esperar 3 segundos;
	
	Escribir "Asegúrate de:";
	Escribir "Tener a mano por lo menos un champú o shampoo, toallas, un cepillo y si es posible un juguete para distraer al perro durante el baño.";
	Esperar 3 segundos;
	Escribir "Tener acceso a agua caliente y fría, preferiblemente en una bañera o en una ducha con puerta.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir Sin Saltar "Existen gran variedad de productos pensados para la higiene de los perros.";
	Esperar 2 segundo;
	Escribir " Es fundamental que estén formulados específicamente para perros porque su composición será apta para su piel y su pelo, evitando problemas dermatológicos.";
	Esperar 3 segundos;
	Escribir "Evita utilizar productos para personas o para otros animales, pues no estarán adaptados ni al pH ni a las características de su piel.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "1. Lleva al perro/a al área del baño y cierra la puerta para evitar que escape.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "Si el perro/a está muy sucio o lleno de nudos, cepíllalo primero para aflojar la suciedad y los nudos.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "2. Moja al perro/a con agua tibia, comenzando por la cabeza y trabajando hacia la cola. Usa una regadera o un cabezal de ducha para mojarlo/a.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "3. Frota el champú para perros en todo el cuerpo del perro/a, asegurándote de no obtener champú en sus ojos, nariz o boca.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "4. Enjuaga completamente el champú del perro/a, asegurándote de que no queden restos de champú en su pelaje.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "5. Usa una toalla para secar al perro/a lo mejor que puedas.";
	Esperar 1 segundo;
	Escribir "Si tienes un secador de pelo para perros, úsalo con aire tibio y no lo pongas demasiado cerca del pelaje del perro/a.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "Si el perro/a es propenso a enredarse, cepíllalo/a nuevamente mientras se seca.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "6. Dale al perro/a un juguete y/o un premio para recompensarlo después del baño, esto hará que lo tome mejor o como una buena intención cada vez.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "¡Listo!";
	Escribir "Recuerda, la seguridad del perro/a es lo más importante. Asegúrate de tener cuidado al bañarlo/a y de no dejarlo/a solo/a en la bañera o ducha. ¡Bañar a un perro/a puede ser divertido para ambos si se hace correctamente!";
	Esperar 4 segundos;
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//------------------------------------------------------------------------------//

Funcion Instruccion_NotaManuscrita
	Escribir "A continuación se muestran los pasos para escribir una nota manuscrita.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "1. Encuentra un papel y un bolígrafo o lápiz que te gusten y que se sientan cómodos en tu mano.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "2. Decide el propósito de la nota y a quién va dirigida.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "3. Piensa en el contenido que deseas incluir en la nota, como un saludo, una pregunta o un mensaje específico.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "4. Comienza con un saludo apropiado, como Querido/a [nombre] o Hola [nombre].";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir Sin Saltar "5. Escribe el contenido principal de la nota en un lenguaje claro y conciso.";
	Esperar 1 segundo;
	Escribir "Trata de ser específico y directo en tu mensaje.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir "6. Si quieres, puedes agregar detalles adicionales como una historia breve o una anécdota personal.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "7. Termina la nota con una despedida apropiada, como Sinceramente o Con cariño.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "8. Firma tu nombre al final de la nota.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "9. Revisa la nota para asegurarte de que esté clara, legible y libre de errores ortográficos y gramaticales.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "10. Dobla la nota con cuidado y colócala en un sobre si es necesario.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "¡Listo!";
	Escribir "Recuerda, una nota manuscrita puede ser una forma personal y significativa de comunicarse con alguien. ¡Así que tómate el tiempo para escribir una nota hermosa y significativa!";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//------------------------------------------------------------------------------//

Funcion Instruccion_AuxilioRiesgo
	Escribir "Pedir auxilio en una situación de riesgo puede ser un proceso crítico y estresante, por lo que es importante saber cómo hacerlo de manera clara y efectiva.";
	Esperar 3 segundos;
	Escribir "A continuación se muestran los pasos a seguir para realizar dicha tarea.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir Sin Saltar "1. Evalúa la situación y determina si necesitas ayuda.";
	Esperar 1 segundo;
	Escribir Sin Saltar "Si estás en una situación de emergencia, llama a los servicios de emergencia inmediatamente (policía, bomberos, ambulancia) marcando el número de emergencia en tu país.";
	Esperar 2 segundos;
	Escribir "En la mayoría de los países, este número es el 911 o el 112.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir Sin Saltar "2. Si no puedes llamar por teléfono, busca a alguien que pueda hacerlo por ti.";
	Esperar 1 segundo;
	Escribir "Pide a alguien que esté cerca que llame a los servicios de emergencia y describa la situación.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir Sin Saltar "3. Si no hay nadie cerca, grita ¡Auxilio! o ¡Ayuda! lo más fuerte posible.";
	Esperar 2 segundos;
	Escribir "Asegúrate de que tu voz se escuche claramente y con fuerza.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir Sin Saltar "4. Usa un silbato o cualquier objeto ruidoso para llamar la atención de otros.";
	Esperar 1 segundo;
	Escribir "Si estás en una zona boscosa o en la montaña, usa un silbato para llamar la atención de otras personas cercanas.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "5. Si tienes un teléfono móvil, envía un mensaje de texto a alguien que pueda ayudarte o use aplicaciones de seguridad, como SOS o Botón de Emergencia para notificar automáticamente a tus contactos de emergencia sobre tu ubicación y necesidad de ayuda.";
	Esperar 5 segundo;
	
	Escribir "";
	Escribir "6. Si estás en una zona poblada, busca un lugar público concurrido, como una tienda o un restaurante, y pide ayuda a la gente que esté allí.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir Sin Saltar "7. Si estás en el agua, mueve los brazos y piernas para llamar la atención y haz sonidos fuertes.";
	Esperar 1 segundo;
	Escribir "Si puedes, usa una linterna o una bengala para llamar la atención de los rescatistas.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "8. Si estás en la carretera, levanta los brazos para llamar la atención de otros conductores o pide ayuda a la policía de tránsito.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "9. Cuando llegue la ayuda, explica la situación detalladamente y sigue las instrucciones que te den.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "¡Listo!";
	Escribir "Recuerda, una nota manuscrita puede ser una forma personal y significativa de comunicarse con alguien. ¡Así que tómate el tiempo para escribir una nota hermosa y significativa!";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//==============================================================================//