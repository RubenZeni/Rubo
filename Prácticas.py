#  Se tiene un listado con los siguientes datos: Número de alumno (1 a n), número de materia (1 a m), nota (0 a 10). * El mismo número de alumno y de materia puede aparecer más de una vez. * El listado no está ordenado, ni necesariamente completo. Esto último quiere decir que puede ser que un alumno no haya cursado una o más materias, y por lo tanto no existan los datos correspondientes en el listado. Se pide: a- Crear una estructura bidimensional que almacene el promedio por materia de cada alumno e informarla asignándole en la impresión un guión en caso de faltar datos. b- Informar el porcentaje de alumnos que cursó cada materia y el promedio general por materia considerando los alumnos que la cursaron. c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo considerando las materias que cursó.
def analisisAlumnos():
    alumnos = []
    materias = []
    notas = []
    promedios = []
    alumno_anotado = -1
    materia_anotada = -1
    promedio_general = 0
    alumnos_que_cursaron = 0
    total_alumnos = 0
    posicion_ultimo_alumno = 0
    
    numero_alumno = int(input('Número de alumno (0 para finalizar): '))
    while numero_alumno != 0:
        alumnos.append(numero_alumno)
        materias.append(int(input('Número de materia: ')))
        nota_alumno = input('Nota: ')
        if nota_alumno == '':
            notas.append('-')
        else:
            notas.append(int(nota_alumno))
        numero_alumno = int(input('Número de alumno (0 para finalizar): '))
    
    promedios.append([alumnos[0], materias[0], 0, 0, 1, 0]) # Asigno a la posición 0 de los promedios (con alumno en posición 0): Número de alumno, Número de materia, Nota, Promedio general del alumno, Cantidad de materias del alumno y Contador de notas para calcular el promedio de cada materia del alumno
    for i in range(len(alumnos)): # Recorro la lista de alumnos (con i)
        print(f'VALOR I = {i}')
        for j in (posicion_ultimo_alumno, 0, -1): # Recorro desde la posición actual hacia atrás (con j)
            print(f'VALOR J = {j}')
            if alumnos[i] == promedios[j][0]: # ¿Es el alumno en la posición actual (i) igual al que se encuentra en la posición j? (j irá cambiando)
                alumno_anotado = j # Si lo es, guardo la posición del alumno
                if materias[i] == promedios[j][1]: # Además ¿Es la materia en la posición actual (la del alumno, i) igual a la que se encuentra en la posición j? (j irá cambiando)
                    materia_anotada = j # Si lo es, guardo la posición de la materia
                else:
                    materia_anotada = -1 # Si no lo es, guardo un número negativo indicando que no hay posición de materia
                break # Además, freno el bucle en reversa
            else:
                alumno_anotado = -1 # Si no lo es, guardo un número negativo indicando que no hay posición de alumno
                if notas[i] != '-': # ¿El alumno cursó la materia?
                    alumnos_que_cursaron += 1 # Si es así, sumno 1 al contador para el porcentaje
        if materia_anotada >= 0: # Una vez finalizado el bucle en reversa, ¿Ya existía el número del alumno en la lista, con la misma materia?
            if notas[i] != '-': # ¿El alumno cursó la materia?
                promedios[alumno_anotado][2] += notas[i] # Si es así, entonces sumo la nota a la actual
                promedios[alumno_anotado][3] += notas[i] # Y también sumo la nota a la de promedio general del alumno
                promedios[alumno_anotado][5] += 1 # Además, agrego uno al contador de notas para poder calcular el promedio
        elif alumno_anotado >= 0: # Si no es así, ¿Estaba el número del alumno pero sin la misma materia?
            promedios.append([alumnos[i], materias[i], notas[i], 0, 1, 0]) # Si es así, asigno un nuevo elemento para el mismo alumno pero con una materia distinta a la lista
            posicion_ultimo_alumno += 1 # Al haber agregado un elemento a la lista debo actualizar el contador de posiciones
            if notas[i] != '-': # ¿El alumno cursó la materia?
                promedios[alumno_anotado][4] += 1 # Si es así, entonces sumo uno a la cantidad de materias que cursó el alumno
        else: # ¿No estaba ya el número del alumno en la lista?
            total_alumnos += 1
            promedios.append([alumnos[i], materias[i], notas[i], 0, 1, 0]) # Si es así, entonces asigno un nuevo elemento para el alumno su respectiva materia y nota
            posicion_ultimo_alumno += 1 # Al haber agregado un elemento a la lista debo actualizar el contador de posiciones
    promedios.sort() # Ordeno la lista de promedios para tener a todos los alumnos en orden
    for i in range(len(promedios)): # Recorro la lista de promedios
        if promedios[i][2] != '-': # ¿El alumno cursó la materia?
            promedio_general += promedios[i][2] # Si es así, sumo los promedios de los alumnos que cursaron para tener el promedio general
            if promedios[i][5] != 0:
                promedios[i][2] = promedios[i][2] / promedios[i][5] # Además, calculo el promedio de cada alumno
            del promedios[i][5] # Y elimino el elemento contador de notas porque no me sirve más
    ver = input('¿Desea visualizar la martiz? (s/n): ')
    print()
    if ver == 's':
        for i in range(len(promedios)):
            print('[', end = '')
            for j in range(len(promedios[0])):
                print(promedios[i][j], end = '')
                if j != len(promedios[0]) - 1:
                    print(', ', end = '')
            print(']')
        print()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Pila - Recursividad
