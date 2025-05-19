import sqlite3

# 1- Conectar no BD
def conect_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2-inserir dados 

def insere_dados(nome , ano ,nota):
    conexao = conect_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
       INSERT INTO filmes (nome , ano , nota)
       VALUES(?,?,?)
        """, (nome , ano,nota)
    )
    conexao.commit()
    conexao.close()

    #3 Listagem de dados

def obter_dados():
    conexao = conect_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados =cursor.fetchall()
    cursor.close()
    return dados