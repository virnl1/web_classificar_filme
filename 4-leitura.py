import sqlite3
 
 #conexão no DB.
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

# Leitura de dados
dados = cursor.execute (" SELECT * FROM filmes")

print(dados.fetchall())