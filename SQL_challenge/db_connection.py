import sqlite3

db_path = './database.db'

def connect_to_database():
    try:
        connection = sqlite3.connect(db_path)
        print("Connection to the database successful!")
        return connection
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed.")

def execute_query(connection, query, parameters=()):
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        print("Query executed successfully!")
        return cursor
    except sqlite3.Error as e:
        print("Error executing query:", e)
        return None

def execute_query_sequence(connection, query, parameters):
    """
    Execute a command sequence on the database.

    Args:
        connection: SQLite database connection object.
        command: SQL command to execute.
        parameters: List of parameters to be used in the command.

    Returns:
        None
    """
    cursor = connection.cursor()
    try:
        cursor.executemany(query, parameters)
    except Exception as error:
        print('\n----- Error executing command:', error, ' -----')
    finally:
        print('\n----- Query executed successfully! -----')


def commit_changes(connection):
    if connection:
        connection.commit()
        # TO-DO Ajustar essa mensagem
        print("Records Saved!")