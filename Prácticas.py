# Búsqueda recursiva de un elemento en una pila.
def buscarPila(pila, elemento):
    if len(pila) == 0:
        print("Elemento no encontrado.")
        return
    temp = pila.pop()
    if temp == elemento:
        print("Elemento encontrado.")
        pila.append(temp)
    else:
        buscarPila(pila, elemento)
        pila.append(temp)

# pila = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# buscarPila(pila, input("Buscar elemento: "))


# Búsqueda recursiva de un elemento en una pila con distancia entre el último elemento y el buscado, o ubicación del elemento dentro de la pila.
def buscarPilaDistancia(pila, elemento):
    if len(pila) == 0:
        print("Elemento no encontrado.")
        return -1
    temp = pila.pop()
    if temp == elemento:
        print("Elemento encontrado.")
        pila.append(temp)
        return 0
    else:
        distancia = buscarPilaDistancia(pila, elemento)
        if distancia != -1:
            distancia += 1
        pila.append(temp)
        return distancia

# pila = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# distancia = buscarPila(pila, "c")
# print(f"Si se quitan los últimos {distancia} elementos de la pila, se podrá acceder al elemento buscado.")

# Hola Mundo
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
def holaMundo(cadena):
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
                    holaMundo(cadena + 1, pos + 1)
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



def holaMundo_auto(cadena):
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
                holaMundo_auto(cadena + 1) # Recursividad
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