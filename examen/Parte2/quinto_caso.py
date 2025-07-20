class quinto_caso():
    def __init__(self, lista):
        self.lista = lista 

    def procesar(self):
        for palabras in self.lista:
            if palabras.isalpha():
                return palabras