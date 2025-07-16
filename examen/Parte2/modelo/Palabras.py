

class Palabras :

    def __init__(self, id, texto, grupo_id):
        self.id= id
        self.texto = texto
        self.grupo_id = grupo_id

    def get_texto(self):
        return self.texto
    
    def set_texto(self,texto):
        self.texto = texto
      
