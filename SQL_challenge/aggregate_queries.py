from db_connection import DatabaseManager

"""
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# a) Select the name and age of clients older than 30 years
query_a = '''
    SELECT nome, idade 
    FROM clientes 
    WHERE idade > 30
'''
cursor_a = db_manager.execute_query(query_a)
rows_a = cursor_a.fetchall()
print("\na) Name and age of clients older than 30 years:")
for row in rows_a:
    print(row)

# b) Calculate the average balance of clients
query_b = '''
    SELECT AVG(saldo) AS saldo_medio
    FROM clientes
'''
cursor_b = db_manager.execute_query(query_b)
saldo_medio = cursor_b.fetchone()[0]
print("\nb) Average balance of clients:", saldo_medio)

# c) Find the client with the maximum balance
query_c = '''
    SELECT nome
    FROM clientes
    WHERE saldo = (SELECT MAX(saldo) FROM clientes)
'''
cursor_c = db_manager.execute_query(query_c)
cliente_max_saldo = cursor_c.fetchone()[0]
print("\nc) Client with the maximum balance:", cliente_max_saldo)

# d) Count the number of clients with balance above 1000
query_d = '''
    SELECT COUNT(*) AS total_above_1000
    FROM clientes
    WHERE saldo > 1000
'''
cursor_d = db_manager.execute_query(query_d)
total_above_1000 = cursor_d.fetchone()[0]
print("\nd) Number of clients with balance above 1000:", total_above_1000)

# Close the connection
db_manager.close_connection()