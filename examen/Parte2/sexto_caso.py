class sexto_caso():
    def __init__(self, minuscula, lista):
        self.muscula = minuscula
        self.lista = lista 

    def procesar(self):
        for palabras in self.lista:
            if palabras.startswith("py"):
             minuscula =palabras.lower()
             return minuscula