import pyodbc 
from modelo.Palabras import Palabras


def main():

    conn = pyodbc.connect(
         "DRIVER={ODBC Driver 17 for SQL Server};"
         "SERVER=ASPIRINA\SQLEXPRESS;"
         "DATABASE=Examen2;"
         "Trusted_Connection=yes"
    ) 
    cursor = conn.cursor() 
    lista = []
    resultados = []
    cursor.execute("SELECT * FROM Palabras")
    for fila in cursor:
        palabra_por_guardar = Palabras(fila[0],fila[1],fila[2])
        lista.append(palabra_por_guardar)
    for palabra in lista:
        texto = palabra.get_texto()
        #primer caso
        if "Gato" in texto:
            texto = texto.strip()
            palabra.set_texto(texto)
            resultados.append(palabra)
        #segundo caso
        if "python" in texto:
            texto = texto.upper()
            palabra.set_texto(texto)
            resultados.append(palabra)
        #tercer caso
        if texto.isdigit():
            resultados.append(palabra)


    for palabra in resultados:
        print(palabra.get_texto())
    




        

if __name__ == "__main__":
    main()

    