import sqlite3
# Importa o módulo sqlite3 para trabalhar com o banco de dados SQLite

def initialize_database():
    # Define a função initialize_database para inicializar o banco de dados
    conn = sqlite3.connect('banco.db')
    # Conecta ao banco de dados SQLite (cria o banco se não existir)
    cursor = conn.cursor()
    # Cria um cursor para interagir com o banco de dados
    
    # Criar tabela de clientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        cpf TEXT NOT NULL UNIQUE,
                        endereco TEXT NOT NULL
                      )''')
    # Executa uma consulta SQL para criar a tabela de clientes, se ela não existir
    # A tabela clientes possui as colunas: id, nome, data_nascimento, cpf e endereco
    # A coluna id é a chave primária e autoincrementada
    # A coluna cpf é única
    
    # Criar tabela de contas
    cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero INTEGER NOT NULL,
                        agencia TEXT NOT NULL,
                        saldo REAL NOT NULL,
                        limite REAL NOT NULL,
                        limite_saques INTEGER NOT NULL,
                        cliente_id INTEGER NOT NULL,
                        FOREIGN KEY(cliente_id) REFERENCES clientes(id),
                        UNIQUE(numero, agencia)
                      )''')
    # Executa uma consulta SQL para criar a tabela de contas, se ela não existir
    # A tabela contas possui as colunas: id, numero, agencia, saldo, limite, limite_saques e cliente_id
    # A coluna id é a chave primária e autoincrementada
    # A coluna cliente_id é uma chave estrangeira que referencia a coluna id da tabela clientes
    # A combinação das colunas numero e agencia deve ser única
    
    # Criar tabela de transações
    cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT NOT NULL,
                        valor REAL NOT NULL,
                        data TEXT NOT NULL,
                        conta_id INTEGER NOT NULL,
                        FOREIGN KEY(conta_id) REFERENCES contas(id)
                      )''')
    # Executa uma consulta SQL para criar a tabela de transações, se ela não existir
    # A tabela transacoes possui as colunas: id, tipo, valor, data e conta_id
    # A coluna id é a chave primária e autoincrementada
    # A coluna conta_id é uma chave estrangeira que referencia a coluna id da tabela contas
    
    conn.commit()
    # Confirma as alterações no banco de dados
    conn.close()
    # Fecha a conexão com o banco de dados

initialize_database()
# Chama a função initialize_database para inicializar o banco de dados