class Stack:
    def __init__(self):
        self.__elements = []
    def push(self, element):
        self.__elements.append(element)
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None
    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None
    def size(self):
        return len(self.__elements)

def llenarPila():
    pila = Stack()
    pila.push("a")
    pila.push("b")
    pila.push("c")
    pila.push("d")
    pila.push("e")
    pila.push("f")
    pila.push("g")
    pila.push("h")
    pila.push("i")
    pila.push("j")
    pila.push("k")
    pila.push("l")

pila_aux = Stack()
llenarPila()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Búsqueda recursiva de un elemento en una pila.
def buscarPila(pila, elemento):
    if pila.size() == 0:
        print("Elemento no encontrado.")
        return
    temp = pila.pop()
    if temp == elemento:
        print("Elemento encontrado.")
        pila.push(temp)
    else:
        buscarPila(pila, elemento)
        pila.push(temp)

# buscarPila(pila, input("Buscar elemento: "))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Búsqueda recursiva de un elemento en una pila con distancia entre el último elemento y el buscado, o ubicación del elemento dentro de la pila.
def buscarPilaDistancia(pila, elemento):
    if pila.size() == 0:
        print("Elemento no encontrado.")
        return -1
    temp = pila.pop()
    if temp == elemento:
        print("Elemento encontrado.")
        pila.push(temp)
        return 0
    else:
        distancia = buscarPilaDistancia(pila, elemento)
        if distancia != -1:
            distancia += 1
        pila.push(temp)
        return distancia

# distancia = buscarPilaDistancia(pila, input("Buscar elemento: "))
# if distancia != -1:
#     print(f"Si se quitan los últimos {distancia} elementos de la pila, se podrá acceder al elemento buscado.")

# -----------------------------------------------------------------------------------------------------------------------------------------

# Suprimir números impares de una pila de manera recursiva.
def supImpares(pila):
    if pila.size() == 0:
        return
    temp = pila.pop()
    if temp % 2 == 0:
        supImpares(pila)
    else:
        supImpares(pila)
        pila.push(temp)

# -----------------------------------------------------------------------------------------------------------------------------------------

# Un Hola Mundo que se escribe solo recorriendo una a una las letras del abecedario. Puede recibir opcionalmente el tiempo que pasa entre cada letra que se muestra en pantalla.
def holaMundoAuto(tiempo = 0.04, pos = 0):
    import time
    indice = pos
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Mapeo de letras
    frases_HM = ["", "H", "Ho", "Hol", "Hola ", "Hola m", "Hola mu", "Hola mun", "Hola mund", "Hola mundo"]
    letras_HM = ["h", "o", "l", "a", "m", "u", "n", "d", "o"]
    letra = 0 # Letra inicial
    while True:
        if indice < 9:
            if letras[letra - 1] == letras_HM[pos]: # Si la última letra es "h"...
                holaMundoAuto(tiempo ,pos + 1) # Recursividad
                return
        else:
            break
            
        print(frases_HM[indice], letras[letra], sep="")
        if letra < 25: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
            
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.04 seg.
    return frases_HM[9]

# holaMundoAuto()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Función que detecta si una tecla ha sido presionada y retorna bool. Puede recibir opcionalemte un caracter y así verificar si la tecla presionada coincide con dicho caracter.
def teclaPresionada(caracter):
    import msvcrt # Este módulo creo que funciona únicamente en Windows. No puedo asegurar que funcione en otros SO
    if msvcrt.kbhit(): # Si existe una "pulsación" de tecla esperando en el búfer
        if not caracter: # Si la función no recibió un caracter específico
            if msvcrt.getch(): # Si se puede recuperar la tecla presionada
                return True
            else:
                return False
        elif msvcrt.getwch() == caracter: # Si la función sí recibió un caracter específico
                return True
        else:
            return False

