# Clase para el error de ingreso de datos
class ErrorIngreso(Exception):
	# El constructor incluye el requisito que se incumple y el mensaje que se devuelve
	def __init__(self, campo, mensaje="No cumple los requisitos."):
		self.requisito = campo
		self.mensaje = mensaje
		super().__init__(f"Incumplimiento del requisito '{self.requisito}': '{self.mensaje}'")

# Clase para las contraseñas
class Credencial:
	# El constructor incluye una cadena que es la futura contraseña, un usuario vinculado y un código para una posible futura desencriptación
	def __init__(self):
		self.cadena = ""
		self.usuario = ""
		self.codigo = None
	
	# Método para ingresar datos a la credencial (usuario y contraseña)
	def ingresar_datos(self, usuario="", cadena="", codigo=None):

		# Submétodo para ingresar los datos (para manejo de errores)
		def __ingresar(usuario, cadena, codigo):
			alfanumero = "abcdefghijklmnñopqrstuvwxyz0123456789"
			if usuario == "":
				raise ErrorIngreso(campo="Nombre de usuario", mensaje="Debe ingresar un nombre de usuario.")
			elif not all([caracter.lower() in alfanumero for caracter in usuario]):
				raise ErrorIngreso(campo="Caracteres alfanuméricos", mensaje="El nombre de usuario debe ser alfanumérico (sólo letras y números).")
			else:
				if len(cadena) < 8:
					raise ErrorIngreso(campo="Caracteres mínimos", mensaje="La contraseña debe contener al menos 8 caracteres.")
				elif not all([caracter.lower() in alfanumero for caracter in cadena]):
					raise ErrorIngreso(campo="Caracteres alfanuméricos", mensaje="La contraseña debe ser alfanumérica (sólo letras y números).")
				else:
					self.usuario = usuario
					self.cadena = cadena
					self.codigo = codigo
					return True
		
		# Manejo de errores en ingreso de datos
		try:
			return __ingresar(usuario, cadena, codigo)
		except ErrorIngreso as e:
			print(e)
			return False
	
	# Método para contar los caracteres de una contraseña, para posteriormente generar un código de encriptación
	def contar_caracteres(self):
		
		# Submétodo recursivo para conteo de caracteres (para modularidad)
		def __conteo(caracteres, resultado):
			if not caracteres:
				return resultado
			else:
				if caracteres[-1] in resultado:
					resultado[caracteres[-1]] += 1
				else:
					resultado[caracteres[-1]] = 1
				caracteres.pop()
				return __conteo(caracteres, resultado)
		
		# Llamado a la función recursiva con una lista que contiene la contraseña separada en caracteres
		caracteres = list(caracter for caracter in self.cadena)
		return __conteo(caracteres, resultado={})
	
	# Método para generar el código de encriptación, para posteriormente crear el cifrado de la contraseña ingresada
	def generar_codigo(self, recordar=False):
		resultado = self.contar_caracteres()
		# print(f"Resultado: {resultado}")
		codigo = ""
		for caracter in self.cadena:
			codigo += str(resultado[caracter] + len(self.cadena)//4)
		# print(f"Código: {codigo}")
		if recordar:
			self.codigo = codigo
		return codigo
	
	# Método poco útil para eliminar el código de la credencial
	def eliminar_codigo(self):
		self.codigo = None
	
	# Método para encriptar contraseña con un código previamente generado
	def encriptar(self, codigo=None):
		frase = self.cadena
		codigo = self.generar_codigo()
		nueva_frase = ""
		alfanumero = "abcdefghijklmnñopqrstuvwxyz0123456789"
		if len(frase) > 0:
			contador = 0
			for letra in frase:
				if letra != " " and letra in alfanumero:
					desplazamiento = alfanumero.index(letra) + int(codigo[contador])
					while True:
						if desplazamiento < len(alfanumero) - 1:
							break
						else:
							desplazamiento -= len(alfanumero) - 1
					nuevo_caracter = alfanumero[desplazamiento]
					nueva_frase = nueva_frase + nuevo_caracter
				if contador < len(codigo) - 1:
					contador += 1
				else:
					contador = len(codigo) - 1
		return nueva_frase
	
	# Método para desencriptar contraseña con un código específico
	def desencriptar(self, codigo=""):
		pass


# Clase de base de datos
class BaseDatos:
	# El constructor incluye únicamente una lista de credenciales
	def __init__(self):
		self.credenciales = []
	
	# Método para buscar credenciales
	def busqueda(self, criterio, valor):
		for indice, elemento in enumerate(self.credenciales):
			if elemento[criterio] == valor:
				return indice
	
	# Método para agregar credenciales
	def agregar_credenciales(self, usuario="", contrasenia=""):

		# Submétodo para agregar credenciales en el cual se 'hashea' la contraseña (se ingresa, encripta, busca y agrega) (para manejo de errores)
		def __agregar(self, usuario, contrasenia):
			hash = Credencial()
			if hash.ingresar_datos(usuario, contrasenia):
				cifrado = hash.encriptar()
				indice = self.busqueda(criterio="cifrado", valor=cifrado)
				if indice is not None:
					if hash.usuario == self.credenciales[indice]["usuario"]:
						raise ErrorIngreso(campo="Credenciales únicas", mensaje="Las credenciales ingresadas ya existen (duplicado).")
				else:
					self.credenciales.append({"cifrado": cifrado, "usuario": hash.usuario})
					return True

		# Manejo de errores
		try:
			return __agregar(self, usuario, contrasenia)
		except ErrorIngreso as e:
			print(e)
			return False
	
	# Método poco útil para obtener las credenciales
	def get_credenciales(self):
		return self.credenciales
	
	# Método para eliminar credenciales
	def eliminar_credenciales(self, usuario="", contrasenia=""):
		
		# Submétodo para eliminar credenciales donde se 'hashea' la contraseña (para manejo de errores)
		def __eliminar(usuario, contrasenia):
			hash = Credencial()
			if hash.ingresar_datos(usuario, contrasenia):
				cifrado = hash.encriptar()
				indice = self.busqueda("cifrado", cifrado)
				if indice is not None:
					if hash.usuario == self.credenciales[indice]["usuario"]:
						self.credenciales.pop(indice)
						return True
					else:
						raise ErrorIngreso(campo="Credenciales exactas", mensaje="Las credenciales ingresadas son incorrectas.")
				else:
					indice = self.busqueda("usuario", usuario)
					if indice is not None:
						raise ErrorIngreso(campo="Credenciales exactas", mensaje="Las credenciales ingresadas son incorrectas.")
					else:
						raise ErrorIngreso(campo="Credenciales existentes", mensaje="Las credenciales ingresadas no existen.")

		# Manejo de errores
		try:
			return __eliminar(usuario, contrasenia)
		except ErrorIngreso as e:
			print(e)
			return False
	
	# Método para modificar credenciales
	def modificar_credenciales(self, usuario="", contrasenia1="", contrasenia2=""):

		# Submétodo para modificar credenciales donde se 'hashea' la contraseña (para manejo de errores)
		def __modificar(usuario, contrasenia1, contrasenia2):
			hash = Credencial()
			if hash.ingresar_datos(usuario, contrasenia1):
				cifrado = hash.encriptar()
				indice = self.busqueda("cifrado", cifrado)
				if indice is not None:
					if hash.usuario == self.credenciales[indice]["usuario"]:
						if hash.ingresar_datos(usuario, contrasenia2):
							cifrado = hash.encriptar()
							self.credenciales[indice] = {"usuario": usuario, "cifrado": cifrado}
							return True
					else:
						raise ErrorIngreso(campo="Credenciales exactas", mensaje="Las credenciales ingresadas son incorrectas.")
				else:
					indice = self.busqueda("usuario", usuario)
					if indice is not None:
						raise ErrorIngreso(campo="Credenciales exactas", mensaje="Las credenciales ingresadas son incorrectas.")
					else:
						raise ErrorIngreso(campo="Credenciales existentes", mensaje="Las credenciales ingresadas no existen.")

		# Manejo de errores
		try:
			return __modificar(usuario, contrasenia1, contrasenia2)
		except ErrorIngreso as e:
			print(e)
			return False


contrasena_bd = BaseDatos()
# contrasena.ingresar(input("Contraseña: "))

print("OK1" if contrasena_bd.agregar_credenciales("Ruben", "zapallos") else "FAIL1") # Agregar "Ruben" y "zapallos" (OK)
print("OK2" if contrasena_bd.eliminar_credenciales("Ruben", "zapallos") else "FAIL2") # Eliminar "Ruben" y "zapallos" (OK)
print("OK3" if contrasena_bd.agregar_credenciales("Ruben", "zapallos") else "FAIL3") # Agregar "Ruben" y "zapallos" (OK)
print("OK4" if contrasena_bd.modificar_credenciales("Ruben", "zapallos", "cannabis") else "FAIL4") # Modificar contraseña de "Ruben", de "zapallos" a "cannabis" (OK)
print("OK5" if contrasena_bd.agregar_credenciales("Pablo", "Celular1989") else "FAIL5") # Agregar "Pablo" y "Celular1989" (OK)
print("OK6" if contrasena_bd.agregar_credenciales("Ezequiel", "mercedes") else "FAIL6") # Agregar "Ezequiel" y "mercedes" (OK)
print("OK7" if contrasena_bd.agregar_credenciales("Julio", "PopUp2024") else "FAIL7") # Agregar "Julio" y "PopUp2024" (OK)

# Mostrar lista de credenciales guardadas (donde todas las contraseñas se encuentran cifradas)
for indice, elemento in enumerate(contrasena_bd.get_credenciales()):
	print(indice, "| Usuario:", elemento["usuario"], "| Contraseña (cifrada):", elemento["cifrado"])