from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.customer_entry_box.hide()

def show_hide(window):
    if window.isHidden():
        window.show()
    else:
        window.hide()

form.action_open_customer_entry_box.triggered.connect(lambda: show_hide(form.customer_entry_box))

def main():
    window.show()
    app.exec()
    

if __name__ == "__main__":
    main()