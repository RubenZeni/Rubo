# Se tiene un listado con los siguientes datos: Número de alumno (1 a m), número de materia (1 a n), nota (0 a 10). * El mismo número de alumno y de materia puede aparecer más de una vez. * El listado no está ordenado, ni necesariamente completo. Esto último quiere decir que puede ser que un alumno no haya cursado una o más materias, y por lo tanto no existan los datos correspondientes en el listado. Se pide: a- Crear una estructura bidimensional (matriz) que almacene el promedio por materia de cada alumno e informarla asignándole en la impresión un guión en caso de faltar datos. b- Informar el porcentaje de alumnos que cursó cada materia y el promedio general por materia considerando los alumnos que la cursaron. c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo considerando las materias que cursó.
def analisis_alumnos():
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
        print(f'Número de alumno: {alumnos} | Número de materia: {materias} | Nota: {notas}.')
        numero_alumno = int(input('Número de alumno (0 para finalizar): '))
    
    promedios.append([alumnos[0], materias[0], 0, 0, 1, 0]) # Asigno a la posición 0 de los promedios (con alumno en posición 0): Número de alumno, Número de materia, Nota, Promedio general del alumno, Cantidad de materias del alumno y Contador de notas para calcular el promedio de cada materia del alumno
    for i in range(len(alumnos)): # Recorro la lista de alumnos (con i)
        alumno_anotado = -1
        materia_anotada = -1
        print(f'Posición en "alumnos": {i}')
        for j in (posicion_ultimo_alumno, 0, -1): # Recorro desde la posición actual hacia atrás (con j)
            print(f'Posición en "posicion_ultimo_alumno": {j}')
            if alumnos[i] == promedios[j][0]: # Si el alumno en la posición actual (i) es igual al que se encuentra en la posición j (j irá cambiando)
                alumno_anotado = j # Guardo la posición del alumno y luego freno...
                if materias[i] == promedios[j][1]: # Además, si la materia en la posición actual (la del alumno[i]) es igual a la que se encuentra en la posición j (j irá cambiando)
                    materia_anotada = j # Guardo la posición de la materia
                else:
                    materia_anotada = -1 # Si no lo es, guardo un número negativo indicando que no hay posición de materia
                break # ...freno el bucle en reversa
            else:
                alumno_anotado = -1 # Si no lo es, guardo un número negativo indicando que no hay posición de alumno
                if notas[i] != '-': # Si el alumno cursó la materia
                    alumnos_que_cursaron += 1 # Sumo 1 al contador para el porcentaje final
        if materia_anotada >= 0: # Una vez finalizado el bucle en reversa, si ya existe el número del alumno en la lista, con la misma materia
            if notas[i] != '-': # Si el alumno cursó la materia
                promedios[alumno_anotado][2] += notas[i] # Sumo la nota a la actual
                promedios[alumno_anotado][3] += notas[i] # Sumo la nota al promedio general del alumno
                promedios[alumno_anotado][5] += 1 # Agrego uno al contador de notas para poder calcular el promedio
        elif alumno_anotado >= 0: # Si sí existe el número del alumno en la lista, pero sin la misma materia
            promedios.append([alumnos[i], materias[i], notas[i], 0, 1, 0]) # Asigno un nuevo elemento para el mismo alumno pero con una materia distinta a la lista
            posicion_ultimo_alumno += 1 # Al haber agregado un elemento a la lista debo actualizar el contador de posiciones
            if notas[i] != '-': # Si el alumno cursó la materia
                promedios[alumno_anotado][4] += 1 # Sumo uno a la cantidad de materias que cursó el alumno
        else: # Si no existe el número del alumno en la lista
            total_alumnos += 1 # Sumo 1 al total de alumnos
            promedios.append([alumnos[i], materias[i], notas[i], 0, 1, 0]) # Asigno un nuevo elemento para el alumno, con su materia y nota correspondientes
            posicion_ultimo_alumno += 1 # Al haber agregado un elemento a la lista debo actualizar el contador de posiciones
    promedios.sort() # Ordeno la lista de promedios para tener a todos los alumnos en orden
    for i in range(len(promedios)): # Recorro la lista de promedios
        if promedios[i][2] != '-': # Si el alumno cursó la materia
            promedio_general += promedios[i][2] # Sumo los promedios de los alumnos que cursaron para tener el promedio general
            if promedios[i][5] != 0: # Si existe promedio de la materia del alumno (muy probablemente sí)
                promedios[i][2] = promedios[i][2] / promedios[i][5] # Calculo el promedio de cada alumno
            del promedios[i][5] # Y elimino el elemento contador de notas porque ya no sirve más
    if input('¿Desea visualizar la martiz? (s/n): ') == 's':
        for i in range(len(promedios)):
            print('[', end = '')
            for j in range(len(promedios[0])):
                print(promedios[i][j], end = '')
                if j != len(promedios[0]) - 1:
                    print(', ', end = '')
            print(']')
        print()

