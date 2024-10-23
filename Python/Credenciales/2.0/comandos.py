# =========================== INVOCADOR ===========================
class Invocador:
	def __init__(self):
		self.comandos = {}

	def registrar_comando(self, nombre, comando):
		self.comandos[nombre] = comando

	def ejecutar_comando(self, nombre):
		comando = self.comandos.get(nombre)
		if comando:
			comando.ejecutar()
		else:
			print(f"No se reconoce el comando: {nombre}")


# =========================== COMANDOS ===========================
from datos.credencial import Credencial
from datos.database import DataBase

class Comando:
	def ejecutar(self):
		raise NotImplementedError("Este método debe ser implementado.")


class ComandoNew(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db

	def ejecutar(self):
		accion = self.instruccion.removeprefix("new").strip()
		if accion.startswith("credencial"):
			print("Se está creando una nueva credencial.")
			# Lógica para crear una nueva credencial
		elif accion.startswith("database"):
			print("Se está creando una nueva base de datos.")
			accion = accion.removeprefix("database").strip()
			if accion.lower().endswith("json"):
				print(f"Nombre del archivo: {accion}")
			else:
				indice = accion.find(".json -")
				if indice >= 0:
					nombre_archivo = accion[1:indice+5]
					ruta_ubicacion = accion[indice+7:]
					print(f"Ruta/Ubicación: {ruta_ubicacion}, Nombre del archivo: {nombre_archivo}")
					db = DataBase(nombre_archivo, ruta_ubicacion)
				else:
					print("Error en la especificación del archivo.")


class ComandoGet(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db

	def ejecutar(self):
		accion = self.instruccion.removeprefix("get").strip()
		if accion.startswith("credencial"):
			print("Obteniendo credencial...")
			# Lógica para obtener una credencial
		elif accion.startswith("database"):
			if self.db:
				print("Obteniendo base de datos...")
				self.db.mostrar_credenciales()
			else:
				print("No hay base de datos cargada.")


class ComandoHelp(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db
	
	def ejecutar(self):
		accion = self.instruccion.removeprefix("help").strip()
		if accion.startswith("new"):
			print("Sintaxis: new -parametro1 -parametro2 -parametroN")
			print("\nParámetros de new:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.startswith("load"):
			print("Sintaxis: load -parametro1 -parametro2 -parametroN")
			print("\nParámetros de load:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.startswith("save"):
			print("Sintaxis: save -parametro1 -parametro2 -parametroN")
			print("\nParámetros de save:")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.startswith("get"):
			print("Sintaxis: get -parametro1 -parametro2 -parametroN")
			print("\nParámetros de get:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		else:
			print("Sintaxis: comando -parametro1 -parametro2 -parametroN (se debe respetar el guion).")
			print("\nComandos:")
			print("new			Crear nueva credencial/database.")
			print("get			Obtener credencial/database ya cargada.")
			print("load			Cargar credencial/database existente.")
			print("\n Para ver los parámetros usa 'help comando'")