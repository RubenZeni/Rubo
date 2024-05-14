//============================ ALGORITMO PRINCIPAL ============================//
Algoritmo TrabajosPracticos
	
	Limpiar Pantalla;
	Escribir "Antes de comenzar ejecuci�n, por favor ampl�e el tama�o de la ventana de la consola -si es posible-, esto se debe a que la interfaz del programa es un poco m�s grande que el tama�o predeterminado de la ventana.";
	Escribir "";
	Escribir "Puede Maximizar la ventana o simplemente ampliar los bordes o esquinas de la misma, en caso que no sea posible puede intentar reducir el tama�o de CTRL + (Rueda hacia abajo) o CTRL + (Tecla -).";
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
	
	Escribir "Gracias por ejecutar mi c�digo!";
	Escribir "Que tenga un buen d�a :)";
	Escribir "";
	Escribir "Presione una tecla para finalizar la ejecuci�n...";
	Esperar Tecla;
	
	Limpiar Pantalla;
	
FinAlgoritmo
//==============================================================================//


//=============================== MENU PRINCIPAL ===============================//
Funcion Menu_S <- Menu
	
	Definir op como Entero;
	
	Repetir
		
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "|     Universidad Aut�noma De Entre R�os       |";
		Escribir "|      Facultad de Ciencia y Tecnolog�a        |";
		Escribir "| Licenciatura en Sistemas de Informaci�n (TM) |";
		Escribir "|             Alumno: Rub�n Zeni               |";
		Escribir "|         Profesora: Fernanda Gavet            |";
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "|               Trabajo Pr�ctico               |";
		Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
		Escribir "";
		Escribir "Seleccione el trabajo pr�ctico que desee explorar:";
		Escribir "";
		Escribir "1. Trabajo Pr�ctico N� 1: Entender el Problema";
		Escribir "";
		Escribir "2. Trabajo Pr�ctico N� 2: Estrategia";
		Escribir "";
		Escribir "0. SALIR";
		Leer Menu_S;
		
		Si Menu_S <> 1 y Menu_S <> 2 y Menu_S <> 0
			Escribir "La opci�n seleccionada no es v�lida.";
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
		
		Seg�n op
	1:
		Escribir "Enunciado:";
		Escribir "Dadas las longitudes de los dos catetos de un tri�ngulo rect�ngulo, hallar la longitud de la hipotenusa";
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
		Escribir "Dados dos valores A y B distintos, determinar cu�l es el mayor.";
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
		Escribir "Determinar si una palabra cualquiera es un pal�ndromo (capic�a); por ejemplo: Neuquen.";
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
		Escribir "Dadas las calificaciones de 7 ex�menes finales de un estudiante determinar el promedio.";
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
		Escribir "Dada una lista de 4 n�meros determinar si el N� 3 se encuentra en dicha lista.";
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
		Escribir "Calcular el valor a cancelar de un producto de un monto ingresado, el programa debe mostrar c�mo se presenta en una factura, subtotal (cantidad por precio), IVA (del subtotal) y total a pagar (la suma del subtotal + el IVA). Use de IVA el 21%.";
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
		Escribir "Escriba un programa que permita el ingreso de un n�mero de tres d�gitos y determine si es un n�mero Armstrong (ej. 153, 371). Como el n�mero que se ingresa posee 3 d�gitos, la suma de cada uno de sus d�gitos elevado a 3 debe ser igual al n�mero.";
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
		Escribir "La opci�n seleccionada no es v�lida.";
		Escribir "";
		Escribir "Presione una tecla para continuar al men� principal...";
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
		Escribir "4. Instruccion_Ba�arPerro.psc";
		Escribir "5. Instruccion_NotaManuscrita.psc";
		Escribir "6. Instruccion_AuxilioRiesgo.psc";
		Escribir "";
		Escribir "100. VOLVER";
		Escribir "0. SALIR";
		Leer op;
		
		Limpiar Pantalla;
		Marco_TP2;
		
		Seg�n op
	1:
		Escribir "Enunciado:";
		Escribir "Determinar si dos n�meros enteros positivos son primos relativos (esto es si no tienen divisores comunes con excepci�n del n�mero 1).";
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
		Escribir "Dada una lista de valores num�ricos, hallar su rango, es decir, la diferencia entre su valor m�ximo y su valor m�nimo.";
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
		Escribir "Indique como escucha su canci�n favorita en Spotify.";
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
		Escribir "Escriba en forma imperativa las instrucciones que le dar�a a una persona para ba�ar a un perro/a.";
		Resolucion1_S <- Resolucion1;
		Si Resolucion1_S = 1
			Repetir
				Limpiar Pantalla;
				Instruccion_Ba�arPerro;
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
		Escribir "Escriba las instrucciones a seguir para pedir auxilio ante una situaci�n de riesgo.";
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
		Escribir "La opci�n seleccionada no es v�lida.";
		Escribir "";
		Escribir "Presione una tecla para continuar al men� principal...";
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
	Escribir "|     Universidad Aut�noma De Entre R�os       |";
	Escribir "|      Facultad de Ciencia y Tecnolog�a        |";
	Escribir "| Licenciatura en Sistemas de Informaci�n (TM) |";
	Escribir "|             Alumno: Rub�n Zeni               |";
	Escribir "|         Profesora: Fernanda Gavet            |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "| Trabajo Pr�ctico N�1 | Entender El Problema  |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "";
