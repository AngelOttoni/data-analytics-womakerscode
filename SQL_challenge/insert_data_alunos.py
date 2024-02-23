from db_connection import DatabaseManager

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Define the records to insert
alunos_data = [
    (1, 'Alice Moreira', 22, 'Ciência da Computação'),
    (2, 'Bob Marlley', 21, 'Matemática'),
    (3, 'Charlie Brown', 23, 'Física'),
    (4, 'David Silva', 20, 'Química'),
    (5, 'Eve Lima', 24, 'Biologia'),
    (6, 'Fernanda Santos', 25, 'Engenharia Civil'),
    (7, 'Gabriel Pereira', 22, 'Administração'),
    (8, 'Heloísa Oliveira', 21, 'Economia'),
    (9, 'Igor Sousa', 23, 'Direito'),
    (10, 'Juliana Costa', 24, 'Psicologia')
]

# Define the query to insert records
insert_query = '''
    INSERT INTO alunos (id, nome, idade, curso)
    VALUES (?, ?, ?, ?)
'''

# Execute the query for each student
db_manager.execute_query_sequence(insert_query, alunos_data)

# Commit the transaction
db_manager.commit_changes()

# Close the connection
db_manager.close_connection()