# analisis_alumnos()

# El código de analisis_alumnos() está bien encaminado en el sentido de que "casi" cumple con el enunciado, pero su funcionamiento es incorrecto. Algunos ejemplos son que en la primer fila se muestra un valor flotante en lugar de entero y sus últimas dos columnas muestran valores raros, en las demás filas estas últimas dos columnas únicamente muestran unos y ceros. Por otra parte los promedios, porcentajes y cantidades podrían probablemente no ser correctos, y la interfaz final mostrada al usuario es muy poco comprensible ya que no se explica qué expresa y para qué sirve cada número. Todos estos y tal vez algunos otros errores son difíciles de encontrar y más difíciles aún de solucionar sin crear consecuentemente más errores, a mi parecer esto se debe a que el código es innecesariamente complejo y muy poco óptimo, además de que lo escribí hace mucho tiempo y es difícil de seguir. A continuación intentaré volver a crear el código de manera más óptima, con una mayor performance, más comprensible y fácil de seguir, con la menor cantidad posible de errores y una mejor interfaz.

# Datos modificados: Nombre y apellido de alumno, nombre de materia, nota (0 a 10).

# Ejemplo de interfaz final:
# NombreApellido1:
# Materia1: Promedio (Nota1, Nota2, NotaN) | Materia2: Promedio (Nota1, Nota2, NotaN) | MateriaN: Promedio (Nota1, Nota2, NotaN) | ...
# NombreApellido2:
# Materia1: Promedio (Nota1, Nota2, NotaN) | Materia2: Promedio (Nota1, Nota2, NotaN) | MateriaN: Promedio (Nota1, Nota2, NotaN) | ...
# NombreApellidoN:
# Materia1: Promedio (Nota1, Nota2, NotaN) | Materia2: Promedio (Nota1, Nota2, NotaN) | MateriaN: Promedio (Nota1, Nota2, NotaN) | ...
# ...

