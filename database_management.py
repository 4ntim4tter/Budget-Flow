from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from popup_module import QuestionPopup

import sqlite3 as sql3

from reciept import Reciept


class DataManager:
    def __init__(self, database: str, language:str) -> None:
        self._language = language
        self.db_link: sql3.Connection
        self.db_cursor: sql3.Cursor
        self.database = database
        self.popup_module = QuestionPopup(self._language)

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
                f"""CREATE TABLE IF NOT EXISTS {table}({fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, 
                {fields[1]} STRING, 
                {fields[2]} STRING, 
                {fields[3]} STRING, 
                {fields[4]} STRING, 
                {fields[5]} STRING, 
                {fields[6]} STRING,
                {fields[7]} INTEGER DEFAULT 0)"""
            )
        if table == "receipts":
            self.db_cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {table}(
                    {fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT, 
                    {fields[1]} INTEGER,
                    {fields[2]} FLOAT,
                    {fields[3]} FLOAT,
                    FOREIGN KEY ({fields[1]}) REFERENCES customers (id) ON DELETE CASCADE)
"""
            )
        if table == "materials":
            self.db_cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {table}(
                    {fields[0]} INTEGER PRIMARY KEY AUTOINCREMENT,
                    {fields[1]} INTEGER,
                    {fields[2]} STRING,
                    {fields[3]} STRING,
                    {fields[4]} INTEGER,
                    {fields[5]} FLOAT,
                    {fields[6]} FLOAT,
                    FOREIGN KEY ({fields[1]}) REFERENCES receipts (id) ON DELETE CASCADE)
"""
            )
        self.db_disconnect()

    def db_insert_customer(self, table: str, customer: list):
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
        self.clear_table(table_widget, 5)
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        if query_string == "":
            self.db_cursor.execute(f"SELECT * FROM {table} WHERE archived = 0")
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
        table_widget.sortItems(4)
        rows = self.db_customer_interaction(
            table, table_widget, search_params, query_string
        )
        for index, row in enumerate(rows):
            temp = ""
            table_widget.setItem(index, 0, QTableWidgetItem(row[1]))
            table_widget.setItem(index, 1, QTableWidgetItem(row[2]))
            table_widget.setItem(index, 2, QTableWidgetItem(row[3]))
            table_widget.setItem(index, 3, QTableWidgetItem(row[4]))
            if int(row[0]) < 10:
                temp = "0000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 100:
                temp = "000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 1000:
                temp = "00" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 10000:
                temp = "0" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            else:
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
            temp = ""
            table_widget.setItem(index, 0, QTableWidgetItem(row[1]))
            table_widget.setItem(index, 1, QTableWidgetItem(row[2]))
            table_widget.setItem(index, 2, QTableWidgetItem(row[3]))
            table_widget.setItem(index, 3, QTableWidgetItem(row[4]))
            if int(row[0]) < 10:
                temp = "0000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 100:
                temp = "000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 1000:
                temp = "00" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 10000:
                temp = "0" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            else:
                table_widget.setItem(index, 4, QTableWidgetItem(f"{row[0]}"))
            table_widget.insertRow(index + 1)

    def customer_receipts_populate_table(
        self, table: str, table_widget: QTableWidget, customer_id: int
    ):
        reciept = Reciept()
        self.clear_table(table_widget, 8)
        table_widget.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"SELECT * FROM {table} WHERE customer_id = {customer_id}"
        )
        rows = self.db_cursor.fetchall()
        for index, row in enumerate(rows):
            reciept.set_data(row)

            self.db_cursor.execute(
                f"SELECT type FROM materials WHERE reciept_id = {reciept.id}"
            )
            materials = ""
            for item in self.db_cursor.fetchall():
                materials += item[0] + ","

            self.db_cursor.execute(
                f"SELECT full_amount FROM materials WHERE reciept_id = {reciept.id}"
            )
            full_amount = 0
            for item in self.db_cursor.fetchall():
                full_amount += item[0]

            table_widget.setItem(index, 0, QTableWidgetItem(f"{reciept.id}"))
            table_widget.setItem(index, 1, QTableWidgetItem(f"{materials[:-1]}"))
            table_widget.setItem(index, 2, QTableWidgetItem(f"{full_amount}"))
            table_widget.setItem(index, 3, QTableWidgetItem(f"{reciept.service}"))
            table_widget.setItem(index, 4, QTableWidgetItem(f"{reciept.full_price}"))
            # table_widget.setItem(index, 5, QTableWidgetItem(f"{reciept_id}"))
            table_widget.insertRow(index + 1)

        self.db_disconnect()

    def delete_selected_customer(self, table: str, table_widget: QTableWidget):
        answer = self.popup_module.confirmation_dialog_warning()
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

    def clear_table(self, table_widget: QTableWidget, row_size):
        table_widget.clearContents()
        table_widget.setRowCount(1)
        # for i in range(table_widget.rowCount(), 0, -1):
        #     table_widget.removeRow(i)

        # for i in range(row_size):
        #     table_widget.setItem(0, i, QTableWidgetItem(""))

    def add_receipt_to_database(self, data: list):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"INSERT INTO receipts (customer_id, service, full_price) values (?,?,?)",
            data,
        )
        self.db_cursor.execute(f"SELECT * FROM receipts ORDER BY id DESC LIMIT 1;")
        receipt_id = self.db_cursor.fetchone()[0]
        self.db_disconnect()
        return receipt_id

    def add_materials_to_database(self, data: list):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"INSERT INTO materials (reciept_id, type, brand, price, amount, full_amount) values (?,?,?,?,?,?)",
            data,
        )
        self.db_disconnect()

    def delete_reciept_from_database(self, reciept_id: str):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"DELETE FROM receipts WHERE id = ?",
            (reciept_id,),
        )
        self.db_disconnect()

    def get_selected_reciept_from_database(self, reciept_id: str):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"SELECT * FROM receipts WHERE id = ?",
            (reciept_id,),
        )
        reciept_data = self.db_cursor.fetchall()

        self.db_cursor.execute(
            f"SELECT * FROM materials WHERE reciept_id = ?",
            (reciept_id,),
        )
        material_data = self.db_cursor.fetchall()
        self.db_disconnect()
        return [reciept_data, material_data]
    
    def get_archived_entries(self, table:str):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"SELECT * FROM {table} WHERE archived = 1"
        )
        archived_customers = self.db_cursor.fetchall()
        self.db_disconnect()
        return archived_customers
    
    def change_archive_status(self, id:str):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()
        self.db_cursor.execute(
            f"SELECT archived FROM customers WHERE id = {id}"
        )
        archived = self.db_cursor.fetchall()[0][0]
        if archived == 0:
            self.db_cursor.execute(
                f"UPDATE customers SET archived = 1 WHERE id = {id}"
            )
        else:
            self.db_cursor.execute(
                f"UPDATE customers SET archived = 0 WHERE id = {id}"
            )
        self.db_disconnect()

    def delete_selected_material(self, id:str):
        self.db_connect(self.database)
        self.db_cursor  = self.db_link.cursor()
        self.db_cursor.execute(
            f"DELETE FROM materials WHERE id = {id}"
        )
        self.db_disconnect()
        
    def update_selected_reciept_entry(self, table:QTableWidget):
        self.db_connect(self.database)
        self.db_cursor = self.db_link.cursor()

        table_data = []
        difference:bool = False
        total_price:float = 0.0
        recipe_id:str = ''
        for i in range(table.rowCount()):
            temp = []
            for j in range(table.columnCount()):
                temp.append(table.item(i, j).text())
            table_data.append(temp)
            self.db_cursor.execute(
                f"SELECT * FROM materials WHERE id = {table_data[i][0]}"
            )
            data = list(map(str, self.db_cursor.fetchone()))
            recipe_id = data.pop(1)

            if data != table_data[i]:
                difference = True
                self.db_cursor.execute(
                f"UPDATE materials SET type = ?, brand = ?, price = ?, amount = ?, full_amount = ? WHERE id = ?", 
                (table_data[i][1],table_data[i][2],table_data[i][3],table_data[i][4],str(float(table_data[i][3])*float(table_data[i][4])), table_data[i][0])
            )
                total_price += float(table_data[i][3])*float(table_data[i][4])

        self.db_cursor.execute(
            f"SELECT service FROM receipts WHERE id = {recipe_id}"
        )
        service = self.db_cursor.fetchone()
        
        total_price += service[0]
        
        self.db_cursor.execute(
            f"UPDATE receipts SET full_price = {total_price} WHERE id = {recipe_id}"
        )
        
        self.db_disconnect()
        
        return difference