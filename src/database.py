import sqlite3
import os.path
import datetime

class Database:
    
    def __init__(self, dbname = None) -> None:
        self.dbname = 'db.db' if not dbname else dbname
                
        if not os.path.exists('./data'):
            os.makedirs('./data') 
        self.create_connection()

    def create_connection(self) -> None:
        try:
            self.connection = sqlite3.connect(f'./data/{self.dbname}')
            self.cursor = self.connection.cursor()
            self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS TICKER (
                    date DATETIME NOT NULL PRIMARY KEY,
                    open REAL NOT NULL,
                    high REAL NOT NULL,
                    low REAL NOT NULL,
                    close REAL NOT NULL)  
                    """)
            self.connection.commit()
        except Exception as e:
            print(f"Error creating connection to database: {e}")
    
    def close_connection(self) -> None:
        self.cursor.close()
    
    def add_row(self, date: datetime.date, open: float, high: float, low: float, close: float) -> None:
        try:
            self.cursor.execute("""
                INSERT INTO TICKER (date, open, high, low, close)
                VALUES (?, ?, ?, ?, ?)
                """, (date, open, high, low, close))
        except Exception as e:
            print(f"Error adding row to table: {e}")
        self.connection.commit()

    def delete_row(self, date: datetime.date):
        try:
            date_str = date.strftime('%Y-%m-%d')
            self.cursor.execute("""
            DELETE FROM TICKER WHERE date = ?          
            """, (date_str,))
        except Exception as e:
            print(f"Error deleting row from table: {e} ")
        self.connection.commit()

    def update_row(self, date: datetime, open: float, high: float, low: float, close: float) -> None:
        pass

    def __del__(self):
        self.close_connection()





