import sqlite3

# Conectando no BD
conexao = sqlite3.connect("titulo.db")
cursor =  conexao.cursor()

# 2 - Atualizando dados 
id = 1
cursor.execute(
    """
 UPDATE filmes SET nome = ?
 WHERE id = ?
    """,
    ("Homem Aranha",id)
)
conexao.commit()
print("Dados Atualizados com sucesso")