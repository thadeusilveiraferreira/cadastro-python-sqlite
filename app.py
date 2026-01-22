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
    if "@" not in email:
        print("Email inválido!")
        return

    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)",
        (nome, email)
    )
    conn.commit()
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")


def atualizar_cliente(id_cliente, novo_nome, novo_email):
    cursor.execute(
        "UPDATE clientes SET nome = ?, email = ? WHERE id = ?",
        (novo_nome, novo_email, id_cliente)
    )
    conn.commit()
    print("Cliente atualizado com sucesso!")


def excluir_cliente(id_cliente):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    print("Cliente excluído com sucesso!")


# Execução principal
while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        cadastrar_cliente(nome, email)

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        id_cliente = input("ID do cliente a atualizar: ")
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo email: ")
        atualizar_cliente(id_cliente, novo_nome, novo_email)

    elif opcao == "4":
        id_cliente = input("ID do cliente a excluir: ")
        excluir_cliente(id_cliente)

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")

conn.close()

