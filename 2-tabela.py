import sqlite3
#1- Conectando no DB

conexao = sqlite3.connect("titulo.db")

#Criando o cursor
cursor =conexao.cursor()

#Criando a Tabela
cursor.execute(
    """CREATE TABLE filmes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    ano INTEGER NOT NULL,
    nota REAL NOT NULL
    );

    """
)
#Fecha a conexão

conexao.close()
print("A tabela foi criada")

