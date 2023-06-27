from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget
from popup_module import PopupModule

import sqlite3 as sql3


class DataManager:
    def __init__(self, database:str) -> None:
        self.db_link: sql3.Connection
        self.db_cursor: sql3.Cursor
        self.database = database
        self.popup_module = PopupModule(
            "Yes", "No", "Unos Mušterije", "Da li želite unijeti mušteriju?"
        )

    def db_connect(self, database):
        self.database = database
        self.db_link = sql3.connect(database)

    def db_disconnect(self):
        self.db_link.commit()
        self.db_link.close()

    def db_create_table(self, table: str, fields: list):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table}({fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, {fields[1]} STRING, {fields[2]} STRING, {fields[3]} STRING, {fields[4]} STRING, {fields[5]} STRING, {fields[6]} STRING)"
        )
        self.db_disconnect()

    def db_insert_customer(self, table: str, customer: list, entry_widget:QWidget, popup_window:QWidget):
        answer = self.popup_module.confirmation_dialog(popup_window)
        if answer:
            self.db_connect(self.database)
            self.db_cursor = self.db_link.cursor()
            self.db_cursor.execute(
                f"INSERT INTO {table} (name, surname, phone, vehicle, plates, chasis) values (?,?,?,?,?,?)",
                customer,
            )
            self.db_disconnect()
            return True


    def populate_customer_table(self, table: str, table_widget: QTableWidget):
        self.clear_customer_table(table_widget)
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(f"SELECT * FROM {table}")
        rows = self.db_cursor.fetchall()
        selected_row = 0
        for row in rows:
            table_widget.setItem(selected_row, 0, QTableWidgetItem(row[1]))
            table_widget.setItem(selected_row, 1, QTableWidgetItem(row[2]))
            table_widget.setItem(selected_row, 2, QTableWidgetItem(row[3]))
            table_widget.setItem(selected_row, 3, QTableWidgetItem(row[4]))
            selected_row += 1
            table_widget.insertRow(selected_row)
        self.db_disconnect()

    def clear_customer_table(self, table_widget: QTableWidget):
        # table_widget.clear()
        for i in range(table_widget.rowCount(), 0, -1):
            table_widget.removeRow(i)
        table_widget.setItem(0, 0, QTableWidgetItem(""))
        table_widget.setItem(0, 1, QTableWidgetItem(""))
        table_widget.setItem(0, 2, QTableWidgetItem(""))
        table_widget.setItem(0, 3, QTableWidgetItem(""))
