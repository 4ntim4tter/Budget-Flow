from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from window_operator import WindowOperator

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.customer_entry_box.hide()

entry_window = WindowOperator(form.customer_entry_box)

form.action_open_customer_entry_box.triggered.connect(lambda: entry_window.window_visibility())
form.cancel_new_customer_button.clicked.connect(lambda: entry_window.window_visibility())
form.save_new_customer_button.clicked.connect(lambda: print(form.add_customer_name.text()))


def main():
    window.show()
    window.showMaximized()
    app.exec()
    

if __name__ == "__main__":
    main()