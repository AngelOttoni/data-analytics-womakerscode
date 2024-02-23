from db_connection import connect_to_database, close_connection, execute_query, commit_changes

# Connect to the database
connection = connect_to_database()

# 4. Update and Removal
# a) Update the age of a specific student in the table
update_query = 'UPDATE alunos SET idade = ? WHERE id = ?'
new_age = 23
student_id_to_update = 1
execute_query(connection, update_query, (new_age, student_id_to_update))
commit_changes(connection)
print("\nUpdated age for student with ID", student_id_to_update, "to", new_age)

# b) Remove a student by their ID
remove_query = 'DELETE FROM alunos WHERE id = ?'
student_id_to_remove = 7
execute_query(connection, remove_query, (student_id_to_remove,))
commit_changes(connection)
print("Removed student with ID", student_id_to_remove)

# Close the connection
close_connection(connection)