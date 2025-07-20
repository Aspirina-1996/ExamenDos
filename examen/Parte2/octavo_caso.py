class octavo_caso():
    def __init__(self, lista):
        self.lista = lista 

    def procesar(self):
        for palabras in self.lista:
            if "split()" in palabras:
                return palabras.find("split()") 