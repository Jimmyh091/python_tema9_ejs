from ej1.Persona import Persona


class Empleado(Persona):

    def __init__(self, nombre, anios, salario):
        super().__init__(nombre, anios)
        self.salario = salario

    def mostrar_salario(self):
        print(f"El salario es {self.salario + self.salario * 0.21}")
