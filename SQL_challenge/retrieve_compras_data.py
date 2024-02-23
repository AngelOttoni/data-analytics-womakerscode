from db_connection import connect_to_database, close_connection, execute_query

def retrieve_compras_data(connection):
    """
    Retrieve data from the "compras" table.

    Args:
        connection: SQLite database connection object.

    Returns:
        None
    """
    query = '''
        SELECT clientes.nome, compras.produto, compras.valor
        FROM compras
        INNER JOIN clientes ON compras.cliente_id = clientes.id
    '''
    cursor = execute_query(connection, query)
    rows = cursor.fetchall()

    print("Client Name | Product | Value")
    for row in rows:
        print(row)

# Resolution usage:

# Connect to the database
connection = connect_to_database()

# Retrieve data from the "compras" table
retrieve_compras_data(connection)

# Close the connection
close_connection(connection)