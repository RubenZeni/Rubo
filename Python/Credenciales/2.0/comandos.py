# =========================== INVOCADOR ===========================
class Invocador:
	def __init__(self):
		self.comandos = {}

	def registrar_comando(self, nombre, comando):
		self.comandos[nombre] = comando

	def ejecutar_comando(self, nombre, credencial=None):
		comando = self.comandos.get(nombre)
		if comando:
			if credencial is not None:
				return comando.ejecutar(credencial)
			return comando.ejecutar()
		else:
			print(f"Comando no reconocido: '{nombre}'")

# =========================== COMANDOS ===========================
from datos.credencial import Credencial
from datos.database import DataBase
from error import Error

# --------------------------- COMANDO ---------------------------
class Comando:
	def ejecutar(self):
		raise NotImplementedError("Este método debe ser implementado.")

# --------------------------- NEW ---------------------------
class ComandoNew(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db

	def ejecutar(self):
		accion = self.instruccion.removeprefix("new").strip()
		if accion.lower().startswith("credencial"):
			accion = accion.removeprefix("credencial").strip()
			if accion.lower().startswith("-"):
				indice = accion.find(" -")
				if indice >= 0:
					usuario = accion[1:indice]
					contrasena = accion[indice+2:]
					credencial = Credencial(usuario=usuario, contrasena=contrasena)
					credencial.cifrar_credencial()
					print("Credencial creada exitosamente")
					return credencial
		elif accion.lower().startswith("database"):
			if self.db is not None:
				print(f"Actualmente se está trabajando en la DataBase '{self.db.obtener_nombre_archivo()[:-5]}'. ¿Reemplazar por '{nombre_archivo[:-5]}'? (S/N)")
				if input(". ").lower() == "s":
					print(f"¿Guardar '{self.db.obtener_nombre_archivo()[:-5]}'? (S/N)")
					if input(". ").lower() == "s":
						self.db.guardar_datos()
						print("Datos guardados exitosamente.")
			accion = accion.removeprefix("database").strip()
			if accion.lower().endswith(".json"):
				nombre_archivo = accion[1:]
				self.db = DataBase(nombre_archivo)
			else:
				indice = accion.find(".json -")
				if indice >= 0:
					nombre_archivo = accion[1:indice+5]
					ruta_ubicacion = accion[indice+7:]
					self.db = DataBase(nombre_archivo, ruta_ubicacion)
				else:
					print("Error en la especificación del archivo.")
			return self.db

# --------------------------- LOAD ---------------------------
class ComandoLoad(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db
	
	def ejecutar(self):
		accion = self.instruccion.removeprefix("load").strip()
		if accion.lower().startswith("credencial"):
			"""accion = accion.removeprefix("credencial").strip()
			if accion.lower().startswith("-"):
				indice = accion.find(" -")
				if indice >= 0:
					usuario = accion[1:indice]
					contrasena = accion[indice+2:]
					credencial = Credencial(usuario=usuario, contrasena=contrasena)
					credencial.cifrar_credencial()
					print("Credencial creada exitosamente")
					return credencial"""
			pass
		elif accion.lower().startswith("database"):
			if self.db is not None:
				print(f"Actualmente se está trabajando en la DataBase '{self.db.obtener_nombre_archivo()[:-5]}'. ¿Reemplazar por '{nombre_archivo[:-5]}'? (S/N)")
				if input(". ").lower() == "s":
					print(f"¿Guardar '{self.db.obtener_nombre_archivo()[:-5]}'? (S/N)")
					if input(". ").lower() == "s":
						self.db.guardar_datos()
						print("Datos guardados exitosamente.")
			accion = accion.removeprefix("database").strip()
			if accion.lower().endswith(".json"):
				nombre_archivo = accion[1:]
				self.db = DataBase(nombre_archivo, carga=True)
			else:
				indice = accion.find(".json -")
				if indice >= 0:
					nombre_archivo = accion[1:indice+5]
					ruta_ubicacion = accion[indice+7:]
					self.db = DataBase(nombre_archivo, ruta_ubicacion, carga=True)
				else:
					print("Error en la especificación del archivo.")
			return self.db

# --------------------------- SAVE ---------------------------
class ComandoSave(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db
	
	def ejecutar(self, credencial=None):
		accion = self.instruccion.removeprefix("save").strip()
		if accion.lower().startswith("credencial"):
			accion = accion.removeprefix("credencial").strip()
			if self.db is None:
				print("No hay Base de Datos cargada.")
				return
			if credencial is None:
				return
			if self.db.agregar_credencial(credencial):
				print("Credencial guardada exitosamente.")
		elif accion.lower().startswith("database"):
			accion = accion.removeprefix("database").strip()
			if self.db.database_vacia():
				print("La Base de Datos se encuentra vacía. ¿Guardar de todas maneras? (S/N)")
				if input(". ").lower() == "s":
					self.db.guardar_datos()
					print("Datos guardados exitosamente.")
				else:
					return
			self.db.guardar_datos()
			print("Datos guardados exitosamente.")

# --------------------------- GET ---------------------------
class ComandoGet(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db

	def ejecutar(self):
		accion = self.instruccion.removeprefix("get").strip()
		if accion.lower().startswith("credencial"):
			print("Obteniendo credencial...")
			# Lógica para obtener una credencial
		elif accion.lower().startswith("database"):
			if self.db is not None:
				self.db.mostrar_credenciales()
			else:
				print("No hay Base de Datos cargada.")

# --------------------------- HELP ---------------------------
class ComandoHelp(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db
	
	def ejecutar(self):
		accion = self.instruccion.removeprefix("help").strip()
		if accion.lower().startswith("new"):
			print("Sintaxis: new comandoSecundario -parametro1 -parametro2 -parametroN")
			print("\nComandos secundarios de new:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.lower().startswith("load"):
			print("Sintaxis: load comandoSecundario -parametro1 -parametro2 -parametroN")
			print("\nComandos secundarios de load:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.lower().startswith("save"):
			print("Sintaxis: save comandoSecundario -parametro1 -parametro2 -parametroN")
			print("\nComandos secundarios de save:")
			print("credencial		Credencial (usuario y contraseña).")
		elif accion.lower().startswith("get"):
			print("Sintaxis: get comandoSecundario -parametro1 -parametro2 -parametroN")
			print("\nComandos secundarios de get:")
			print("database		Base de datos (json).")
			print("credencial		Credencial (usuario y contraseña).")
		else:
			print("Sintaxis: comandoPrimario comandoSecundario -parametro1 -parametro2 -parametroN (se debe respetar el guion).")
			print("\nComandos primarios:")
			print("new			Crear nueva credencial/database.")
			print("get			Obtener credencial/database ya cargada.")
			print("load			Cargar credencial/database existente.")
			print("\n Para ver los comandos secundarios usa 'help comandoPrimario'")