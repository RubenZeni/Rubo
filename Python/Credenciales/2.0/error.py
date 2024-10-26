class Error(Exception):
    def __init__(self, nombre, mensaje="Algo falló xd"):
        self.nombre = nombre
        self.mensaje = mensaje
        super().__init__(f"'{self.nombre}': {self.mensaje}.")