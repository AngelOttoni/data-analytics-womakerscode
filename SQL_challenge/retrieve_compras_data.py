from db_connection import DatabaseManager

"""
8. Junção de Tabelas
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

def retrieve_compras_data():
    """
    Retrieve data from the "compras" table.

    Returns:
        None
    """
    query = '''
        SELECT clientes.nome, compras.produto, compras.valor
        FROM compras
        INNER JOIN clientes ON compras.cliente_id = clientes.id
    '''
    cursor = db_manager.execute_query(query)
    rows = cursor.fetchall()

    print("Client Name | Product | Value")
    for row in rows:
        print(row)

# Resolution usage:
# Retrieve data from the "compras" table
retrieve_compras_data()

# Close the connection
db_manager.close_connection()