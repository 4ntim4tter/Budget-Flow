from re import S
from PyQt6.QtWidgets import QLineEdit, QWidget, QTableWidget
from customer import Customer
from database_management import DataManager


class WindowOperator:
    def __init__(self) -> None:
        self.db_manager = DataManager("table.db")

    def wipe_entered_data(self, widget):
        widgets = widget.children()
        for child in widgets:
            if isinstance(child, QLineEdit):
                p_text = child.placeholderText()
                child.setText("")
                child.setInputMask("")
                child.setPlaceholderText(p_text)

    def store_entered_data(
        self, table: str, customer: list, entry_widget: QWidget, popup_window: QWidget
    ):
        accepted = self.db_manager.db_insert_customer(table, customer, popup_window)
        if accepted:
            self.wipe_entered_data(entry_widget)

    def hide_opened(self, widget):
        for item in widget:
            if hasattr(item, "hide"):
                item.hide()

    def get_customer_values(self, widget):
        customer = Customer(
            widget.add_customer_name.text(),
            widget.add_customer_surname.text(),
            widget.add_customer_phone.text(),
            widget.add_customer_vehicle.text(),
            widget.add_customer_plates.text(),
            widget.add_customer_chasis.text(),
        )

        return customer.get_data()

    def line_focus_changed(self, new, old):
        if old is not None and hasattr(old, "placeholderText"):
            if old.placeholderText() == "Registracija":
                old.setInputMask("NNN-N-NNN")
            if old.placeholderText() == "Telefon":
                old.setInputMask("999-999-999")

    def search_for_customer(self, table: str, table_widget: QTableWidget, widget):
        customer = Customer(
            widget.search_customer_name.text(),
            widget.search_customer_surname.text(),
            widget.search_customer_phone.text(),
            widget.search_customer_vehicle.text(),
            widget.search_customer_plates.text(),
            widget.search_customer_chasis.text(),
        )
        temporary_params = []
        query = [
            "name LIKE ?",
            "surname LIKE ?",
            "phone LIKE ?",
            "vehicle LIKE ?",
            "plates LIKE ?",
            "chasis LIKE ?",
        ]
        for index, item in enumerate(customer.get_data()):
            if item != "" and item != None and item != "--":
                temporary_params.append(item)
            if item == "" or item == None or item == "--":
                query[index] = ""

        search_param = []
        query_string = ""
        for index, item in enumerate(temporary_params):
            temp = '%'
            if len(item.split('-'))>1:
                for part in item.split('-'):
                    if part != '':
                        temp += (part + "%")
            
            if temp != "%":
                search_param.append(temp)
                query_string += query[index] + " OR "            
            elif item != "":
                search_param.append(item)
                query_string += query[index] + " OR "

        query_string = "WHERE " + query_string

        self.db_manager.search_customers_populate_table(
            table, table_widget, tuple(search_param), query_string[:-4]
        )

    def select_customer_from_table(self, item):
        """
        docstring
        """
        print("gottem", item.text())
