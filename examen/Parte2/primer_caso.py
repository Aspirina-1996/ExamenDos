class primer_caso():
    def __init__(self, animal,lista):
        self.animal= animal 
        self.lista= lista

    def procesar(self):
        for palabra in self.lista:
            if self.animal in palabra:
                return palabra.strip()
         
        
    
    #def set_texto(self,texto):
     #   self.texto = texto
      #  print(self.texto)