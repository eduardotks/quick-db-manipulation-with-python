import mysql.connector
from mysql.connector import Error

# Inserir registros em um banco de dados MySql

try:
    # Conecta com o bd
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PASSCODE',
        database='DATABASENAME'
    )

    inserir_produtos = """INSERT INTO status_art
                            (CODIGO, DESCRICAO) 
                            VALUE 
                            (6, 'TESTE')
                        """
    print(inserir_produtos)
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "Registros inseridos na tabela!")
    cursor.close()
except Error as erro:
    print("Erro ao acessar tabela MySQL: {}".format(erro))
finally:
    if con.is_connected():
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada\n")
