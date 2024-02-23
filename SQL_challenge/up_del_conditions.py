from db_connection import DatabaseManager

"""
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Use of functions to provide modularity and reuse of query scripting with conditionals
def update_client_balance(client_id, new_balance):
    """
    Update the balance of a specific client.

    Args:
        connection: SQLite database connection object.
        client_id: ID of the client to update.
        new_balance: New balance to set for the client.

    Returns:
        None
    """
    update_query = '''
        UPDATE clientes_test
        SET saldo = ?
        WHERE id = ?
    '''
    db_manager.execute_query(update_query, (new_balance, client_id))
    db_manager.commit_changes()
    print("Balance updated for client with ID", client_id)

def remove_client_by_id(client_id):
    """
    Remove a client by their ID.

    Args:
        connection: SQLite database connection object.
        client_id: ID of the client to remove.

    Returns:
        None
    """
    remove_query = 'DELETE FROM clientes_test WHERE id = ?'
    db_manager.execute_query(remove_query, (client_id,))
    db_manager.commit_changes()
    print("Client with ID", client_id, "removed")

# Resolution usage:

# a) Update the balance of a specific client
update_client_balance(client_id=3, new_balance=3000.50)

# b) Remove a client by their ID
remove_client_by_id(client_id=9)

# Close the connection
db_manager.close_connection()