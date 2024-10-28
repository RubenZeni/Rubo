class ErrorIngresoDatos(Exception):
	def __init__(self, requisito, mensaje="Incumplimiento de los requisitos de ingreso de datos."):
		self.requisito = requisito
		self.mensaje = mensaje
		super().__init__(f"ERROR {self.requisito}: {self.mensaje}")

class Credencial:
	def __init__(self, usuario="", contrasena=""):
		usuario = usuario if usuario != "" else input("Usuario: ")
		contrasena = contrasena if contrasena != "" else input("Contraseña: ")

		self.__usuario,	self.__contrasena = self.ingresar_datos(usuario, contrasena)
		self.__codigo = None
	
	def ingresar_datos(self, usuario, contrasena):
		def __ingresar(usuario, contrasena):
			minusculas = "abcdefghijklmnñopqrstuvwxyz"
			mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
			numeros = "0123456789"
			simbolos = "._-"
			if usuario == "":
				raise ErrorIngresoDatos(requisito="001", mensaje="Debe ingresar un nombre de usuario válido.")
			elif contrasena == "":
				raise ErrorIngresoDatos(requisito="002", mensaje="Debe ingresar una contraseña válida.")
			elif len(contrasena) < 8:
				raise ErrorIngresoDatos(requisito="003", mensaje="La contraseña debe contener al menos 8 caracteres.")
			elif not all([(caracter in minusculas or caracter in mayusculas or caracter in numeros or caracter in simbolos) for caracter in usuario]):
				raise ErrorIngresoDatos(requisito="004", mensaje="El nombre de usuario debe ser alfanumérico (sólo letras y números) y puede contener los símbolos '. - _'.")
			elif not all([(caracter in minusculas or caracter in mayusculas or caracter in numeros or caracter in simbolos) for caracter in contrasena]):
				raise ErrorIngresoDatos(requisito="005", mensaje="La contraseña debe ser alfanumérica (sólo letras y números) y puede contener los símbolos '. - _'.")
			elif not (any(caracter in minusculas for caracter in contrasena) and any(caracter in mayusculas for caracter in contrasena) and any(caracter in numeros for caracter in contrasena)):
				raise ErrorIngresoDatos(requisito="006", mensaje="La contraseña debe contener al menos una mayúscula, una minúscula y un número.")
			else:
				return usuario, contrasena
		
		try:
			return __ingresar(usuario, contrasena)
		except ErrorIngresoDatos as e:
			print(e)
			return "", ""
	
	def mostrar_datos(self):
		print (f"Usuario: {self.__usuario} - Contraseña: {self.__contrasena} - Código: {self.__codigo}.")
	
	def obtener_usuario(self):
		return self.__usuario
	
	def obtener_contrasena(self):
		return self.__contrasena
	
	def obtener_codigo(self):
		return self.__codigo
	
	def generar_codigo(self, cadena, recordar=False):
		def __conteo(cadena, registro={}):
			if cadena == "":
				return registro
			else:
				if cadena[0] not in registro:
					registro[cadena[0]] = 1
				else:
					registro[cadena[0]] += 1
			return __conteo(cadena[1:], registro)
		
		def __generacion(cadena, registro, codigo=[]):
			abece = "0aAbBc1CdDeEf2FgGhH3i.IjJkK4lLmMn5NñÑoOp6Pq_QrR7sStTuU8vVwWx9-XyYzZ"
			if cadena == "":
				return codigo
			else:
				indice = abece.index(cadena[-1])
				indice += registro[cadena[-1]] + 7
				if indice > len(abece) - 1:
					indice -= len(abece) - 1
				codigo.append(indice)
			return __generacion(cadena[:-1], registro, codigo)
		
		registro = __conteo(cadena)
		codigo = __generacion(cadena, registro)
		if recordar:
			self.__codigo = codigo
		return codigo
	
	def eliminar_codigo(self):
		self.__codigo = None
	
	def cifrar(self, cadena, recordar=False):
		def __cifrar(cadena, codigo, cifrado=""):
			abece = "0aAbBc1CdDeEf2FgGhH3i.IjJkK4lLmMn5NñÑoOp6Pq_QrR7sStTuU8vVwWx9-XyYzZ"
			if cadena == "" and not codigo:
				return cifrado
			else:
				cifrado += abece[codigo[-1]]
			return __cifrar(cadena[:-1], codigo[:-1], cifrado)
		
		codigo = self.generar_codigo(cadena, recordar=recordar)
		return __cifrar(cadena, codigo)
	
	def cifrar_usuario(self):
		self.__usuario = self.cifrar(self.__usuario, recordar=True)
	
	def cifrar_contrasena(self):
		self.__contrasena = self.cifrar(self.__contrasena, recordar=True)

	def cifrar_credencial(self):
		if self.__usuario != "":
			self.cifrar_usuario()
			self.cifrar_contrasena()
			self.eliminar_codigo()