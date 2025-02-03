from ej1.Persona import Persona
from ej2.Empleado import Empleado
from ej3.Producto import Producto, diccionario, mostrar_diccionario, agregar_diccionario, actualizar_diccionario

persona1 = Persona("Jaime", 19)
persona1.saludar()

print()

empleado1 = Empleado("Gaspar", 100, 2)
empleado1.saludar()
empleado1.mostrar_salario()

print()

producto1 = Producto("mazorca de maiz", 1.5)
agregar_diccionario(producto1.nombre, producto1.precio)
mostrar_diccionario()
actualizar_diccionario("mazorca de maiz", 5,0)
mostrar_diccionario()