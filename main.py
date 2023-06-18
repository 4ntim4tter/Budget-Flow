from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from window_operator import WindowOperator as wop

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.customer_entry_box.hide()

form.action_open_customer_entry_box.triggered.connect(lambda: wop.window_visibility(form.customer_entry_box))

form.cancel_new_customer_button.clicked.connect(lambda: wop.window_visibility(form.customer_entry_box))


def main():
    window.show()
    window.showMaximized()
    app.exec()
    

if __name__ == "__main__":
    main()