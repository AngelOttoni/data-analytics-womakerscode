from db_connection import connect_to_database, close_connection, execute_query

# Connect to the database
connection = connect_to_database()

# a) Select the name and age of clients older than 30 years
query_a = '''
    SELECT nome, idade 
    FROM clientes 
    WHERE idade > 30
'''
cursor_a = execute_query(connection, query_a)
rows_a = cursor_a.fetchall()
print("\na) Name and age of clients older than 30 years:")
for row in rows_a:
    print(row)

# b) Calculate the average balance of clients
query_b = '''
    SELECT AVG(saldo) AS saldo_medio
    FROM clientes
'''
cursor_b = execute_query(connection, query_b)
saldo_medio = cursor_b.fetchone()[0]
print("\nb) Average balance of clients:", saldo_medio)

# c) Find the client with the maximum balance
query_c = '''
    SELECT nome
    FROM clientes
    WHERE saldo = (SELECT MAX(saldo) FROM clientes)
'''
cursor_c = execute_query(connection, query_c)
cliente_max_saldo = cursor_c.fetchone()[0]
print("\nc) Client with the maximum balance:", cliente_max_saldo)

# d) Count the number of clients with balance above 1000
query_d = '''
    SELECT COUNT(*) AS total_above_1000
    FROM clientes
    WHERE saldo > 1000
'''
cursor_d = execute_query(connection, query_d)
total_above_1000 = cursor_d.fetchone()[0]
print("\nd) Number of clients with balance above 1000:", total_above_1000)

# Close the connection
close_connection(connection)