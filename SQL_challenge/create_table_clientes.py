from db_connection import connect_to_database, execute_query, close_connection

# Connect to the database
connection = connect_to_database()

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
execute_query(connection, create_table_query)

# Close the connection
close_connection(connection)