def matriz_alumnos():
    alumnos = [] # En esta lista se almacenarán los nombres y apellidos de los alumnos
    materias = [] # En esta lista se almacenarán las materias de los alumnos
    notas = [] # En esta lista se almacenarán las notas de los alumnos para calcular el promedio por materia de cada uno
    promedios = [] # En esta lista se almacenarán los alumnos, con su materia y promedio correspondiente
    notas_ind = [] # En esta lista se almacenarán los alumnos, con su materia y notas individuales correspondientes (Nota1, Nota2, NotaN)
    # Bucle para ingreso de datos
    while True:
        nombre_apellido = input('Nombre y apellido ("salir" para finalizar): ')
        if nombre_apellido == 'salir':
            break # Salir del while
        else:
            alumnos.append(nombre_apellido) # Agregar el nombre y apellido a alumnos[]
        materias.append(input('Materia: ')) # Agregar la materia
        nota = input('Nota: ')
        if nota == '' or nota == '-':
            notas.append('-') # Si no cursó la materia, agregar un guion
        else:
            notas.append(nota) # Si cursó la materia, agregar la nota correspondiente
    # Secuencia operacional
    promedios.append([alumnos[0]]) # Agregar la primer lista con NombreApellido a promedios[] para definir matriz.
    notas_ind.append([alumnos[0]]) # Agregar la primer lista con NombreApellido a notas_ind[] para definir matriz.
    for i in range(len(alumnos)): # Recorrer las posiciones de alumnos[]
        posicion_alumno = False # Reestablecer posicion_alumno en caso que el alumno no se encuentre en la lista
        for j in range(len(promedios)): # Recorrer las posiciones de promedios[]
            if alumnos[i] in promedios[j] and not posicion_alumno:
                posicion_alumno = True # Si el alumno se encuentra en la lista, guardar su posición  
                if materias[i] in promedios[j]: # Si la materia ya se encuentra en la lista correspondiente al alumno...
                    posicion_materia = -1 # Reestablecer posicion_materia para su poterior correcto funcionamiento y utilización
                    for k in range(len(promedios[j])): # Recorrer las posiciones de la "sublista" correspondiente al alumno, promedios[[]]
                        if materias[i] == promedios[j][k]:
                            posicion_materia = k # Al encontrar la posición de la materia dentro de esta "sublista", guardarla y frenar el bucle
                            break
                    if notas[i] != '-':
                        promedios[j][posicion_materia + 1] += int(notas[i]) # Sumar la nota a la existente para el promedio (dividendo)
                        promedios[j][posicion_materia + 2] += 1 # Sumar 1 al contador de notas para el promedio (divisor)
                        notas_ind[j].append(int(notas[i])) # Agregar la nota individual a la misma lista
                    break
                else:
                    promedios[j].append(materias[i]) # Si la materia no se encuentra en la lista correspondiente al alumno, agregarla
                    notas_ind[j].append(materias[i]) # Agregar la materia también a la lista de notas individuales del alumno
                    if notas[i] == '-':
                        promedios[j].append(notas[i])
                        notas_ind[j].append(notas[i])
                    else:
                        promedios[j].append(int(notas[i])) # Agregar la nota a la lista para el promedio (dividendo)
                        promedios[j].append(1) # Agregar un contador de notas para el promedio (divisor)
                        notas_ind[j].append(int(notas[i])) # Agregar la nota individual a la misma lista
                    break
        if not posicion_alumno:
            promedios.append([alumnos[i]]) # Si el alumno no se encuentra en la lista, agregarlo
            notas_ind.append([alumnos[i]]) # También agregarlo a la lista de notas individuales
            promedios[-1].append(materias[i]) # Si la materia no se encuentra en la lista correspondiente al alumno, agregarla
            notas_ind[-1].append(materias[i]) # Agregar la materia también a la lista de notas individuales del alumno
            if notas[i] == '-':
                promedios[-1].append(notas[i])
                notas_ind[-1].append(notas[i])
            else:
                promedios[-1].append(int(notas[i])) # Agregar la nota a la lista para el promedio (dividendo)
                promedios[-1].append(1) # Agregar un contador de notas para el promedio (divisor)
                notas_ind[-1].append(int(notas[i])) # Agregar la nota individual a la misma lista
    
    print(promedios)
    print(notas_ind)

#matriz_alumnos()

promedios = [['Rubén', 'Matemática', 27, 3, 'Lengua', 23, 4, 'Física', '-', 'Inglés', 40, 5], ['Ezequiel', 'Matemática', '-', 'Lengua', 33, 4, 'Física', 29, 3], ['Pablo', 'Matemática', 17, 3, 'Lengua', '-', 'Física', 24, 3, 'Alemán', 19, 2]]
notas_ind = [['Rubén', 'Matemática', 10, 9, 8, 'Lengua', 6, 6, 5, 6, 'Física', '-', 'Inglés', 6, 7, 10, 8, 9], ['Ezequiel', 'Matemática', '-', 'Lengua', 9, 8, 9, 7, 'Física', 10, 9, 10], ['Pablo', 'Matemática', 6, 5, 6, 'Lengua', '-', 'Física', 7, 8, 9, 'Alemán', 9, 10]]

