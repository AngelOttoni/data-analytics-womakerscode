from db_connection import connect_to_database, close_connection, execute_query, commit_changes

# Use of functions to provide modularity and reuse of query scripting with conditionals
def update_client_balance(connection, client_id, new_balance):
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
        UPDATE clientes
        SET saldo = ?
        WHERE id = ?
    '''
    execute_query(connection, update_query, (new_balance, client_id))
    commit_changes(connection)
    print("Balance updated for client with ID", client_id)

def remove_client_by_id(connection, client_id):
    """
    Remove a client by their ID.

    Args:
        connection: SQLite database connection object.
        client_id: ID of the client to remove.

    Returns:
        None
    """
    remove_query = 'DELETE FROM clientes WHERE id = ?'
    execute_query(connection, remove_query, (client_id,))
    commit_changes(connection)
    print("Client with ID", client_id, "removed")

# Example usage:
# Connect to the database
connection = connect_to_database()

# a) Update the balance of a specific client
update_client_balance(connection, client_id=3, new_balance=3000.50)

# b) Remove a client by their ID
remove_client_by_id(connection, client_id=9)

# Close the connection
close_connection(connection)