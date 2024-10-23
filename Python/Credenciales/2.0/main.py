import comandos
import os

class Error(Exception):
    def __init__(self, tipo, mensaje="Algo falló xd"):
        self.numero = tipo
        self.mensaje = mensaje
        super().__init__(f"ERROR {self.numero}: {self.mensaje}.")

# Bucle principal
invocador = comandos.Invocador()

db = None  # Base de datos vacía

while True:
    try:
        instruccion = input(". ")

        if instruccion.lower().startswith("new"):
            invocador.registrar_comando("new", comandos.ComandoNew(instruccion, db))
            db = invocador.ejecutar_comando("new")

        elif instruccion.lower().startswith("get"):
            invocador.registrar_comando("get", comandos.ComandoGet(instruccion, db))
            invocador.ejecutar_comando("get")

        elif instruccion.lower().startswith("help"):
            invocador.registrar_comando("help", comandos.ComandoHelp(instruccion, db))
            invocador.ejecutar_comando("help")
        
        elif instruccion.lower() in ["clear", "cls"]:
            os.system("cls" if os.name == "nt" else "clear") # Limpiar consola (nt = Windows)
        
        elif instruccion.lower() == "exit":
            break
        
        else:
            print(f"Comando '{instruccion}' no reconocido. Usa 'help' para ver los comandos disponibles.")

    except Error as error:
        print(error)