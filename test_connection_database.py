import mysql.connector

# Conecta com o bd
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='PASSCODE',
    database='DATABASENAME'
)

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MYSQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão com o MySQL foi encerrada")


