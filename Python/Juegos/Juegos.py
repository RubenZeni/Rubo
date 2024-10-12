# Función que detecta si una tecla ha sido presionada y retorna bool. Puede recibir opcionalemte un caracter y así verificar si la tecla presionada coincide con dicho caracter. Utiliza el módulo msvcrt (únicamente disponible en Windows).

def tecla_presionada_1(tecla):

    def main(caracter):
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

    def presionada(caracter = None): # Esta función sirve para probar teclaPresionada()
        while True:
            if main(caracter):
                if caracter != None:
                    print(f'Se presionó la tecla {caracter}.')
                else:
                    print('Se presionó una tecla.')
                break
            else:
                print('Sin cambios.')

    presionada(tecla)

# -------------------------------------------------------------------------------------------------

# Juego matemático de agilidad mental. Tras un conteo regresivo aparece una operación en pantalla, entonces el usuario deberá ingresar el resultado de ésta, si no lo hace antes de un tiempo indicado se toma como incorrecto, en cuyo caso el jugador perderá una vida y deberá volver a intentar. Si las vidas llegan a 0 entonces piede. Si ingresa el resultado correcto y a tiempo entonces podrá continuar con otra opeación un poco más difícil, de esta manera irá subiendo de nivel. Más pronto sea ingresado el resultado correcto, más puntos obtendrá el usuario. Los puntos se acumulan y al llegar al final del juego son mostrados en pantalla. El final del juego aún no está definido.

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

# -------------------------------------------------------------------------------------------------

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
            if tecla_presionada_1(None): # Si se presionó una tecla...
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

# -------------------------------------------------------------------------------------------------

# Un simple piedra, papel o tijera contra el ordenador. Se escoje una de las tres opciones o salir, mientras no se elija salir se muestra si le ganaste al ordenador, si perdiste o si empataron. Se van sumando los puntos y se van mostrando en pantalla luego de cada ronda.

def piedra_papel_tijera():
    import random
    opciones = ['piedra', 'papel', 'tijera']
    ordenador_puntos = 0
    usuario_puntos = 0
    
    nombre = input('Nombre de usuario: ')

    while True:
        print('Eige una de las siguientes opciones:')
        print('1: PIEDRA')
        print('2: PAPEL')
        print('3: TIJERA')
        print('0. SALIR')
        usuario = int(input(''))

        if usuario == 0:
            print('¡Gracias por jugar!')
            break
        else:
            usuario = opciones[usuario - 1]

        ordenador = random.choice(opciones)
        print(f'\n¡{usuario.upper()} vs {ordenador.upper()}!')

        if usuario not in opciones:
            print('Error, opción no válida.', end='\n\n')
        elif (usuario == 'piedra' and ordenador == 'tijera') or (usuario == 'papel' and ordenador == 'piedra') or (usuario == 'tijera' and ordenador == 'papel'):
            print('¡Ganaste!', end='\n\n')
            usuario_puntos += 1
        elif usuario == ordenador:
            print('¡Empate!', end='\n\n')
        else:
            print('¡Perdiste!', end='\n\n')
            ordenador_puntos += 1
        
        print(f'{nombre}: {usuario_puntos} puntos.')
        print(f'Ordenador: {ordenador_puntos} puntos.', end='\n\n')

# piedra_papel_tijera()