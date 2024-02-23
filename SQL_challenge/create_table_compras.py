from db_connection import DatabaseManager

"""
8. Junção de Tabelas
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Create the "compras" table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS compras (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto VARCHAR(40),
        valor REAL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
'''
# Execute the query to create the table
db_manager.execute_query(create_table_query)

# Close the connection
db_manager.close_connection()