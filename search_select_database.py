import mysql.connector
from mysql.connector import Error

try:
    # Conecta com o bd
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PASSCODE',
        database='DATABASENAME'
    )

    consulta_sql = "SELECT * FROM BANCOS"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os registros cadastrados")

    for linha in linhas:
        print("Código: ", linha[0])
        print("Nome", linha[1], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")

