import sqlite3 as sql3

class DataManager():
    def __init__(self) -> None:
        self.db_link:sql3.Connection
        self.db_cursor:sql3.Cursor

    def db_connection(self, database):
        self.db_link = sql3.connect(database)
        self.db_cursor = self.db_link.cursor()

    def db_create_table(self, table:str, fields:list):
        self.db_cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}({fields[0]}, {fields[1]}, {fields[2]}, {fields[3]}, {fields[4]}, {fields[5]})')