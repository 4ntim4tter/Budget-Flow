from PyQt6.QtWidgets import QMessageBox, QAbstractButton
from PyQt6.QtCore import Qt


class QuestionPopup:
    def __init__(self, yes: str, no: str, title: str, question: str) -> None:
        self.yes = yes
        self.no = no
        self.title = title
        self.question = question
        self.style = """QMessageBox {
                background-color: #333333;
                border: 2px;
                border-style: groove;
                border-color: darkgrey;
            }

            QPushButton {
                background-color: #333333;
                color: white;
            }

            QMessageBox QLabel {
                color: white;
            }
            """

    def set_title(self, title):
        self.title = title

    def set_question(self, question):
        self.question = question

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        conf_dialog.setIcon(QMessageBox.Icon.Question)
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

class WarningPopup:
    def __init__(self, title: str, warning: str) -> None:
        self.ok = "OK"
        self.title = title
        self.warning = warning
        self.style = """QMessageBox {
                background-color: #333333;
                border: 2px;
                border-style: groove;
                border-color: darkgrey;
            }

            QPushButton {
                background-color: #333333;
                color: white;
            }

            QMessageBox QLabel {
                color: white;
            }
            """

    def set_title(self, title):
        self.title = title

    def set_warning(self, warning):
        self.warning = warning

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        conf_dialog.setIcon(QMessageBox.Icon.Warning)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setWindowTitle(self.title)
        conf_dialog.setText(self.warning)
        conf_dialog.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Ok)
        yes_button.setText(self.ok)
        yes_button.setStyleSheet(self.style)
        conf_dialog.exec()