from credencial import Credencial
from dataBase import DataBase

class Error(Exception):
	def __init__(self, tipo, mensaje="Algo falló xd"):
		self.numero = tipo
		self.mensaje = mensaje
		super().__init__(f"ERROR {self.numero}: {self.mensaje}.")

cargado = False
db = None

while True:
	try:
		instruccion = input(". ")
		if instruccion.lower().startswith("new"):
			print("|NEW|")
			if instruccion[4:].lower().startswith("credencial"):
				print("|CREDENCIAL|")
				if instruccion[14:].lower().startswith(" -"):
					print("|GUION|")
				else:
					print("|SIN GUION|")
			elif instruccion[4:].lower().startswith("database"):
				print("|DATABASE|")
				if instruccion[12:].lower().startswith(" -"):
					print("|GUION|")
					if instruccion[14:].lower().endswith("json"):
						print("|SIN RUTA|")
						nombre_archivo = instruccion[14:]
						print(f"Nombre del archivo: {nombre_archivo}")
					else:
						print("|CON RUTA|")
						indice = instruccion.find(".json -")
						if indice >= 0:
							nombre_archivo = instruccion[14:indice+5]
							ruta_ubicacion = instruccion[indice+7:]
							print(f"Ruta/Ubicación: {ruta_ubicacion}, Nombre del archivo: {nombre_archivo}")
							db = DataBase(nombre_archivo, ruta_ubicacion)
						else:
							print("Error en la especificación del archivo.")
				else:
					print("|SIN GUION|")
			else:
				print("|SIN CREDENCIAL/DATABASE|")
		elif instruccion.lower().startswith("get"):
			print("|GET|")
			if instruccion[4:].lower().startswith("credencial"):
				print("|CREDENCIAL|")
				if instruccion[14:].lower().startswith(" -"):
					print("|GUION|")
				else:
					print("|SIN GUION|")
			elif instruccion[4:].lower().startswith("database"):
				print("|DATABASE|")
				if instruccion[12:].lower().startswith(" -"):
					print("|GUION|")
					if instruccion[14:].lower().endswith("json"):
						print("|SIN RUTA|")
						nombre_archivo = instruccion[14:]
						print(f"Nombre del archivo: {nombre_archivo}")
					else:
						print("|CON RUTA|")
						indice = instruccion.find(".json -")
						if indice >= 0:
							nombre_archivo = instruccion[14:indice+5]
							ruta_ubicacion = instruccion[indice+7:]
							print(f"Ruta/Ubicación: {ruta_ubicacion}, Nombre del archivo: {nombre_archivo}")
							db = DataBase(nombre_archivo, ruta_ubicacion)
						else:
							print("Error en la especificación del archivo.")
				else:
					print("|SIN GUION|")
					if db is not None:
						db.mostrar_credenciales()
					else:
						print("No hay DataBase cargada.")
			else:
				print("|SIN CREDENCIAL/DATABASE|")
		elif instruccion.lower().endswith("help"):
			print("|HELP|")
			print("Sintaxis: comando -parametro1 -parametro2 -parametroN (se debe respetar el guion).")
			print("\nComandos:")
			print("new		Crear nueva credencial/database.")
			print("get		Obtener credencial/database ya cargada.")
			print("load		Cargar credencial/database existente.")
			print("\n Para ver los parámetros usa 'help comando'")
		elif instruccion.lower().startswith("help"):
			if instruccion[5:].lower().startswith("new"):
				print("|HELP NEW|")
				print("Sintaxis: new -parametro1 -parametro2 -parametroN")
				print("\nParámetros de new:")
				print("database		Base de datos (json).")
				print("credencial	Credencial (usuario y contraseña).")
			elif instruccion[5:].lower().startswith("load"):
				print("|HELP LOAD|")
				print("Sintaxis: load -parametro1 -parametro2 -parametroN")
				print("\nParámetros de load:")
				print("database		Base de datos (json).")
				print("credencial	Credencial (usuario y contraseña).")
			elif instruccion[5:].lower().startswith("get"):
				print("|HELP GET|")
				print("Sintaxis: get -parametro1 -parametro2 -parametroN")
				print("\nParámetros de get:")
				print("database		Base de datos (json).")
				print("credencial	Credencial (usuario y contraseña).")
		elif instruccion.lower().startswith("exit"):
			break
		elif instruccion.lower().startswith(""):
			print("|SIN NEW/GET/HELP|")
			raise Error(tipo="Comando inválido", mensaje="Usa 'help' para ver los comandos.")
	except IndexError:
		print("IndexError")
	except Error as error:
		print(error)