class Persona:

    def __init__(self, nombre, anios):
        self.nombre = nombre
        self.anios = anios

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.anios} anios")