from db_connection import DatabaseManager

"""
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# a) Select all records from the "alunos" table
query_a = 'SELECT * FROM alunos'
cursor_a = db_manager.execute_query(query_a)
rows_a = cursor_a.fetchall()
print("\na) All records from the 'alunos' table:")
for row in rows_a:
    print(row)
    
# b) Select the name and age of students older than 20 years
query_b = 'SELECT nome, idade FROM alunos WHERE idade > 20'
cursor_b = db_manager.execute_query(query_b)
rows_b = cursor_b.fetchall()
print("\nb) Name and age of students older than 20 years:")
for row in rows_b:
    print(row)

# c) Select students from the "Engenharia" course in alphabetical order
query_c = "SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome"
cursor_c = db_manager.execute_query(query_c)
rows_c = cursor_c.fetchall()

if rows_c:
    print("\nc) Students from the Engineering course in alphabetical order:")
    for row in rows_c:
        print(row)
else:
    print("\nc) No students enrolled in the Engineering course.")
    
# Close the connection
db_manager.close_connection()