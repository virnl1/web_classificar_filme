import sqlite3

#Conectando no BD

conexao =  sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#Deletando os dados

id = 1,2
cursor.execute(
    """
 DELETE FROM filmes
 WHERE ID in (?,?)
    """,
    id
)
conexao.commit()
print("Dados deletados com sucesso")
