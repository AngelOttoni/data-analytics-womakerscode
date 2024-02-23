from db_connection import DatabaseManager

"""
5. Criar uma Tabela e Inserir Dados
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Create the "clientes" table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        idade INTEGER,
        saldo REAL
        
    )
'''
# Execute the query to create the table
db_manager.execute_query(create_table_query)

# Close the connection
db_manager.close_connection()