def presionarTecla(caracter = None): # Esta función sirve para probar teclaPresionada()
    while True:
        if teclaPresionada(caracter):
            if caracter != None:
                print(f"Se presionó la tecla {caracter}.")
            else:
                print("Se presionó una tecla.")
            break
        else:
            print("Sin cambios.")

# presionarTecla()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Este es como el holaMundoAuto(), con la diferencia de que en este se debe presionar una tecla para detener el abecedario, debiendo quedar la letra correspondiente a la posición del cursor en la palabra "Hola Mundo". Es algo así como un juego del holaMundoAuto(), de ahí el nombre.

def holaMundoJuego(tiempo = 0.2, pos = 0):
    import time
    indice = pos
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Mapeo de letras
    frases_HM = ["", "H", "Ho", "Hol", "Hola ", "Hola m", "Hola mu", "Hola mun", "Hola mund", "Hola mundo"]
    letras_HM = ["h", "o", "l", "a", "m", "u", "n", "d", "o"]
    letra = 0 # Letra inicial
    while True:
        if indice < 9:
            if teclaPresionada(None): # Si se presionó una tecla...
                if letras[letra - 1] == letras_HM[pos]: # Si la última letra es "h"...
                    holaMundoJuego(tiempo, pos + 1)
                    return "Bien hecho!"
                else:
                    print("Mal ahí, seguí intentando...")
                    letra = 0
                    time.sleep(1) # Esperar 1 segundo
        else:
            break
            
        print(frases_HM[indice], letras[letra], sep="")
        if letra < 25: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
            
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.2 seg
    return frases_HM[9]

# print(holaMundoJuego())

# -----------------------------------------------------------------------------------------------------------------------------------------

# Función recursiva que imprime la cadena ingresada como parámetro de la misma manera en que holaMundoAuto() lo haría. Se admiten caracteres alfanuméricos y unos cuantos símbolos. ¿Por qué recursiva? Porque sí, porque queda linda :)
def escribirAuto(cadena, tiempo = 0.02, pos = 0): # Recibe una cadena y la posicion de la letra a buscar en letras
    import time
    indice = pos # Hay lugares en donde pos por poco no es el correcto, por eso lo almaceno antes en indice (como un pos_aux)
    letras = [" ", "a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", "-", "_", "(", ")", "¿", "?", "¡", "!", "#", "$", "%", "+", "*", "/"] # Mapeo de caracteres
    frases = [""] # Declaración de la lista donde se almacenará la cadena por partes. Siendo f la posición de cada elemento en frases y g la posición de cada elemento en cadena, empezando con f(0)
    extra = -1
    while True:
        if extra < len(cadena) + 1:
            cadenita = ""
            for elemento in range(0, extra):
                cadenita += cadena[elemento]
            if cadenita != "":
                frases.append(cadenita)
            extra += 1
        else:
            break
    listaCadena = [cadena[0]]
    for elemento in range(1, len(cadena)):
        listaCadena.append(cadena[elemento])
    letra = 0 # Letra inicial
    while True:
        if indice < len(listaCadena):
            if letras[letra - 1] == f"{listaCadena[pos]}".lower(): # Si la última letra es correcta...
                escribirAuto(cadena, tiempo, pos + 1) # Recursividad
                return ""
        else:
            break
        
        print(frases[indice], letras[letra], sep="")
        if letra < len(letras) - 1: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
          
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.02 seg

# print(escribirAuto("+¿Para el Junior? / -Sí, creo. / +Perfecto! Gracias :)"))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Juego matemático de agilidad mental. Tras un conteo regresivo aparece una operación en pantalla, entonces el usuario deberá ingresar el resultado de ésta, si no lo hace antes de un tiempo indicado se toma como incorrecto, en cuyo caso el jugador perderá una vida y deberá volver a intentar. Si las vidas llegan a 0 entonces piede. Si ingresa el resultado correcto y a tiempo entonces podrá continuar con otra opeación un poco más difícil, de esta manera irá subiendo de nivel. Más pronto sea ingresado el resultado correcto, más puntos obtendrá el usuario. Los puntos se acumulan y al llegar al final del juego son mostrados en pantalla. El final del juego aún no está definido.
# Pienso escribir cada día un poco más del código, haciendo versiones distintas del juego cada vez. Hasta lograr el enunciado de arriba.

