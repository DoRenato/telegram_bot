import sqlite3


def criar_bd(nome_bd):
    db = sqlite3.connect(nome_bd)
    return db

def criar_tabela(db, nome_tabela, tipo='lista_compras'):
    cursor = db.cursor()
    # Criar uma tabela
    if tipo=='lista_compras':
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS lista_{nome_tabela} (
            id INTEGER PRIMARY KEY,
            produto TEXT UNIQUE NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
        ''')
        db.commit()


def produto_existente(db, nome_tabela, nome_produto):
    """Verifica se um usuário com o nome especificado já existe na tabela users."""
    cursor = db.cursor()
    cursor.execute(f'''
    SELECT 1 FROM lista_{nome_tabela} WHERE produto = ?
    ''', (nome_produto,))
    result = cursor.fetchone()
    # Retorna True ou False
    return result is not None

def editar_produto(db, nome_tabela, produto, preco, quantidade):
    cursor = db.cursor()
    cursor.execute(f'''
    UPDATE lista_{nome_tabela} SET preco = ?, quantidade = ? WHERE produto = ?
    ''', (preco, quantidade, produto))
    db.commit()
    return db

def adicionar_produto(db, nome_tabela, produto, preco=0, quantidade=1):
    cursor = db.cursor()
    # Inserir dados na tabela
    produto_existe=produto_existente(db, nome_tabela, produto)
    if produto_existe:
        editar_produto(db, nome_tabela, produto, preco, quantidade)
    else:
        cursor.execute(f'''
        INSERT INTO lista_{nome_tabela} (produto, preco, quantidade) VALUES (?, ?, ?)
        ''', (produto, preco, quantidade))
    # Salvar (commit) as alterações
    db.commit()
    return db

def excluir_produto(db, nome_tabela, produto):
    cursor = db.cursor()
    cursor.execute(f'''
    DELETE FROM lista_{nome_tabela} WHERE produto = ?
    ''', (produto,))
    db.commit()
    return db

def ver_tabela(db, nome_tabela):
    cursor = db.cursor()
    # Consultar dados
    cursor.execute(f'SELECT * FROM lista_{nome_tabela}')
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# # Salvar (commit) as alterações
# conn.commit()

# # Excluir dados
# cursor.execute('''
# DELETE FROM users WHERE name = ?
# ''', ('John Doe',))

# # Salvar (commit) as alterações
# conn.commit()

# # Fechar a conexão
# conn.close()

def list_tables(conn):
    """Lista todas as tabelas no banco de dados."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])


if __name__ == '__main__':
    banco=criar_bd('lista_compras')
    nova_tabela=criar_tabela(banco, 'lista1')
    novo_produto1=adicionar_produto(banco, 'lista1', 'arroz')
    ver_tabela(banco, 'lista1')
    list_tables(banco)
    #Encerrar conexão com bd
    banco.close()