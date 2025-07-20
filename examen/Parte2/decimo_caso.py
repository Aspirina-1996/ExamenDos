
class decimo_caso():
    def __init__(self, lista):
        self.lista = lista 

    def procesar(self):
        for palabras in self.lista:
           if "final" in palabras:
            return palabras.upper()
            