for i in range(len(promedios)):
    print(f'{promedios[i][0]}:')
    for j in range(len(promedios[i])):
        #print(f'|J={j}|', end='')
        if j > 0:
            if isinstance(promedios[i][j], str) and promedios[i][j] != '-':
                print(f'{promedios[i][j]}:', end=' ')
                if promedios[i][j + 1] != '-':
                    print(promedios[i][j + 1]/promedios[i][j + 2], end=' ')
                else:
                    print(promedios[i][j + 1], end=' ')
                print('(', end='')
                lista = False
                for k in range(j, len(notas_ind[i])):
                    #print(f'|K={k}|', end='')
                    if lista or notas_ind[i][k] == promedios[i][j]:
                        lista = True
                        for l in range(k, len(notas_ind[i])):
                            #print(f'|L={l}|', end='')
                            if l < len(notas_ind[i]) and isinstance(notas_ind[i][l], int):
                                print(notas_ind[i][l], end='')
                                if l < len(notas_ind[i]) - 1:
                                    if isinstance(notas_ind[i][l + 1], int):
                                        print(', ', end='')
                                    else:
                                        if l == len(notas_ind[i]):
                                            print(')')
                                        else:
                                            print(') | ', end='')
                                        break
                                else:
                                    if l == len(notas_ind[i]):
                                        print(')')
                                    else:
                                        print(') | ', end='')
                                    break
                            else:
                                lista = False
                        break

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

def llenar_pila():
    pila = Stack()
    pila.push('a')
    pila.push('b')
    pila.push('c')
    pila.push('d')
    pila.push('e')
    pila.push('f')
    pila.push('g')
    pila.push('h')
    pila.push('i')
    pila.push('j')
    pila.push('k')
    pila.push('l')

pila_aux = Stack()
llenar_pila()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Búsqueda recursiva de un elemento en una pila.
def buscar_pila(pila, elemento):
    if pila.size() == 0:
        print('Elemento no encontrado.')
        return
    temp = pila.pop()
    if temp == elemento:
        print('Elemento encontrado.')
        pila.push(temp)
    else:
        buscar_pila(pila, elemento)
        pila.push(temp)

# buscar_pila(pila, input('Buscar elemento: '))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Búsqueda recursiva de un elemento en una pila con distancia entre el último elemento y el buscado, o ubicación del elemento dentro de la pila.
def buscar_pila_distancia(pila, elemento):
    if pila.size() == 0:
        print('Elemento no encontrado.')
        return -1
    temp = pila.pop()
    if temp == elemento:
        print('Elemento encontrado.')
        pila.push(temp)
        return 0
    else:
        distancia = buscar_pila_distancia(pila, elemento)
        if distancia != -1:
            distancia += 1
        pila.push(temp)
        return distancia

# distancia = buscar_pila_distancia(pila, input('Buscar elemento: '))
# if distancia != -1:
#     print(f'Si se quitan los últimos {distancia} elementos de la pila, se podrá acceder al elemento buscado.')

# -----------------------------------------------------------------------------------------------------------------------------------------

# Suprimir números impares de una pila de manera recursiva.
def suprimir_impares(pila):
    if pila.size() == 0:
        return
    temp = pila.pop()
    if temp % 2 == 0:
        suprimir_impares(pila)
        pila.push(temp)
    else:
        suprimir_impares(pila)

# -----------------------------------------------------------------------------------------------------------------------------------------

