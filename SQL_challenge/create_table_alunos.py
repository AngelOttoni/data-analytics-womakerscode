from db_connection import DatabaseManager

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Define the query to create the "alunos" table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        idade INTEGER,
        curso VARCHAR(30)
    )
'''

# Execute the query to create the table
db_manager.execute_query(create_table_query)

# Close the connection
db_manager.close_connection()