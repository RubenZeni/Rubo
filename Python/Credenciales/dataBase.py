import json
import os
import random
import string
from credencial import Credencial

class DataBase:
	def __init__(self, nombre_archivo):
		self.__nombre_archivo = nombre_archivo
		self.__credenciales = self.cargar_datos()
	
	def cargar_datos(self):
		try:
			with open(os.path.expanduser(f"C:\\VSCode\\Local\\Python\\Proyectos\\Credenciales\\{self.__nombre_archivo}"), 'r') as archivo:
				return json.load(archivo)
			# with open(self.__nombre_archivo, "r") as archivo:
			# 	return {"credenciales": json.load(archivo)}
		except FileNotFoundError:
			print(f"Archivo {self.__nombre_archivo} no encontrado, creando uno nuevo.")
			return {"credenciales": []}
	
	def guardar_datos(self):
		with open(os.path.expanduser(f"C:\\VSCode\\Local\\Python\\Proyectos\\Credenciales\\{self.__nombre_archivo}"), 'w') as archivo:
			json.dump(self.__credenciales, archivo, indent=4, ensure_ascii= False)
	
	def mostrar_credenciales(self):
		print("Credenciales guardadas:")
		for credencial in self.__credenciales["credenciales"]:
			print(f"Usuario: {credencial['usuario']}, Contraseña: {credencial['contrasena']}")
	
	def agregar_credencial(self, usuario="", contrasena=""):
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
			self.guardar_datos()
			print(f"Credencial de usuario {usuario} agregada.")
	
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
						self.guardar_datos()
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
							self.guardar_datos()
							print(f"Nombre de usuario modificado: {usuario} -> {usuario_aux}")
						elif contrasena_aux != "":
							nueva_contrasena = nueva_credencial.cifrar(contrasena_aux)
							credencial["contrasena"] = nueva_contrasena
							self.guardar_datos()
							print(f"Constraseña modificada: {contrasena} -> {contrasena_aux}")
							
						return
					else:
						print("Los datos ingresados son incorrectos.")
					return
			print(f"Credencial de usuario {usuario} no encontrada.")


db = DataBase("credenciales.json")
db.mostrar_credenciales()
print("")
# db.agregar_credencial()
# print("")
db.mostrar_credenciales()
print("")
db.modificar_credencial(usuario="PabloZeni", contrasena_aux="Raul3000.", contrasena="HDataya23.")