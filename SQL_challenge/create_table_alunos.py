from db_connection import connect_to_database, close_connection, execute_query

# Connect to the database
connection = connect_to_database()

# Define the query to create the "alunos" table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS alunos_teste (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        idade INTEGER,
        curso VARCHAR(30)
    )
'''

# Execute the query to create the table
execute_query(connection, create_table_query)

# Close the connection
close_connection(connection)