FinFuncion
//==============================================================================//


//================================ MARCO de TP 2 ===============================//
Funcion Marco_TP2
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "|     Universidad Aut�noma De Entre R�os       |";
	Escribir "|      Facultad de Ciencia y Tecnolog�a        |";
	Escribir "| Licenciatura en Sistemas de Informaci�n (TM) |";
	Escribir "|             Alumno: Rub�n Zeni               |";
	Escribir "|         Profesora: Fernanda Gavet            |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "|      Trabajo Pr�ctico N�2 | Estrategia       |";
	Escribir "- - - - - - - - - - - - - - - - - - - - - - - -";
	Escribir "";
FinFuncion
//==============================================================================//


//================================ RESOLUCI�N 1 ===============================//
Funcion Resolucion1_S <- Resolucion1
	Escribir "";
	Escribir "�Desea ver la resoluci�n del problema? (SI/NO)";
	Leer op;
	
	op <- Minusculas(op);
	
	Segun op
		"si" o "s�":
			Resolucion1_S <- 1;
		"no": 
			Resolucion1_S <- 0;
	FinSegun
FinFuncion
//==============================================================================//


//================================ RESOLUCI�N 2 ===============================//
Funcion Resolucion2_S <- Resolucion2
	Escribir "";
	Escribir "�Desea volver a ver la resoluci�n del problema? (SI/NO)";
	Leer op;
	
	op <- Minusculas(op);
	
	Segun op
		"si" o "s�":
			Resolucion2_S <- 1;
		"no": 
			Resolucion2_S <- 0;
	FinSegun
FinFuncion
//==============================================================================//


//=================================== TP N�1 ==================================//

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
		Escribir "La palabra es un pal�ndromo.";
	SiNo
		Escribir "La palabra no es un pal�ndromo.";
	FinSi
FinFuncion

//------------------------------------------------------------------------------//

Funcion SieteCalificaciones_Promedio
	Definir C1,C2,C3,C4,C5,C6,C7 como Entero;
	Definir Promedio como Real;
	
	Escribir "Ingrese la calificaci�n de cada parcial, uno a uno."
	Leer Sin Saltar C1,C2,C3,C4,C5,C6,C7;
	
	Promedio <- (C1+C2+C3+C4+C5+C6+C7)/7;
	
	Escribir "La nota promedio de sus parciales es de ",Promedio,".";
FinFuncion

//------------------------------------------------------------------------------//

Funcion CuatroNumeros_3enLista
	Definir Num1,Num2,Num3,Num4 como Entero;
	Definir Pos como Caracter;
	
	Escribir "Ingrese los cuatro n�meros, uno a uno.";
	Leer Num1,Num2,Num3,Num4;
	
	Si Num1 = 3 o Num2 = 3 o Num3 = 3 o Num4 = 3
		Escribir "El N�3 se encuentra en la lista.";
	SiNo
		Escribir "El N�3 no se encuentra en la lista.";
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
		Escribir "Ingrese un n�mero de tres d�gitos.";
		Leer Num1;
		
		Si Num1 < 100 | Num1 > 999
			Escribir "El n�mero debe contener s�lo tres d�gitos.";
		FinSi
	FinMientras
	
	Dig3 <- Num1 mod 10;
	Dig2_aux <- trunc(Num1/10);
	Dig2 <- Dig2_aux mod 10;
	Dig1 <- trunc(Dig2_aux/10);
	Calculo <- ((Dig3^3)+(Dig2^3)+(Dig1^3));
	
	Escribir "La suma de cada d�gito elevado al cubo es igual a ",Calculo;
	
	Si Calculo = Num1
		Escribir "El n�mero ingresado es un N�mero Armstrong.";
	SiNo
		Escribir "El n�mero ingresado no es un N�mero Armstrong.";
	FinSi
