import os

direccion = "D:\\Rubén\\Música\\Canciones\\Nueva carpeta"
archivos = list(os.listdir(direccion))

numeros = [f"{numero}" for numero in range(0, 100)]
canciones = []
cambio = []
for archivo in archivos:
	if "Billie Eilish" in archivo and "." in archivo:
		contador = 0
		no_va = False
		for indice, caracter in enumerate(archivo):
			if caracter not in numeros:
				contador += 1
			if contador == len(archivo) - 1:
				no_va = True
		if no_va:
			print("No va:", archivo)
		else:
			canciones.append(archivo)
			pI = None
			pF = None
			for indice, caracter in enumerate(archivo):
				if caracter in numeros and pI == None:
					pI = indice
				if caracter == "." and archivo[indice + 1:] != "mp3" and pF == None:
					pF = indice
					break
			if pI is not None and pF is not None:
				cambio.append(archivo[:pI] + archivo[pF + 2:])
			print(f"A cambiar: {archivo} -> {cambio[-1]}")

for indice, cancion in enumerate(canciones):
	os.rename(f"{direccion}\\{cancion}", f"{direccion}\\{cambio[indice]}")
	print("Listo!")