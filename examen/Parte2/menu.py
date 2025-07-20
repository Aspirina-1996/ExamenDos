import pyodbc 
from primer_caso import primer_caso
from segundo_caso import segundo_caso 
from tercer_caso import tercer_caso
from cuarto_caso import cuarto_caso
from quinto_caso import quinto_caso
from sexto_caso import sexto_caso
from setimo_caso import setimo_caso
from octavo_caso import octavo_caso
from noveno_caso import noveno_caso
from decimo_caso import decimo_caso


def main():
    conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=ASPIRINA\\SQLEXPRESS;"
            "DATABASE=Examen2;"
            "Trusted_Connection=yes"
    ) 
    cursor = conn.cursor() 
    lista = []
    cursor.execute("SELECT * FROM Palabras")
    for fila in cursor:
        palabra_por_guardar = fila[1]
        lista.append(palabra_por_guardar)
    return lista

#menu de opciones 

def menu(lista): 
    while True:
        print("ACERTIJOS DE EXAMEN DOS")
        print("son 10 acertijos, digite un numero del 1 al 0")
        seleccion = int(input("Digite el caso que desea ejecutar:  "))
        if seleccion == 1:
            caso1 = primer_caso("Gato", lista)
            print(caso1.procesar())
        elif seleccion == 2:
            caso2 = segundo_caso("python", lista)
            print(caso2.procesar())
        elif seleccion == 3:
            caso3= tercer_caso("123", lista)
            print(caso3.procesar())
        elif seleccion == 4:
            caso4 = cuarto_caso("agua", lista)
            print(caso4.procesar())
        elif seleccion == 5:
            caso5 = quinto_caso(lista) 
            print(caso5.procesar())
        elif seleccion == 6:
            caso6 = sexto_caso("minuscula", lista)
            print(caso6.procesar())
        elif seleccion == 7:
            caso7 = setimo_caso(lista)
            print(caso7.procesar())
        elif seleccion == 8:  
            caso8 = octavo_caso(lista)
            print(caso8.procesar())
        elif seleccion == 9:
            caso9 = noveno_caso(lista)
            print(caso9.procesar())
        elif seleccion == 0:
            caso0 = decimo_caso(lista)
            print(caso0.procesar())


        """#llamando al caso 
    caso1 = primer_caso("Gato", lista)
    print(caso1.procesar())

    caso2= segundo_caso("python", lista)
    print(caso2.procesar())

    caso3= tercer_caso("123", lista)
    print(caso3.procesar())

    caso4 = cuarto_caso("agua", lista)
    print(caso4.procesar())

    caso5 = quinto_caso(lista) 
    print(caso5.procesar())

    caso6 = sexto_caso("minuscula", lista)
    print(caso6.procesar())

    caso7 = setimo_caso(lista)
    print(caso7.procesar())

    caso8 = octavo_caso(lista)
    print(caso8.procesar())

    caso9 = noveno_caso(lista)
    print(caso9.procesar())
    
    caso0 = decimo_caso(lista)
    print(caso0.procesar())"""
 
        


if __name__ == "__main__":
    resultados = main() 
    menu(resultados)