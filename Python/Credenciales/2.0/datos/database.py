import json
import os
import random
import string
from .credencial import Credencial

class DataBase:
	def __init__(self, nombre_archivo, ruta_ubicacion = None):
		self.__ruta_ubicacion = ruta_ubicacion
		self.__nombre_archivo = nombre_archivo
		self.__credenciales = self.cargar_datos()
	
	def cargar_datos(self):
		try:
			# self.__ruta_ubicacion = input("Ubicación: ") if self.__ruta_ubicacion is None else self.__ruta_ubicacion
			self.__ruta_ubicacion = ".\\Python\\Credenciales\\2.0\\datos" if self.__ruta_ubicacion is None else self.__ruta_ubicacion
			with open(os.path.expanduser(f"{self.__ruta_ubicacion}\\{self.__nombre_archivo}"), 'r') as archivo:
				return json.load(archivo)
		except FileNotFoundError:
			print(f"Archivo {self.__nombre_archivo} no encontrado. Creando nuevo archivo.")
			return {"credenciales": []}
	
	def guardar_datos(self):
		# self.__ruta_ubicacion = input("Ubicación: ") if self.__ruta_ubicacion is None else self.__ruta_ubicacion
		self.__ruta_ubicacion = ".\\Python\\Credenciales\\2.0\\datos" if self.__ruta_ubicacion is None else self.__ruta_ubicacion
		with open(os.path.expanduser(f"{self.__ruta_ubicacion}\\{self.__nombre_archivo}"), 'w') as archivo:
			json.dump(self.__credenciales, archivo, indent=4, ensure_ascii= False)
	
	def database_vacia(self):
		return True if not self.__credenciales["credenciales"] else False

	def obtener_nombre_archivo(self):
		return self.__nombre_archivo

	def mostrar_credenciales(self):
		if self.database_vacia():
			print(f"Data Base '{self.__nombre_archivo}' vacía")
			return
		print(f"Data Base '{self.__nombre_archivo}':")
		for indice, credencial in enumerate(self.__credenciales["credenciales"]):
			print(f"Usuario: {credencial['usuario']},\nContraseña: {credencial['contrasena']}", end = "\n" if indice < len(self.__credenciales["credenciales"]) - 1 else "\n-- - -- - -- - -- - -- - -- - -- - -- - --\n")

	def buscar_credencial(self, criterio, valor):
		for indice, credencial in self.__credenciales["credenciales"]:
			if credencial[criterio] == valor:
				return indice
	
	def agregar_credencial(self, credencial):
		indice = self.buscar_credencial("usuario", credencial.obtener_usuario())
		if indice is not None:
			print("El nombre de usuario ya existe.")
			return False
		self.__credenciales["credenciales"].append({"usuario": credencial.obtener_usuario(), "contrasena": credencial.obtener_contrasena()})
		return True

	"""def agregar_credencial(self, usuario="", contrasena=""):
		if usuario == "":
			usuario = input("Usuario: ")
		if contrasena == "":
			contrasena = input("Contraseña: ")
		nueva_credencial = Credencial(usuario, contrasena)
		if nueva_credencial.obtener_usuario() != "":
			nueva_credencial.cifrar_usuario()
			nueva_credencial.cifrar_contrasena()
			for credencial in self.__credenciales["credenciales"]:
				if credencial["usuario"] == nueva_credencial.obtener_usuario() or credencial["contrasena"] == nueva_credencial.obtener_contrasena():
					print("El nombre de usuario o la contraseña ya existe.")
					return
			self.__credenciales["credenciales"].append({"usuario": nueva_credencial.obtener_usuario(), "contrasena": nueva_credencial.obtener_contrasena()})
			# self.guardar_datos()
			print(f"Credencial de usuario {usuario} agregada.")"""
	
	def eliminar_credencial(self, usuario="", contrasena=""):
		if usuario == "":
			usuario = input("Usuario: ")
		if contrasena == "":
			contrasena = input("Contraseña: ")
		nueva_credencial = Credencial(usuario, contrasena)
		if nueva_credencial.obtener_usuario() != "":
			nueva_credencial.cifrar_usuario()
			nueva_credencial.cifrar_contrasena()
			for credencial in self.__credenciales["credenciales"]:
				if credencial["usuario"] == nueva_credencial.obtener_usuario():
					if credencial["contrasena"] == nueva_credencial.obtener_contrasena():
						self.__credenciales["credenciales"].remove(credencial)
						# self.guardar_datos()
						print(f"Credencial de usuario {usuario} eliminada.")
					else:
						print("Los datos ingresados son incorrectos.")
					return
			print(f"Credencial de usuario {usuario} no encontrada.")
	
	def modificar_credencial(self, usuario="", usuario_aux="", contrasena="", contrasena_aux=""):
		if usuario == "":
			usuario = input("Usuario: ")
		if contrasena == "":
			contrasena = input("Contraseña: ")
		if usuario_aux == "" and contrasena_aux == "":
			print("Debe ingresar usuario y/o contraseña nuevo/a.")
			return
		nueva_credencial = Credencial(usuario, contrasena)
		if nueva_credencial.obtener_usuario() != "":
			nueva_credencial.cifrar_usuario()
			nueva_credencial.cifrar_contrasena()
			for credencial in self.__credenciales["credenciales"]:
				if credencial["usuario"] == nueva_credencial.obtener_usuario():
					if credencial["contrasena"] == nueva_credencial.obtener_contrasena():
						if usuario_aux != "":
							nuevo_usuario = nueva_credencial.cifrar(usuario_aux)
							credencial["usuario"] = nuevo_usuario
							print(f"Nombre de usuario modificado: {usuario} -> {usuario_aux}")
						elif contrasena_aux != "":
							nueva_contrasena = nueva_credencial.cifrar(contrasena_aux)
							credencial["contrasena"] = nueva_contrasena
							print(f"Constraseña modificada: {contrasena} -> {contrasena_aux}")
						# self.guardar_datos()
						return
					else:
						print("Los datos ingresados son incorrectos.")
					return
			print(f"Credencial de usuario {usuario} no encontrada.")


# db = DataBase("credenciales.json", "C:\\Users\\Estudiante\\Documents\\Visual Studio Code\\Rubo\\Python\\Credenciales")