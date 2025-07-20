class setimo_caso():
    def __init__(self, lista):
        self.lista = lista 

    def procesar(self):
        for palabras in self.lista:
            if "cielo azul" in palabras:
                return palabras.swapcase()
                