def juegoMatematico():
    import random
    import time
    # Mensaje de bienvenida y explicación del juego
    print("A continuación se mostrarán distintas operaciones que irán aumentando su dificultad con cada nivel. Si respondés bien subís de nivel, si respondés mal perdés una vida y tanto el nivel como la operación son los mismos. Tenés 5 segundos para ingresar el resultado, si una vez ingresado el tiempo expiró se toma como respuesta incorrecta.")
    input("Presioná cualquier tecla para continuar...")

    def generar_operacion(nivel): # Definir los límites de los números aleatorios según el nivel
        if nivel <= 5: # Para los niveles 1 al 5, los números aleatorios están entre 1 y nivel*10
            a = random.randint(1, nivel * 10)
            b = random.randint(1, nivel * 10)
            operador = random.choice(['+', '-']) if nivel > 2 else '+' # Aleatoriamente + o -, a partir del nivel 3, sino sólo +
        elif nivel <= 10:
            # Para los niveles 6 al 10, los números aleatorios están entre 1 y 10
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            operador = random.choice(['*', '/']) if nivel > 7 else '*'  # Aleatoriamente * o /, a partir del nivel 8, sino sólo *
            while operador == '/' and a % b != 0: # Si el operador es división, asegurarse de que la división sea entera
                a = random.randint(1, 10)
                b = random.randint(1, 10)
        else: # Para los niveles superiores a 10, se incluyen el resto de operadores (+, -, *, /)
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            operador = random.choice(['+', '-', '*', '/'])
        
        return f"{a} {operador} {b}" # Devolver la operación como una cadena de texto

    def ingresarResultado(resultado): # Función para que el usuario ingrese el resultado de la operación
        inicio = time.time()  # Tiempo de inicio
        respuesta_usuario = input("Ingrese el resultado: ")  # El usuario ingresa su respuesta
        fin = time.time()  # Tiempo de finalización

        # Verificar si el usuario ingresó el resultado correcto
        if fin - inicio > 5:  # Si el tiempo transcurrido es mayor a 5 segundos
            if int(respuesta_usuario) != resultado: # Si además la respuesta es incorrecta (ambos se cumplen)
                return -2
            else:
                return -1
        elif int(respuesta_usuario) == resultado:  # Si la respuesta es correcta
            return 1
        else: # Si la respuesta es incorrecta
            return 0

    vidas = 3  # Número inicial de vidas
    nivel = 1  # Número inicial de nivel
    operacion = ""  # Operación actual

    while vidas > 0:  # Mientras el jugador tenga vidas
        print("")  # Línea en blanco
        print(f"Nivel: {nivel}")  # Nivel actual
        print(f"Vidas: {vidas}")  # Cantidad de vidas restantes

        if not operacion:  # Si no hay una operación actual generada
            operacion = generar_operacion(nivel)  # Generar una nueva operación para el nivel actual
        print(f"Operación: {operacion}")  # Imprimir la operación actual

        resultado = ingresarResultado(eval(operacion))  # Obtener la respuesta del usuario y evaluarla
        if resultado == -2:  # Si el tiempo expiró y la respuesta es incorrecta.
            vidas -= 1  # Restar una vida
            print("Respuesta incorrecta y iempo expirado.")  # Imprimir un mensaje indicando que ta todo mal
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input("¿Desea salir? (s/n): ")  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == -1:  # Si el tiempo expiró
            vidas -= 1  # Restar una vida
            print("Tiempo expirado.")  # Imprimir un mensaje indicando que el tiempo expiró
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input("¿Desea salir? (s/n): ")  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == 0:  # Si la respuesta es incorrecta
            vidas -= 1  # Restar una vida
            print("Respuesta incorrecta.")  # Imprimir un mensaje indicando que el tiempo expiró
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input("¿Desea salir? (s/n): ")  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == 1:  # Si la respuesta es correcta
            print("Respuesta correcta.")  # Imprimir un mensaje indicando que la respuesta es correcta
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input("¿Desea salir? (s/n): ")  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                operacion = ""  # Reiniciar la operación para generar una nueva en el próximo ciclo
                if nivel < 20:  # Si el nivel actual es menor que 20
                    nivel += 1  # Incrementar el nivel
                else:
                    nivel = 20  # Establecer el nivel máximo
            
    print("Juego terminado.")  # Imprimir un mensaje indicando que el juego ha terminado

# juegoMatematico()