class tercer_caso():
    def __init__(self, digito, lista):
        self.digito  = digito
        self.lista = lista

    def procesar(self):
        for palabras in self.lista:
            if palabras.isdigit():
                return palabras
                