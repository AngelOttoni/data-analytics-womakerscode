from db_connection import DatabaseManager

"""
8. Junção de Tabelas
"""

# Create an instance of DatabaseManager
db_manager = DatabaseManager(db_path='./database.db')

# Connect to the database
db_manager.connect()

# Define the records to insert into the "clientes" table
compras_data = [
    (1, 'Laptop', 1200.00),
    (2, 'Smartphone', 800.00),
    (3, 'Tablet', 300.00),
    (4, 'Smartwatch', 250.00),
    (5, 'Headphones', 100.00),
    (6, 'Wireless Earbuds', 150.00),
    (7, 'Gaming Console', 400.00),
    (8, 'VR Headset', 300.00),
    (9, '4K TV', 1000.00),
    (10, 'Home Theater System', 500.00),
    (11, 'Digital Camera', 600.00),
    (12, 'Drone', 700.00),
    (13, 'Fitness Tracker', 150.00),
    (14, 'External Hard Drive', 80.00),
    (15, 'Robot Vacuum Cleaner', 250.00)
]

# Define the query to insert records into the "compras" table
insert_query = '''
    INSERT INTO compras (cliente_id, produto, valor)
    VALUES (?, ?, ?)
'''

# Call the function to insert client records
db_manager.execute_query_sequence(insert_query, compras_data)

# Commit the transaction
db_manager.commit_changes()

# Close the connection
db_manager.close_connection()