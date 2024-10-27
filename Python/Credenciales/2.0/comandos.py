# =========================== INVOCADOR ===========================
class Invocador:
	def __init__(self):
		self.comandos = {}

	def registrar_comando(self, nombre, comando):
		self.comandos[nombre] = comando

	def ejecutar_comando(self, nombre):
		comando = self.comandos.get(nombre)
		if comando:
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
					print(f"Usuario: {usuario} | Contraseña: {contrasena}")
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
		pass

# --------------------------- SAVE ---------------------------
class ComandoSave(Comando):
	def __init__(self, instruccion, db):
		self.instruccion = instruccion
		self.db = db
	
	def ejecutar(self):
		accion = self.instruccion.removeprefix("save").strip()
		if accion.lower().startswith("credencial"):
			accion = accion.removeprefix("credencial").strip()
			pass
		elif accion.lower().startswith("database"):
			accion = accion.removeprefix("database").strip()
			if self.db.database_vacia():
				print("La DataBase se encuentra vacía. ¿Guardar de todas maneras? (S/N)")
				if input(". ").lower() == "s":
					self.db.guardar_datos()
					print("Datos guardados exitosamente.")
				else:
					return

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
				print("No hay base de datos cargada.")

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