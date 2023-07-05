from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication

from window_operator import WindowOperator
from database_management import DataManager

Form, Window = loadUiType("untitled.ui")

app = QApplication([])

window = Window()
form = Form()
form.setupUi(window)

db_manager = DataManager("table.db")
entry_window = WindowOperator()
new_customer_window = form.customer_entry_box
customer_search_window = form.customer_search_box

db_manager.db_connect("table.db")
db_manager.db_create_table(
    "customers", ["id", "name", "surname", "phone", "vehicle", "plates", "chasis"]
)

# focus changed signal
app.focusChanged.connect(entry_window.line_focus_changed)

# Customer Entry Window
form.cancel_new_customer_button.clicked.connect(
    lambda: entry_window.wipe_entered_data(new_customer_window)
)
form.save_new_customer_button.clicked.connect(
    lambda: entry_window.store_entered_data(
        "customers",
        entry_window.get_customer_values(form),
        new_customer_window
    )
)

# Customer Search Window
form.cancel_search_customer_button.clicked.connect(
    lambda: entry_window.wipe_entered_data(customer_search_window)
)
form.search_customer_button.clicked.connect(
    lambda: entry_window.search_for_customer("customers", form.customer_table, form)
)

# Customer Table
form.populate_table_button.clicked.connect(
    lambda: db_manager.populate_customer_table("customers", form.customer_table, (), "")
)
form.clear_table_button.clicked.connect(
    lambda: db_manager.clear_customer_table(form.customer_table)
)
form.delete_selected_table_button.clicked.connect(
    lambda: db_manager.delete_selected_customer("customers", form.customer_table)
)

form.customer_table.itemDoubleClicked.connect(
    lambda: entry_window.select_customer_from_table(form, form.customer_table)
)


def main():
    window.show()
    # window.showMaximized()
    app.exec()


if __name__ == "__main__":
    main()