# Un Hola Mundo que se escribe solo recorriendo una a una las letras del abecedario. Puede recibir opcionalmente el tiempo que pasa entre cada letra que se muestra en pantalla.
def hola_mundo_auto(tiempo = 0.04, pos = 0):
    import time
    indice = pos
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Mapeo de letras
    frases_HM = ['', 'H', 'Ho', 'Hol', 'Hola ', 'Hola m', 'Hola mu', 'Hola mun', 'Hola mund', 'Hola mundo']
    letras_HM = ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']
    letra = 0 # Letra inicial
    while True:
        if indice < 9:
            if letras[letra - 1] == letras_HM[pos]: # Si la última letra es 'h'...
                hola_mundo_auto(tiempo ,pos + 1) # Recursividad
                return
        else:
            break
            
        print(frases_HM[indice], letras[letra], sep='')
        if letra < 25: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
            
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.04 seg.
    return frases_HM[9]

# hola_mundo_auto()

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
                print(f'Se presionó la tecla {caracter}.')
            else:
                print('Se presionó una tecla.')
            break
        else:
            print('Sin cambios.')

# presionarTecla()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Este es como el hola_mundo_auto(), con la diferencia de que en este se debe presionar una tecla para detener el abecedario, debiendo quedar la letra correspondiente a la posición del cursor en la palabra "Hola Mundo". Es algo así como un juego del hola_mundo_auto(), de ahí el nombre.

def hola_mundo_juego(tiempo = 0.2, pos = 0):
    import time
    indice = pos
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Mapeo de letras
    frases_HM = ['', 'H', 'Ho', 'Hol', 'Hola ', 'Hola m', 'Hola mu', 'Hola mun', 'Hola mund', 'Hola mundo']
    letras_HM = ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']
    letra = 0 # Letra inicial
    while True:
        if indice < 9:
            if teclaPresionada(None): # Si se presionó una tecla...
                if letras[letra - 1] == letras_HM[pos]: # Si la última letra es "h"...
                    hola_mundo_juego(tiempo, pos + 1)
                    return 'Bien hecho!'
                else:
                    print('Mal ahí, seguí intentando...')
                    letra = 0
                    time.sleep(1) # Esperar 1 segundo
        else:
            break
            
        print(frases_HM[indice], letras[letra], sep='')
        if letra < 25: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
            
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.2 seg
    return frases_HM[9]

# print(hola_mundo_juego())

# -----------------------------------------------------------------------------------------------------------------------------------------

# Función recursiva que imprime la cadena ingresada como parámetro de la misma manera en que hola_mundo_auto() lo haría. Se admiten caracteres alfanuméricos y unos cuantos símbolos. ¿Por qué recursiva? Porque sí, porque queda linda :)
def escribirAuto(cadena, tiempo = 0.02, pos = 0): # Recibe una cadena y la posicion de la letra a buscar en letras
    import time
    indice = pos # Hay lugares en donde pos por poco no es el correcto, por eso lo almaceno antes en indice (como un pos_aux)
    letras = [' ', 'a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', ':', '-', '_', '(', ')', '¿', '?', '¡', '!', '#', '$', '%', '+', '*', '/'] # Mapeo de caracteres
    frases = [''] # Declaración de la lista donde se almacenará la cadena por partes. Siendo f la posición de cada elemento en frases y g la posición de cada elemento en cadena, empezando con f(0)
    extra = -1
    while True:
        if extra < len(cadena) + 1:
            cadenita = ''
            for elemento in range(0, extra):
                cadenita += cadena[elemento]
            if cadenita != '':
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
            if letras[letra - 1] == f'{listaCadena[pos]}'.lower(): # Si la última letra es correcta...
                escribirAuto(cadena, tiempo, pos + 1) # Recursividad
                return ''
        else:
            break
        
        print(frases[indice], letras[letra], sep='')
        if letra < len(letras) - 1: # Para repetir el abcedario después de la Z
            letra += 1
        else:
            letra = 0
          
        time.sleep(tiempo) # Esperar tiempo indicado. Predeterminado: 0.02 seg

# print(escribirAuto('+¿Para el Junior? / -Sí, creo. / +Perfecto! Gracias :)'))

# -----------------------------------------------------------------------------------------------------------------------------------------

