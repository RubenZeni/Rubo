import os
# import subprocess
from error import Error
import comandos

# Bucle principal
invocador = comandos.Invocador()

db = None  # Base de datos vacía
reset = False

while True:
	try:
		instruccion = input(". ")

		if instruccion.lower().startswith("new"):
			if instruccion.lower().removeprefix("new").strip().startswith("database"):
				invocador.registrar_comando("new", comandos.ComandoNew(instruccion, db))
				db = invocador.ejecutar_comando("new")
				if not isinstance(db, comandos.DataBase):
					db = None
				elif db.database_nula():
					db = None

			elif instruccion.lower().removeprefix("new").strip().startswith("credencial"):
				invocador.registrar_comando("new", comandos.ComandoNew(instruccion, db))
				credencial = invocador.ejecutar_comando("new")
				if not isinstance(credencial, comandos.Credencial):
					credencial = None
		
		elif instruccion.lower().startswith("load"):
			invocador.registrar_comando("load", comandos.ComandoLoad(instruccion, db))
			db = invocador.ejecutar_comando("load")
			if not isinstance(db, comandos.DataBase):
				db = None
			elif db.database_nula():
				db = None
		
		elif instruccion.lower().startswith("save"):
			invocador.registrar_comando("save", comandos.ComandoSave(instruccion, db))
			if instruccion.lower().removeprefix("save").strip().startswith("credencial"):
				invocador.ejecutar_comando("save", credencial)
			else:
				invocador.ejecutar_comando("save")

		elif instruccion.lower().startswith("get"):
			invocador.registrar_comando("get", comandos.ComandoGet(instruccion, db))
			invocador.ejecutar_comando("get")

		elif instruccion.lower().startswith("help"):
			invocador.registrar_comando("help", comandos.ComandoHelp(instruccion, db))
			invocador.ejecutar_comando("help")
		
		elif instruccion.lower() in ["clear", "cls"]:
			os.system("cls" if os.name == "nt" else "clear") # Limpiar consola (nt = Windows)
		
		elif instruccion.lower() in ["reset", "restart"]:
			reset = True
			break

		elif instruccion.lower() == "exit":
			reset = False
			break
		
		else:
			print(f"Comando '{instruccion}' no reconocido. Usa 'help' para ver los comandos disponibles.")

	except Error as error:
		print(error)

if reset:
	print("Reiniciando el script...")
	# subprocess.Popen(["python", __file__])  # Ejecuta una nueva instancia del mismo script
else:
	print("Saliendo del script...")