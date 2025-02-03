class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aniadir(self):
        diccionario[self.nombre] = self.precio

diccionario = {}

diccionario["pizza"] = 10.0
diccionario["ensalada"] = 1.0
diccionario["switch 2"] = 399.99

def agregar_diccionario(nombre, precio):

    diccionario[nombre] = precio


def actualizar_diccionario(nombre, precio):

    if nombre in diccionario.keys():
        diccionario[nombre] = precio
    else:
        print("Esta clave no se encuentra en el diccionario")


def mostrar_diccionario():

    for nombre, precio in diccionario.items():

        print(f"Nombre: {nombre}, precio: {precio}")