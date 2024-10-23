def encriptar(frase):
	nueva_frase = ""
	if len(frase) > 0:
		for letra in frase:
			if letra != " ":
				nueva_letra = chr(ord(letra) + 3)
				nueva_frase = nueva_frase + nueva_letra
	return nueva_frase

def desencriptar(frase):
	nueva_frase = ""
	if len(frase) > 0:
		for letra in frase:
			if letra != " ":
				if letra in ["x", "y", "z"]:
					if letra == "x":
						letra = "^"
				nueva_letra = chr(ord(letra) - 3)
				nueva_frase = nueva_frase + nueva_letra
	return nueva_frase

encriptadas = []
desencriptadas = []

while True:
	respuesta = input("¿Encriptar o Desencriptar? (E/D)\n").lower()
	if respuesta == "e":
		texto = input("Texto a encriptar: ")
		texto = encriptar(texto)
		encriptadas.append(texto)
		print(texto)
		if input("¿Desea ver las palabras encriptadas? (S/N)").lower() == "s":
			print(encriptadas)
	elif respuesta == "d":
		texto = input("Texto a desencriptar: ")
		texto = desencriptar(texto)
		desencriptadas.append(texto)
		print(texto)
		if input("¿Desea ver las palabras desencriptadas? (S/N)").lower() == "s":
			print(desencriptadas)
	if input("¿Reiniciar? (S/N)").lower() == "n":
		break