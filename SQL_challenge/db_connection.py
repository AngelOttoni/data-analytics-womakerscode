import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Connection to the database successful!")
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, parameters=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, parameters)
            print("Query executed successfully!")
            return cursor
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return None

    def execute_query_sequence(self, query, parameters):
        """
        Execute a command sequence on the database.

        Args:
            query: SQL command to execute.
            parameters: List of parameters to be used in the command.

        Returns:
            None
        """
        cursor = self.connection.cursor()
        try:
            cursor.executemany(query, parameters)
        except Exception as error:
            print('Error executing command:', error,)
        finally:
            print('Query executed successfully!')

    def commit_changes(self):
        if self.connection:
            self.connection.commit()
            print("Changes committed successfully!")