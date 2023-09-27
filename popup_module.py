from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt


class QuestionPopup:
    def __init__(self, language: str) -> None:
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
        self.style = """
QMessageBox
{
    background-color: rgb(36, 39, 68);
    border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
}

QMessageBox QLabel
{
    color: white;
}

QPushButton
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));
	color: #ffffff;
	min-width: 80px;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QPushButton::flat
{
	background-color: rgb(24, 25, 45);
	color:white;
}


QPushButton::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QPushButton::hover
{
	background-color: rgba(0, 85, 255, 10%);
	border: 1px solid  rgb(0, 85, 255);

}


QPushButton::pressed
{
	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.494, y2:1, stop:0.102273 rgba(0, 0, 0, 255), stop:0.880682 rgba(9, 31, 198, 167));
	border: 1px solid #b78620;

}
            """

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        conf_dialog.setIcon(QMessageBox.Icon.Question)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setText(self.question)
        conf_dialog.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Yes)
        yes_button.setText(self.yes)
        yes_button.setFlat(True)
        yes_button.setStyleSheet(self.style)
        no_button = conf_dialog.button(QMessageBox.StandardButton.No)
        no_button.setText(self.no)
        no_button.setFlat(True)
        no_button.setStyleSheet(self.style)
        conf_dialog.exec()

        if conf_dialog.clickedButton() == yes_button:
            return True
        elif conf_dialog.clickedButton() == no_button:
            return False

    def confirmation_dialog_warning(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        conf_dialog.setIcon(QMessageBox.Icon.Question)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setText(self.question + self.warning)
        conf_dialog.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Yes)
        yes_button.setText(self.yes)
        yes_button.setFlat(True)
        yes_button.setStyleSheet(self.style)
        no_button = conf_dialog.button(QMessageBox.StandardButton.No)
        no_button.setText(self.no)
        no_button.setFlat(True)
        no_button.setStyleSheet(self.style)
        conf_dialog.exec()

        if conf_dialog.clickedButton() == yes_button:
            return True
        elif conf_dialog.clickedButton() == no_button:
            return False


class WarningPopup:
    def __init__(self, language: str) -> None:
        if language == "english":
            self.ok = "OK"
            self.warning = "Operation not possible!"
        else:
            self.ok = "OK"
            self.warning = "Operacija nije moguća!"
        self.style = """
QMessageBox
{
    background-color: rgb(36, 39, 68);
    border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
}


QMessageBox QLabel
{
    color: white;
}


QPushButton
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));
	color: #ffffff;
	min-width: 80px;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QPushButton::flat
{
	background-color: rgb(24, 25, 45);
	color:white;
}


QPushButton::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QPushButton::hover
{
	background-color: rgba(0, 85, 255, 10%);
	border: 1px solid  rgb(0, 85, 255);

}


QPushButton::pressed
{
	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.494, y2:1, stop:0.102273 rgba(0, 0, 0, 255), stop:0.880682 rgba(9, 31, 198, 167));
	border: 1px solid #b78620;

}
            """

    def set_warning(self, warning):
        self.warning = warning

    def confirmation_dialog(self):
        conf_dialog = QMessageBox()
        conf_dialog.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint
        )
        conf_dialog.setIcon(QMessageBox.Icon.Warning)
        conf_dialog.setStyleSheet(self.style)
        conf_dialog.setText(self.warning)
        conf_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        yes_button = conf_dialog.button(QMessageBox.StandardButton.Ok)
        yes_button.setText(self.ok)
        yes_button.setFlat(True)
        yes_button.setStyleSheet(self.style)
        conf_dialog.exec()
