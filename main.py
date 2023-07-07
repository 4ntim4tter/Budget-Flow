from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication

from window_operator import WindowOperator
from database_management import DataManager

Form, Window = loadUiType("untitled.ui")

app = QApplication([])

window = Window()
formMain = Form()
formMain.setupUi(window)

db_manager = DataManager("table.db")
entry_window = WindowOperator()
new_customer_window = formMain.customer_entry_box
customer_search_window = formMain.customer_search_box

db_manager.db_connect("table.db")
db_manager.db_create_table(
    "customers", ["id", "name", "surname", "phone", "vehicle", "plates", "chasis"]
)

# focus changed signal
app.focusChanged.connect(entry_window.line_focus_changed)

# Customer Entry Window
formMain.cancel_new_customer_button.clicked.connect(
    lambda: entry_window.wipe_entered_data(new_customer_window)
)
formMain.save_new_customer_button.clicked.connect(
    lambda: entry_window.store_entered_data(
        "customers",
        entry_window.get_customer_values(formMain),
        new_customer_window
    )
)

# Customer Search Window
formMain.cancel_search_customer_button.clicked.connect(
    lambda: entry_window.wipe_entered_data(customer_search_window)
)
formMain.search_customer_button.clicked.connect(
    lambda: entry_window.search_for_customer("customers", formMain.customer_table, formMain)
)

# Customer Table
formMain.populate_table_button.clicked.connect(
    lambda: db_manager.populate_customer_table("customers", formMain.customer_table, (), "")
)
formMain.clear_table_button.clicked.connect(
    lambda: db_manager.clear_customer_table(formMain.customer_table)
)
formMain.delete_selected_table_button.clicked.connect(
    lambda: db_manager.delete_selected_customer("customers", formMain.customer_table)
)

formMain.customer_table.itemDoubleClicked.connect(
    lambda: entry_window.select_customer_from_table(formMain, formMain.customer_table)
)


def main():
    window.show()
    # window.showMaximized()
    app.exec()


if __name__ == "__main__":
    main()
