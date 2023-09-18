from email.charset import QP
import sys
from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtCore import QProcess

from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow


class LoadUi:
    def __init__(self, language: str, entry_window):
        self.app = QApplication([])
        self.entry_window = entry_window
        
        self._default_language = language
        self._MainForm:Ui_MainWindow
        self._MainWindow:QMainWindow
        self._ReceiptForm:Ui_ReceiptWindow
        self._ReceiptWindow:QDialog
        self._SettingsForm:Ui_SettingsWindow
        self._SettingsWindow:QDialog
        
        if self._default_language == "english":
            self._MainForm, self._MainWindow = loadUiType("englishMain.ui")
            self._ReceiptForm, self._ReceiptWindow = loadUiType("englishRec.ui")
            self._SettingsForm, self._SettingsWindow = loadUiType("englishSettings.ui")
        else:
            self._MainForm, self._MainWindow = loadUiType("bosnianMain.ui")
            self._ReceiptForm, self._ReceiptWindow = loadUiType("bosnianRec.ui")
            self._SettingsForm, self._SettingsWindow = loadUiType("bosnianSettings.ui")


        self.form = self._MainForm()
        self.window = self._MainWindow()
        self.form.setupUi(self.window)
        
        self.formReceipt = self._ReceiptForm()
        self.windowReceipt = self._ReceiptWindow()
        self.formReceipt.setupUi(self.windowReceipt)
        
        self.formSettings = self._SettingsForm()
        self.windowSettings = self._SettingsWindow()
        self.formSettings.setupUi(self.windowSettings)
        
        self.form.add_new_reciept_frame.hide()
        self.app.focusChanged.connect(entry_window.line_focus_changed)
        
    def set_style(self):
        self.app.setStyleSheet(
            """QLabel,
            QPushButton, 
            QLineEdit, 
            QTableWidget, 
            QTableWidgetItem,
            QTableView,
            QHeaderView::section
            {font-family: Rec Mono Casual;}"""
        )
        
    def change_language(self):
        self.app.quit()
        process = QProcess
        process.startDetached("C:/Users/ANES/Budget Flow/main.py")

    def get_app(self):
        return self.app
    
    
    def run(self):
        self.window.show()
        self.app.exec()