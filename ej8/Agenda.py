class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"El contacto {nombre} no existe.")

    def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, "Contacto no encontrado")

    def mostrar_agenda(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")

mi_agenda = Agenda()

mi_agenda.agregar_contacto("Ana", "123456789")
mi_agenda.agregar_contacto("Juan", "987654321")
mi_agenda.agregar_contacto("Luis", "555666777")

print("Buscar Ana:", mi_agenda.buscar_contacto("Ana"))
print("Buscar Pedro:", mi_agenda.buscar_contacto("Pedro"))

mi_agenda.mostrar_agenda()

mi_agenda.eliminar_contacto("Juan")

mi_agenda.mostrar_agenda()
