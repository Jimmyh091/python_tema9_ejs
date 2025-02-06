import re

class Texto:
    def __init__(self, contenido):
        self.contenido = contenido.lower()

    def palabras_unicas(self):
        palabras = re.findall(r'\b\w+\b', self.contenido)
        return set(palabras)

    def frecuencia_palabras(self):
        palabras = re.findall(r'\b\w+\b', self.contenido)
        frecuencia = {}
        for palabra in palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
        return frecuencia

parrafo = """El sol brilla en el cielo. El día es hermoso y el viento sopla suavemente.
El sol calienta la tierra y la gente disfruta del clima."""

texto = Texto(parrafo)

print("Palabras únicas:", texto.palabras_unicas())

print("Frecuencia de palabras:")
for palabra, cantidad in texto.frecuencia_palabras().items():
    print(f"{palabra}: {cantidad}")
