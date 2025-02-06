class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __eq__(self, other):
        if isinstance(other, Libro):
            return self.titulo == other.titulo and self.autor == other.autor
        return False

    def __hash__(self):
        return hash((self.titulo, self.autor))

biblioteca = {}

def registrar_libro(libro, cantidad):
    if libro in biblioteca:
        biblioteca[libro] += cantidad
    else:
        biblioteca[libro] = cantidad

def consultar_copias(libro):
    return biblioteca.get(libro, 0)

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("1984", "George Orwell")

registrar_libro(libro1, 5)
registrar_libro(libro2, 3)
registrar_libro(libro3, 2)

print(f"Copias de '1984': {consultar_copias(libro1)}")
print(f"Copias de 'Cien años de soledad': {consultar_copias(libro2)}")