FinFuncion

//==============================================================================//


//=================================== TP N�2 ==================================//

Funcion DosNumerosPositivos_PrimosRelativos
	Definir Num1,Num2,Lim Como Entero;
	
	Escribir "Ingrese el primer n�mero.";
	Leer Num1;
	
	Escribir "Ingrese el segundo n�mero.";
	Leer Num2;
	
	Lim <- Num1;
	Si Num2 > Lim
		Lim <- Num2;
	FinSi
	
	Para i<-2 Hasta Lim con Paso 1
		Si Num1 MOD i = 0
			Si Num2 MOD i = 0
				Escribir "Los n�meros ingresados no son primos relativos, ambos son divisibles por ",i,".";
				i <- Lim;
			SiNo
				Si i = Lim
					Escribir "Los n�meros son primos relativos, no poseen divisores comunes a excepci�n del 1.";
				FinSi
			FinSi
		SiNo
			Si i = Lim
				Escribir "Los n�meros son primos relativos, no poseen divisores comunes a excepci�n del 1.";
			FinSi
		FinSi
	FinPara
FinFuncion

//------------------------------------------------------------------------------//

Funcion ValoresNumericos_Rango
	Definir N1,N2,N3,N4,N5,Max,Min,Rango como Entero;
	
	Escribir "Ingrese 5 valores num�ricos, uno a uno."
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
	
	Escribir "A continuaci�n se indicar� c�mo escuchar tu canci�n favorita en Spotify, paso a paso.";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "�Qu� tipo de dispositivo utilizar�s para escuchar la canci�n?";
	Escribir "Selecciona una de las siguientes opciones:";
	Escribir "1. Ordenador port�til o de escritorio.";
	Escribir "2. Tableta.";
	Escribir "3. Celular/Smartphone.";
	Escribir "4. Otro.";
	Leer disp;
	
	Escribir "�Se encuentra tu dispositivo conectado a Internet?";
	Leer int;
	int <- Minusculas(int);
	
	Si int = "no"
		Escribir "Intenta conectar tu dispositivo a Internet";
		Escribir "�Has logrado establecer la conexi�n?";
		Leer int
		int <- Minusculas(int);
		Si int = "no"
			Escribir "Lamentablemente para poder realizar la tarea principal se requiere de una conexi�n estable a Internet, por lo que no podr�s continuar. Intenta de nuevo cuando puedas conectar tu dispositivo a Internet.";
		FinSi
	SiNo
		Limpiar Pantalla;
	FinSi
	
	Si int <> "no"
		Escribir "1. Abre la aplicaci�n de Spotify en tu dispositivo.";
		Escribir "�Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir Sin Saltar "Aseg�rate de tener la aplicaci�n de Spotify descargada e instalada en tu dispositivo";
			Si disp <> 3
				Escribir Sin Saltar " o de poder ingresar a trav�s de un navegador web";
			FinSi
			Escribir ", luego vuelve a intentar el primer paso.";
			Escribir "";
			Escribir "Cuando hayas logrado ejecutar la aplicaci�n o ingresar a la web presiona cualquier tecla para continuar...";
			Esperar Tecla;
		FinSi
		Escribir "";
		
		Escribir "2. Inicia sesi�n en tu cuenta de Spotify.";
		Escribir "�Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir "Verifica tus credenciales de inicio de sesi�n o crea una cuenta de Spotify si no tienes una.";
			Escribir "";
			Escribir "Cuando hayas logrado iniciar sesi�n en tu cuenta presiona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "3. Utiliza el buscador para encontrar la canci�n que quieres escuchar.";
		Escribir "�Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir Sin Saltar "Utiliza la barra de b�squeda, en la aplicaci�n suele encontrarse en";
			Si disp <> 3
				Escribir Sin Saltar " el panel a la izquierda de la pantalla, com�nmente entre Inicio y Tu Biblioteca, en la web igual.";
			SiNo
				Escribir Sin Saltar " la parte inferior de la pantalla, com�nmente entre Inicio y Tu biblioteca.";
			FinSi
			Escribir " El �cono de b�squeda es una lupa.";
			Escribir "";
			Escribir "Cuando hayas logrado realizar la b�squeda presiona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "4. Selecciona la canci�n de la lista de resultados.";
		Escribir "�Has logrado realizar este paso?";
		Leer op;
		op <- Minusculas(op);
		
		Si op = "no"
			Escribir "Busca la canci�n en la lista de resultados, si no est� a simple vista recuerda que puedes deslizar (pueden existir distintas versiones de la canci�n que buscas).";
			Escribir "";
			Escribir "Si la canci�n que buscas no aparece en la lista, recuerda revisar tu ortograf�a, podr�a estar mal escrito.";
			Escribir "Si esto no funciona puedes intentar buscar la canci�n por el nombre de artista, �lbum o incluso playlist.";
			Escribir "";
			Escribir "Cuando hayas logrado seleccionar la canci�n preciona cualquier tecla para continuar...";
			Esperar Tecla;
		Fin Si
		Escribir "";
		
		Escribir "5. Disfruta tu canci�n favorita en Spotify!";
		Escribir "Presione cualquier tecla para finalizar...";
		Esperar Tecla;
	FinSi
