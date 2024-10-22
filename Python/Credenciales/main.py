from credencial import Credencial
from dataBase import DataBase

class Error(Exception):
	def __init__(self, numero, mensaje="Algo falló xd"):
		self.numero = numero
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
		else:
			print("|SIN NEW|")
	except IndexError:
		print("IndexError")
	except Error as error:
		print(error)