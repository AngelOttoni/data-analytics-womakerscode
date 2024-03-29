from db_connection import DatabaseManager

"""
5. Criar uma Tabela e Inserir Dados
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Define the records to insert into the "clientes" table
clientes_data = [
    (1, 'Alice Silva', 30, 1000.50),
    (2, 'Bob Santos', 25, 1500.75),
    (3, 'Charlie Oliveira', 35, 2000.00),
    (4, 'David Costa', 40, 1800.25),
    (5, 'Eve Pereira', 28, 2200.80),
    (6, 'Fernanda Martins', 33, 1350.60),
    (7, 'Gabriel Almeida', 29, 1900.45),
    (8, 'Heloísa Ribeiro', 37, 1675.90),
    (9, 'Igor Lima', 42, 2100.35),
    (10, 'Juliana Ferreira', 26, 1850.70),
    (11, 'Karina Castro', 31, 1550.25),
    (12, 'Lucas Mendes', 36, 2300.80),
    (13, 'Mariana Carvalho', 27, 1750.95),
    (14, 'Nathan Sousa', 34, 2000.50),
    (15, 'Olivia Barbosa', 38, 2450.30)
]

# Define the query to insert records into the "clientes" table
insert_query = '''
    INSERT INTO clientes (id, nome, idade, saldo)
    VALUES (?, ?, ?, ?)
'''

# Call the function to insert client records
db_manager.execute_query_sequence(insert_query, clientes_data)

# Commit the transaction
db_manager.commit_changes()

# Close the connection
db_manager.close_connection()