FinFuncion
//------------------------------------------------------------------------------//

Funcion Instruccion_Ba�arPerro
	Escribir "A continuaci�n se muestran los pasos para ba�ar a un perro/a.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "Antes de comenzar, deber�s preparar odo lo necesario para poder realizar esta tarea.";
	Esperar 3 segundos;
	
	Escribir "Aseg�rate de:";
	Escribir "Tener a mano por lo menos un champ� o shampoo, toallas, un cepillo y si es posible un juguete para distraer al perro durante el ba�o.";
	Esperar 3 segundos;
	Escribir "Tener acceso a agua caliente y fr�a, preferiblemente en una ba�era o en una ducha con puerta.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir Sin Saltar "Existen gran variedad de productos pensados para la higiene de los perros.";
	Esperar 2 segundo;
	Escribir " Es fundamental que est�n formulados espec�ficamente para perros porque su composici�n ser� apta para su piel y su pelo, evitando problemas dermatol�gicos.";
	Esperar 3 segundos;
	Escribir "Evita utilizar productos para personas o para otros animales, pues no estar�n adaptados ni al pH ni a las caracter�sticas de su piel.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "1. Lleva al perro/a al �rea del ba�o y cierra la puerta para evitar que escape.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "Si el perro/a est� muy sucio o lleno de nudos, cep�llalo primero para aflojar la suciedad y los nudos.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "2. Moja al perro/a con agua tibia, comenzando por la cabeza y trabajando hacia la cola. Usa una regadera o un cabezal de ducha para mojarlo/a.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "3. Frota el champ� para perros en todo el cuerpo del perro/a, asegur�ndote de no obtener champ� en sus ojos, nariz o boca.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "4. Enjuaga completamente el champ� del perro/a, asegur�ndote de que no queden restos de champ� en su pelaje.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "5. Usa una toalla para secar al perro/a lo mejor que puedas.";
	Esperar 1 segundo;
	Escribir "Si tienes un secador de pelo para perros, �salo con aire tibio y no lo pongas demasiado cerca del pelaje del perro/a.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "Si el perro/a es propenso a enredarse, cep�llalo/a nuevamente mientras se seca.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "6. Dale al perro/a un juguete y/o un premio para recompensarlo despu�s del ba�o, esto har� que lo tome mejor o como una buena intenci�n cada vez.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "�Listo!";
	Escribir "Recuerda, la seguridad del perro/a es lo m�s importante. Aseg�rate de tener cuidado al ba�arlo/a y de no dejarlo/a solo/a en la ba�era o ducha. �Ba�ar a un perro/a puede ser divertido para ambos si se hace correctamente!";
	Esperar 4 segundos;
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//------------------------------------------------------------------------------//

