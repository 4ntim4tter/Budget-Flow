import sqlite3 as sql3

class DataManager():
    def __init__(self) -> None:
        self.db_link:sql3.Connection
        self.db_cursor:sql3.Cursor

    def db_connect(self, database):
        self.db_link = sql3.connect(database)

    def db_create_table(self, table:str, fields:list):
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}({fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, {fields[1]} STRING, {fields[2]} STRING, {fields[3]} STRING, {fields[4]} STRING, {fields[5]} STRING, {fields[6]} STRING)')
        self.db_disconnect()

    def db_insert_customer(self, table:str, customer:list):
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.executemany(f'INSERT INTO {table} (name, surname, phone, vehicle, plates, chasis) values (?,?,?,?,?,?)', customer)
        self.db_disconnect()

    def db_disconnect(self):
        self.db_cursor.close()