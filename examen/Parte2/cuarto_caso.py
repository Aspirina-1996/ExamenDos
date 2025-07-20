class cuarto_caso():
    def __init__(self,frase , lista):
        self.frase  = frase
        self.lista = lista

    def procesar(self):
        for palabras in self.lista:
         if "agua" in palabras:
           frase = palabras.split()
           return frase[0]