Funcion Instruccion_NotaManuscrita
	Escribir "A continuaci�n se muestran los pasos para escribir una nota manuscrita.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir "1. Encuentra un papel y un bol�grafo o l�piz que te gusten y que se sientan c�modos en tu mano.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "2. Decide el prop�sito de la nota y a qui�n va dirigida.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "3. Piensa en el contenido que deseas incluir en la nota, como un saludo, una pregunta o un mensaje espec�fico.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "4. Comienza con un saludo apropiado, como Querido/a [nombre] o Hola [nombre].";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir Sin Saltar "5. Escribe el contenido principal de la nota en un lenguaje claro y conciso.";
	Esperar 1 segundo;
	Escribir "Trata de ser espec�fico y directo en tu mensaje.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir "6. Si quieres, puedes agregar detalles adicionales como una historia breve o una an�cdota personal.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "7. Termina la nota con una despedida apropiada, como Sinceramente o Con cari�o.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "8. Firma tu nombre al final de la nota.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "9. Revisa la nota para asegurarte de que est� clara, legible y libre de errores ortogr�ficos y gramaticales.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "10. Dobla la nota con cuidado y col�cala en un sobre si es necesario.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "�Listo!";
	Escribir "Recuerda, una nota manuscrita puede ser una forma personal y significativa de comunicarse con alguien. �As� que t�mate el tiempo para escribir una nota hermosa y significativa!";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//------------------------------------------------------------------------------//

Funcion Instruccion_AuxilioRiesgo
	Escribir "Pedir auxilio en una situaci�n de riesgo puede ser un proceso cr�tico y estresante, por lo que es importante saber c�mo hacerlo de manera clara y efectiva.";
	Esperar 3 segundos;
	Escribir "A continuaci�n se muestran los pasos a seguir para realizar dicha tarea.";
	Escribir "Presione cuaqluier tecla para continar...";
	Esperar Tecla;
	Limpiar Pantalla;
	
	Escribir Sin Saltar "1. Eval�a la situaci�n y determina si necesitas ayuda.";
	Esperar 1 segundo;
	Escribir Sin Saltar "Si est�s en una situaci�n de emergencia, llama a los servicios de emergencia inmediatamente (polic�a, bomberos, ambulancia) marcando el n�mero de emergencia en tu pa�s.";
	Esperar 2 segundos;
	Escribir "En la mayor�a de los pa�ses, este n�mero es el 911 o el 112.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir Sin Saltar "2. Si no puedes llamar por tel�fono, busca a alguien que pueda hacerlo por ti.";
	Esperar 1 segundo;
	Escribir "Pide a alguien que est� cerca que llame a los servicios de emergencia y describa la situaci�n.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir Sin Saltar "3. Si no hay nadie cerca, grita �Auxilio! o �Ayuda! lo m�s fuerte posible.";
	Esperar 2 segundos;
	Escribir "Aseg�rate de que tu voz se escuche claramente y con fuerza.";
	Esperar 1 segundo;
	
	Escribir "";
	Escribir Sin Saltar "4. Usa un silbato o cualquier objeto ruidoso para llamar la atenci�n de otros.";
	Esperar 1 segundo;
	Escribir "Si est�s en una zona boscosa o en la monta�a, usa un silbato para llamar la atenci�n de otras personas cercanas.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "5. Si tienes un tel�fono m�vil, env�a un mensaje de texto a alguien que pueda ayudarte o use aplicaciones de seguridad, como SOS o Bot�n de Emergencia para notificar autom�ticamente a tus contactos de emergencia sobre tu ubicaci�n y necesidad de ayuda.";
	Esperar 5 segundo;
	
	Escribir "";
	Escribir "6. Si est�s en una zona poblada, busca un lugar p�blico concurrido, como una tienda o un restaurante, y pide ayuda a la gente que est� all�.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir Sin Saltar "7. Si est�s en el agua, mueve los brazos y piernas para llamar la atenci�n y haz sonidos fuertes.";
	Esperar 1 segundo;
	Escribir "Si puedes, usa una linterna o una bengala para llamar la atenci�n de los rescatistas.";
	Esperar 2 segundos;
	
	Escribir "";
	Escribir "8. Si est�s en la carretera, levanta los brazos para llamar la atenci�n de otros conductores o pide ayuda a la polic�a de tr�nsito.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "9. Cuando llegue la ayuda, explica la situaci�n detalladamente y sigue las instrucciones que te den.";
	Esperar 3 segundos;
	
	Escribir "";
	Escribir "�Listo!";
	Escribir "Recuerda, una nota manuscrita puede ser una forma personal y significativa de comunicarse con alguien. �As� que t�mate el tiempo para escribir una nota hermosa y significativa!";
	Escribir "Presiona cualquier tecla para continuar...";
	Esperar Tecla;
FinFuncion

//==============================================================================//