

import pandas as pd
import pyodbc

def busqueda(df, palabra):
     matriz = df.values.tolist()
     fila = len(matriz)
     col = len(matriz[0])
    # Buscar horizontalmente (izquierda a derecha)
     for i in range(fila):
        fila_str = ''.join(matriz[i])
        if palabra in fila_str:
            pos = fila_str.find(palabra)
            return i, pos
    
    # Buscar horizontalmente (derecha a izquierda)
     for i in range(fila):
        fila_str = ''.join(matriz[i][::-1])
        if palabra in fila_str:
            pos = fila_str.find(palabra)
            return i, col-1-pos
    
    # Buscar verticalmente (arriba a abajo)
     for j in range(col):
        columna_str = ''.join([matriz[i][j] for i in range(fila)])
        if palabra in columna_str:
            pos = columna_str.find(palabra)
            return pos, j
    
    # Buscar verticalmente (abajo a arriba)
     for j in range(col):
        columna_str = ''.join([matriz[i][j] for i in range(fila-1, -1, -1)])
        if palabra in columna_str:
            pos = columna_str.find(palabra)
            return fila-1-pos, j
    
     return None
   
def main():
    try:
        palabras_por_buscar = ["letra","luz","reto","clase","radar","python"]
        df = pd.read_excel('Examen2.xlsx',
                   sheet_name="Sopa",
                   engine='openpyxl',
                   skiprows=4,
                   usecols='E:N',
                   nrows=10,
                   )
        for palabra in palabras_por_buscar:
         print(busqueda(df,palabra),' ',palabra)

     
      #print (df["Examen2.xlsx"].head)
        return df.head(20)
    except ValueError as ex:
     print (f"error al leer archivo de excel {ex}")
     

if __name__ == '__main__':
    main( )

