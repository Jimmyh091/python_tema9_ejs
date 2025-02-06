registrados = {"Ana", "Juan", "Luis", "Pedro", "María", "Sofía", "Carlos"}

aprobados = {"Juan", "Luis", "María", "Sofía"}

alumnos_aprobados = registrados.intersection(aprobados)

alumnos_no_aprobados = registrados.difference(aprobados)

print("Alumnos que aprobaron:", alumnos_aprobados)
print("Alumnos registrados que no aprobaron:", alumnos_no_aprobados)
