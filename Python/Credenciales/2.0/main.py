import comandos
import sys  
sys.path.append('C:\\VSCode\\Rubo\\Python\\Credenciales\\2.0\\datos')

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
        instruccion = input(". ").strip().lower()

        if instruccion.startswith("new"):
            invocador.registrar_comando("new", comandos.ComandoNew(instruccion, db))
            invocador.ejecutar_comando("new")

        elif instruccion.startswith("get"):
            invocador.registrar_comando("get", comandos.ComandoGet(instruccion, db))
            invocador.ejecutar_comando("get")

        elif instruccion.startswith("help"):
            invocador.registrar_comando("help", comandos.ComandoHelp(instruccion, db))
            invocador.ejecutar_comando("help")
        
        elif instruccion == "exit":
            break
        
        else:
            print(f"Comando '{instruccion}' no reconocido. Usa 'help' para ver los comandos disponibles.")

    except Error as error:
        print(error)