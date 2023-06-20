from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from window_operator import WindowOperator
from database_management import DataManager

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.customer_entry_box.hide()

entry_window = WindowOperator()
db_manager = DataManager()

db_manager.db_connect('table.db')
db_manager.db_create_table('customers', ['id', 'name', 'surname', 'phone', 'vehicle', 'plates', 'chasis'])

form.action_open_customer_entry_box.triggered.connect(lambda:entry_window.hide_opened(form.centralwidget.children()))
form.action_open_customer_entry_box.triggered.connect(lambda: entry_window.window_visibility(form.customer_entry_box))
form.cancel_new_customer_button.clicked.connect(lambda: entry_window.window_visibility(form.customer_entry_box))
form.save_new_customer_button.clicked.connect(lambda: db_manager.db_insert_customer('customers', entry_window.get_customer_values(form)))

def main():
    window.show()
    # window.showMaximized()
    app.exec()

if __name__ == "__main__":
    main()