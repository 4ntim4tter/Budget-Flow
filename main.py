from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from window_operator import WindowOperator
from database_management import DataManager

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([]) 

window = Window()
form = Form()
form.setupUi(window)

entry_window = WindowOperator()
db_manager = DataManager()
new_customer_window = form.customer_entry_box
new_customer_search_window = form.customer_search_box

db_manager.db_connect('table.db')
db_manager.db_create_table('customers', ['id', 'name', 'surname', 'phone', 'vehicle', 'plates', 'chasis'])

#focus changed signal
app.focusChanged.connect(entry_window.line_focus_changed)

#Customer Entry Window
# form.action_open_customer_entry_box.triggered.connect(lambda: entry_window.hide_opened(form.centralwidget.children())) #hides all shown widgets
# form.action_open_customer_entry_box.triggered.connect(lambda: entry_window.window_visibility(new_customer_window))
form.cancel_new_customer_button.clicked.connect(lambda: entry_window.wipe_entered_data(new_customer_window))
form.save_new_customer_button.clicked.connect(lambda: db_manager.db_insert_customer('customers', entry_window.get_customer_values(form)))

#Customer Search Window
form.cancel_search_customer_button.clicked.connect(lambda: entry_window.wipe_entered_data(new_customer_search_window))

#Customer Table
db_manager.populate_customer_table('customers', form.customer_table)

def main():
    window.show()
    window.showMaximized()
    app.exec()

if __name__ == "__main__":
    main()