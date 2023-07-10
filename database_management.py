from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget
from popup_module import PopupModule

import sqlite3 as sql3


class DataManager:
    def __init__(self, database: str) -> None:
        self.db_link: sql3.Connection
        self.db_cursor: sql3.Cursor
        self.database = database
        self.popup_module = PopupModule("Yes", "No", "", "")

    def db_connect(self, database):
        """Connect to database -> Sqlite3

        Args:
            database (string): database table to connect to
        """
        self.database = database
        self.db_link = sql3.connect(database)

    def db_disconnect(self):
        self.db_link.commit()
        self.db_link.close()

    def db_create_table(self, table: str, fields: list):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        if table == "customers":
            self.db_cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table}({fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, {fields[1]} STRING, {fields[2]} STRING, {fields[3]} STRING, {fields[4]} STRING, {fields[5]} STRING, {fields[6]} STRING)"
            )
        if table == "receipts":
            self.db_cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {table}(
                    {fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, 
                    {fields[1]} INTEGER,
                    {fields[2]} STRING, 
                    {fields[3]} STRING, 
                    {fields[4]} FLOAT, 
                    {fields[5]} INTEGER, 
                    {fields[6]} FLOAT,
                    {fields[7]} FLOAT,
                    {fields[8]} FLOAT,
                    FOREIGN KEY ({fields[1]}) REFERENCES customers (id))
"""
            )
        self.db_disconnect()

    def db_insert_customer(self, table: str, customer: list):
        self.popup_module.set_title("Unos")
        self.popup_module.set_question("Da li želite spremiti unesene podatke?")
        answer = self.popup_module.confirmation_dialog()
        if answer:
            self.db_connect(self.database)
            self.db_cursor = self.db_link.cursor()
            self.db_cursor.execute(
                f"INSERT INTO {table} (name, surname, phone, vehicle, plates, chasis) values (?,?,?,?,?,?)",
                customer,
            )
            self.db_disconnect()
            return True

    def db_customer_interaction(
        self, table, table_widget: QTableWidget, search_params: tuple, query_string: str
    ):
        self.clear_customer_table(table_widget)
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        if search_params == () or query_string == "" or query_string == "WH":
            self.db_cursor.execute(f"SELECT * FROM {table}")
        else:
            self.db_cursor.execute(
                f"SELECT * FROM {table} {query_string}",
                search_params,
            )
        rows = self.db_cursor.fetchall()
        self.db_disconnect()
        return rows

    def veiw_selected_customer(self, table, id: tuple):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        if id != "" and id is not None:
            self.db_cursor.execute(f"SELECT * FROM {table} WHERE id = ?", id)
        rows = self.db_cursor.fetchall()
        self.db_disconnect()
        return rows

    def populate_customer_table(
        self,
        table: str,
        table_widget: QTableWidget,
        search_params: tuple,
        query_string: str,
    ):
        rows = self.db_customer_interaction(
            table, table_widget, search_params, query_string
        )
        for index, row in enumerate(rows):
            for i in range(4):
                table_widget.setItem(index, i, QTableWidgetItem(row[i + 1]))
            table_widget.setItem(index, 4, QTableWidgetItem(f"{row[0]}"))
            table_widget.insertRow(index + 1)

    def search_customers_populate_table(
        self,
        table: str,
        table_widget: QTableWidget,
        search_params: tuple,
        query_string: str,
    ):
        rows = self.db_customer_interaction(
            table, table_widget, search_params, query_string
        )
        for index, row in enumerate(rows):
            for i in range(4):
                table_widget.setItem(index, i, QTableWidgetItem(row[i + 1]))
            table_widget.setItem(index, 4, QTableWidgetItem(f"{row[0]}"))
            table_widget.insertRow(index + 1)

    def delete_selected_customer(self, table: str, table_widget: QTableWidget):
        self.popup_module.set_title("Brisanje")
        self.popup_module.set_question(
            "Da li želite obrisati mušteriju iz baze podataka? \n (Upozorenje: Ova radnja je nepovratna!)"
        )
        answer = self.popup_module.confirmation_dialog()
        if answer:
            if (
                table_widget.selectedItems() != []
                and table_widget.selectedItems() is not None
            ):
                selected_row = table_widget.selectedItems()
                self.db_connect(self.database)
                self.db_cursor = self.db_link.cursor()
                self.db_cursor.execute(
                    f"DELETE FROM {table} WHERE id = ?",
                    (selected_row[4].text(),),
                )
                self.db_disconnect()
                table_widget.removeRow(table_widget.currentRow())
            # self.populate_customer_table(table, table_widget, (), "")

    def clear_customer_table(self, table_widget: QTableWidget):
        for i in range(table_widget.rowCount(), 0, -1):
            table_widget.removeRow(i)

        for i in range(5):
            table_widget.setItem(0, i, QTableWidgetItem(""))