# Juego matemático de agilidad mental. Tras un conteo regresivo aparece una operación en pantalla, entonces el usuario deberá ingresar el resultado de ésta, si no lo hace antes de un tiempo indicado se toma como incorrecto, en cuyo caso el jugador perderá una vida y deberá volver a intentar. Si las vidas llegan a 0 entonces piede. Si ingresa el resultado correcto y a tiempo entonces podrá continuar con otra opeación un poco más difícil, de esta manera irá subiendo de nivel. Más pronto sea ingresado el resultado correcto, más puntos obtendrá el usuario. Los puntos se acumulan y al llegar al final del juego son mostrados en pantalla. El final del juego aún no está definido.
# Pienso escribir cada día un poco más del código, haciendo versiones distintas del juego cada vez. Hasta lograr el enunciado de arriba.

def juego_matematico():
    import random
    import time
    # Mensaje de bienvenida y explicación del juego
    print('A continuación se mostrarán distintas operaciones que irán aumentando su dificultad con cada nivel. Si respondés bien subís de nivel, si respondés mal perdés una vida y tanto el nivel como la operación son los mismos. Tenés 5 segundos para ingresar el resultado, si una vez ingresado el tiempo expiró se toma como respuesta incorrecta.')
    input('Presioná cualquier tecla para continuar...')

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
        
        return f'{a} {operador} {b}' # Devolver la operación como una cadena de texto

    def ingresarResultado(resultado): # Función para que el usuario ingrese el resultado de la operación
        inicio = time.time()  # Tiempo de inicio
        respuesta_usuario = input('Ingrese el resultado: ')  # El usuario ingresa su respuesta
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
    operacion = ''  # Operación actual

    while vidas > 0:  # Mientras el jugador tenga vidas
        print('')  # Línea en blanco
        print(f'Nivel: {nivel}')  # Nivel actual
        print(f'Vidas: {vidas}')  # Cantidad de vidas restantes

        if not operacion:  # Si no hay una operación actual generada
            operacion = generar_operacion(nivel)  # Generar una nueva operación para el nivel actual
        print(f'Operación: {operacion}')  # Imprimir la operación actual

        resultado = ingresarResultado(eval(operacion))  # Obtener la respuesta del usuario y evaluarla
        if resultado == -2:  # Si el tiempo expiró y la respuesta es incorrecta.
            vidas -= 1  # Restar una vida
            print('Respuesta incorrecta y iempo expirado.')  # Imprimir un mensaje indicando que ta todo mal
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input('¿Desea salir? (s/n): ')  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == -1:  # Si el tiempo expiró
            vidas -= 1  # Restar una vida
            print('Tiempo expirado.')  # Imprimir un mensaje indicando que el tiempo expiró
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input('¿Desea salir? (s/n): ')  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == 0:  # Si la respuesta es incorrecta
            vidas -= 1  # Restar una vida
            print('Respuesta incorrecta.')  # Imprimir un mensaje indicando que el tiempo expiró
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input('¿Desea salir? (s/n): ')  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                continue  # Continuar con la siguiente iteración del bucle
        elif resultado == 1:  # Si la respuesta es correcta
            print('Respuesta correcta.')  # Imprimir un mensaje indicando que la respuesta es correcta
            if vidas == 0:  # Si ya no quedan vidas
                break  # Salir del bucle
            respuesta = input('¿Desea salir? (s/n): ')  # Preguntar al usuario si desea salir
            if respuesta.lower() == 's':  # Si el usuario desea salir
                break  # Salir del bucle
            elif respuesta.lower() == 'n':  # Si el usuario desea continuar
                operacion = ''  # Reiniciar la operación para generar una nueva en el próximo ciclo
                if nivel < 20:  # Si el nivel actual es menor que 20
                    nivel += 1  # Incrementar el nivel
                else:
                    nivel = 20  # Establecer el nivel máximo
            
    print('Juego terminado.')  # Imprimir un mensaje indicando que el juego ha terminado

# juego_matematico()