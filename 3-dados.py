import sqlite3

#Conectando no BD

conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#Inserindo os Dados

cursor.execute(

"""

INSERT INTO filmes (nome, ano,nota)
VALUES ('TITANIC', 2005,7)
 
 """
)
conexao.commit()
conexao.close()
print("Dados inseridos com sucesso")