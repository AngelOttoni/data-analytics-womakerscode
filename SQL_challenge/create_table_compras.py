from db_connection import connect_to_database, execute_query, close_connection

# Connect to the database
connection = connect_to_database()

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
execute_query(connection, create_table_query)

# Close the connection
close_connection(connection)