import mysql.connector
from mysql.connector import Error


# Atualizar registros em um banco de dados MySql

def conectar():
    try:
        # Conecta com o banco
        global con
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='PASSCODE',
            database='DATABASENAME'
        )
    except Error as e:
        print("Erro de conexão com o banco.", e)

def consulta(idProd):
    try:
        conectar()
        consulta_sql = 'SELECT * FROM funcionarios WHERE codigo = 1 '
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("Codigo: ", linha[0])
            print("Login: ", linha[1])
            print("Senha: ", linha[2])
    except Error as erro:
        print("Falha ao consultar a tabela: {}".format(erro))

def atualiza(declaracao):
    try:
        conectar()
        alteraa_preco = declaracao
        cursor = con.cursor()
        cursor.execute(alteraa_preco)
        con.commit()
        print("Preço alterado com sucesso!")
    except Error as erro:
        print("Falha ao inserir dados na tabela: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

if __name__ == '__main__':
    print("ATUALIZADOR DE INFORMAÇÕES")
    consulta(1)
    # print("\nEntre com o novo preço do produto:")
    # precoProd = input("Preço: ")
    textVal = "admin"
    declaracao = """UPDATE xTABELAx SET LOGIN = '""" + textVal + """' WHERE CODIGO = 1 """
    atualiza(declaracao)
    print(declaracao)