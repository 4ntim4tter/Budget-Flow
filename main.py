from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType('untitled.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.add_customer_widget.hide()

def main():
    window.show()
    app.exec()
    

if __name__ == "__main__":
    main()