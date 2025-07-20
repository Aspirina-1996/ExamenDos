class segundo_caso():
    def __init__(self, lenguaje, lista):
        self.lenguaje  = lenguaje
        self.lista = lista

    def procesar(self):
        for palabras in self.lista:
            if self.lenguaje in palabras:
                return palabras.upper()
