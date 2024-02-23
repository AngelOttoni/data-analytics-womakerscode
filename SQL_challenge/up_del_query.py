from db_connection import DatabaseManager

"""
4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# a) Update the age of a specific student in the table
update_query = 'UPDATE alunos_new_test SET idade = ? WHERE id = ?'
new_age = 23
student_id_to_update = 1
db_manager.execute_query(update_query, (new_age, student_id_to_update))
db_manager.commit_changes()
print("\nUpdated age for student with ID", student_id_to_update, "to", new_age)

# b) Remove a student by their ID
remove_query = 'DELETE FROM alunos_new_test WHERE id = ?'
student_id_to_remove = 7
db_manager.execute_query(remove_query, (student_id_to_remove,))
db_manager.commit_changes()
print("Removed student with ID", student_id_to_remove)

# Close the connection
db_manager.close_connection()