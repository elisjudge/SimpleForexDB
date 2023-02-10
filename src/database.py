import sqlite3
import os.path
import sys

class Database:
    
    def __init__(self) -> None:
        self.dbname = 'db.db'
        if not os.path.exists(f'./data/{self.dbname}'):
            self.create_database()


    def create_database(self):
        connection = sqlite3.connect(f'./data/{self.dbname}')
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AUDJPY (
        date NOT NULL PRIMARY KEY,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL)  
        """)

        connection.commit()
        cursor.close()


print(sys.path)
