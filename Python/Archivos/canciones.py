import os

nombres = []
artistas = []
canciones = []
contador = 0
sin_guion = "ninguno"
direccion = "D:\\Rubén\\Música\\Canciones\\Nueva carpeta"
archivos = list(os.listdir(direccion))
for item in archivos: #".": Listado en el mismo directorio donde está el fichero de python. Para ruta absoluta: "Unidad:\\Carpeta\\Carpeta"
	# if item[-4:] == ".mp3":
	nombres.append(item)
	if "-" in item:
		for indice, caracter in enumerate(item):
			if caracter == "-":
				artistas.append(item[(indice + 2):-4])
				canciones.append(item[:(indice - 1)])
			else:
				sin_guion = item
		contador += 1

cambio = []
for indice, nombre in enumerate(nombres):
	try:
		cambio.append(artistas[indice] + " - " + canciones[indice] + ".mp3")

		os.rename(f"{direccion}\\{nombres[indice]}", f"{direccion}\\{cambio[indice]}")

		print(f"CAMBIO: {nombres[indice]} -> {cambio[indice]}")
	except FileNotFoundError:
		print("NO SE ENCONTRÓ EL ARCHIVO")