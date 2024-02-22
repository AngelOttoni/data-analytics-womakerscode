from db_connection import connect_to_database, close_connection, execute_query

# Connect to the database
connection = connect_to_database()

# a) Select all records from the "alunos" table
query_a = 'SELECT * FROM alunos'
cursor_a = execute_query(connection, query_a)
rows_a = cursor_a.fetchall()
print("\na) All records from the 'alunos' table:")
for row in rows_a:
    print(row)
    
# b) Select the name and age of students older than 20 years
query_b = 'SELECT nome, idade FROM alunos WHERE idade > 20'
cursor_b = execute_query(connection, query_b)
rows_b = cursor_b.fetchall()
print("\nb) Name and age of students older than 20 years:")
for row in rows_b:
    print(row)

# c) Select students from the "Engenharia" course in alphabetical order
query_c = "SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome"
cursor_c = execute_query(connection, query_c)
rows_c = cursor_c.fetchall()

if rows_c:
    print("\nc) Students from the Engineering course in alphabetical order:")
    for row in rows_c:
        print(row)
else:
    print("\nc) No students enrolled in the Engineering course.")
    
# Close the connection
close_connection(connection)