import mysql.connector
#Conexao com o Banco de Dados
"""
try:
    conexao = mysql.connector.Connect(host='localhost',database='univap',user='root',password='8tyTeDENtsxl0S2')
    if conexao.is_connected():
        informacaobanco = conexao.get_server_info()
        print(f"Conectado ao servidor banco de dados - Versao :{informacaobanco}")
        print('Conexao OK')
        comandosql = conexao.cursor()
        comandosql.execute('select database();')
        nomebanco = comandosql.fetchone()
        print(f"Banco de dados acessado: {nomebanco}")
    else:
        print(f"Conexao nao realizada com banco")
except Exception as erro:
    print(f'Erro: {erro}')
"""

#Cadastro no Banco de Dados
"""
try:
    conexao = mysql.connector.Connect(host='localhost',database='univap',user='root',password='8tyTeDENtsxl0S2')
    if conexao.is_connected():
        comandosql = conexao.cursor()
        cd = int(input("Codigo da disciplina: "))
        nd = input("Nome da disciplina: ")
        comandosql.execute(f'insert into disciplinas(codigodics,nomedisc) values({cd},"{nd}") ;')
        conexao.commit()
        print("Cadastro feito com sucesso ................!!!")
        comandosql.close()
        conexao.close()
except Exception as erro:
    print(f"Ocorreu erro: {erro}")
"""


#Consulta no Banco de Dados
"""
try:
    conexao = mysql.connector.Connect(host='localhost',database='univap',user='root',password='8tyTeDENtsxl0S2')
    if conexao.is_connected():
        comandosql = conexao.cursor()
        cd = int(input("Codigo da disciplina: "))
        comandosql.execute(f'select * from disciplinas where codigodics = {cd} ;')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f"Nome da disciplina: {registro[1]}")

        comandosql.close()
        conexao.close()
except Exception as erro:
    print(f"Ocorreu erro: {erro}")
"""
