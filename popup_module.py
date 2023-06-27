from PyQt6.QtWidgets import QWidget, QMessageBox


class PopupModule:
    def __init__(self, yes: str, no: str, title: str, question: str) -> None:
        self.yes = yes
        self.no = no
        self.title = title
        self.question = question
        self.style = """QMessageBox {
                background-color: #333333;
            }

            QPushButton {
                background-color: #333333;
                color: white;
            }

            QMessageBox QLabel {
                color: white;
            }
            """

    def confirmation_dialog(self, popup_window: QWidget):
        conf_dialog = QMessageBox()
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setWindowTitle(self.title)
        conf_dialog.setText(self.question)
        conf_dialog.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Yes)
        yes_button.setText(self.yes)
        yes_button.setStyleSheet(self.style)
        no_button = conf_dialog.button(QMessageBox.StandardButton.No)
        no_button.setText(self.no)
        no_button.setStyleSheet(self.style)
        conf_dialog.exec()

        if conf_dialog.clickedButton() == yes_button:
            return True
        elif conf_dialog.clickedButton() == no_button:
            return False
