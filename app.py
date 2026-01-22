import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()

def cadastrar_cliente(nome, email):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

# Execução principal
while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        cadastrar_cliente(nome, email)
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        break
    else:
        print("Opção inválida")

conn.close()

