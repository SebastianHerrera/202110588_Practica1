class Cliente:
    def __init__(self, nombre, direccion, correo, telefono, pastel, tiempo):
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono
        self.pastel = pastel
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None