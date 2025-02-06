class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __lt__(self, other):
        return self.salario < other.salario

    def __repr__(self):
        return f"{self.nombre} - ${self.salario}"

empleados = [
    Empleado("Ana", 3000),
    Empleado("Juan", 2500),
    Empleado("Luis", 4000),
    Empleado("Pedro", 3500),
    Empleado("Sofía", 2800)
]

empleados_ordenados = sorted(empleados)

print("Empleados ordenados por salario:")
for emp in empleados_ordenados:
    print(emp)
