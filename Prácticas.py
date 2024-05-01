#  Se tiene un listado con los siguientes datos: Número de alumno (1 a n), número de materia (1 a m), nota (0 a 10). * El mismo número de alumno y de materia puede aparecer más de una vez. * El listado no está ordenado, ni necesariamente completo. Esto último quiere decir que puede ser que un alumno no haya cursado una o más materias, y por lo tanto no existan los datos correspondientes en el listado. Se pide: a- Crear una estructura bidimensional que almacene el promedio por materia de cada alumno e informarla asignándole en la impresión un guión en caso de faltar datos. b- Informar el porcentaje de alumnos que cursó cada materia y el promedio general por materia considerando los alumnos que la cursaron. c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo considerando las materias que cursó.
def Ejercicio6():
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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

def llenarPila(n):
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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Un Hola Mundo que se escribe solo recorriendo una a una las letras del abecedario.
def holaMundoAuto(cadena):
    if not cadena:
        cadena = 0
    pos = cadena
    teclas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Mapeo de letras
    frases_HM = ["", "H", "Ho", "Hol", "Hola ", "Hola m", "Hola mu", "Hola mun", "Hola mund", "Hola mundo"]
    teclas_HM = ["h", "o", "l", "a", "m", "u", "n", "d", "o"]
    tecla = 0 # Letra inicial
    while True:
        if pos < 9:
            if teclas[tecla - 1] == teclas_HM[cadena]: # Si la última letra es "h"...
                holaMundoAuto(cadena + 1) # Recursividad
                return
        else:
            break
            
        print(frases_HM[pos], teclas[tecla], sep="")
        if tecla < 25: # Para repetir el abcedario después de la Z
            tecla += 1
        else:
            tecla = 0
            
        time.sleep(0.04) # Esperar 0.3 segundo
    return frases_HM[9]

# holaMundo_auto(0)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Este Hola Mundo es como el automático, con la diferencia de que en este se debe presionar una tecla para detener el abecedario, debiendo quedar la letra correspondiente a la posición del cursor en la palabra "Hola Mundo". Es algo así como un juego de Hola Mundo.
import time
def tecla_presionada(tecla):
    import msvcrt
    if msvcrt.kbhit():
        if not tecla:
            if msvcrt.getch():
                return True
            else:
                return False
        elif msvcrt.getwch() == tecla:
                return True
        else:
            return False
def holaMundoJuego(cadena):
    if not cadena:
        cadena = 0
    pos = cadena
    teclas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Mapeo de letras
    frases_HM = ["", "H", "Ho", "Hol", "Hola ", "Hola m", "Hola mu", "Hola mun", "Hola mund", "Hola mundo"]
    teclas_HM = ["h", "o", "l", "a", "m", "u", "n", "d", "o"]
    tecla = 0 # Letra inicial
    while True:
        if pos < 9:
            if tecla_presionada(None): # Si se presionó una tecla...
                if teclas[tecla - 1] == teclas_HM[cadena]: # Si la última letra es "h"...
                    holaMundoJuego(cadena + 1, pos + 1)
                    return
                else:
                    print("Mal ahí, seguí intentando...")
                    tecla = 0
                    time.sleep(1) # Esperar 1 segundo
        else:
            break
            
        print(frases_HM[pos], teclas[tecla], sep="")
        if tecla < 25: # Para repetir el abcedario después de la Z
            tecla += 1
        else:
            tecla = 0
            
        time.sleep(0.3) # Esperar 0.3 segundo
    return frases_HM[9]

# holaMundo(0)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Juego matemático de agilidad mental. Tras un conteo regresivo aparece una operación en pantalla, entonces el usuario deberá ingresar el resultado de ésta, si no lo hace antes de un tiempo indicado se toma como incorrecto, en cuyo caso el jugador perderá una vida y deberá volver a intentar. Si las vidas llegan a 0 entonces piede. Si ingresa el resultado correcto y a tiempo entonces podrá continuar con otra opeación un poco más difícil, de esta manera irá subiendo de nivel. Más pronto sea ingresado el resultado correcto, más puntos obtendrá el usuario. Los puntos se acumulan y al llegar al final del juego son mostrados en pantalla. El final del juego aún no está definido.