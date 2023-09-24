from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt


class QuestionPopup:
    def __init__(self,language: str) -> None:
        if language == "english":    
            self.yes = "Yes"
            self.no = "No"
            self.question = "Are you sure?"
            self.warning = "\n(Action irreversible!)"
        else:
            self.yes = "Da"
            self.no = "Ne"
            self.question = "Da li ste sigurni?"
            self.warning = "\n(Nepovratna radnja!)"
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

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        conf_dialog.setIcon(QMessageBox.Icon.Question)
        conf_dialog.setStyleSheet(self.style)
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

    def confirmation_dialog_warning(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        conf_dialog.setIcon(QMessageBox.Icon.Question)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setText(self.question+self.warning)
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
    def __init__(self, language:str) -> None:
        if language == "english":    
            self.ok = "OK"
            self.warning = "Operation not possible!"
        else:
            self.ok = "OK"
            self.warning = "Operacija nije moguća!"
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


    def set_warning(self, warning):
        self.warning = warning

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        conf_dialog.setIcon(QMessageBox.Icon.Warning)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setText(self.warning)
        conf_dialog.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Ok)
        yes_button.setText(self.ok)
        yes_button.setStyleSheet(self.style)
        conf_dialog.exec()