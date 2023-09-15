from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow


class LoadUi:
    def __init__(self, language: str):
        self.app = QApplication([])
        
        self.default_language = language
        self.MainForm:Ui_MainWindow
        self.MainWindow:QMainWindow
        self.ReceiptForm:Ui_ReceiptWindow
        self.ReceiptWindow:QDialog
        self.SettingsForm:Ui_SettingsWindow
        self.SettingsWindow:QDialog
        
        if self.default_language == "english":
            self.MainForm, self.MainWindow = loadUiType("englishMain.ui")
            self.ReceiptForm, self.ReceiptWindow = loadUiType("englishRec.ui")
            self.SettingsForm, self.SettingsWindow = loadUiType("englishSettings.ui")
        else:
            self.MainForm, self.MainWindow = loadUiType("bosnianMain.ui")
            self.ReceiptForm, self.ReceiptWindow = loadUiType("bosnianRec.ui")
            self.SettingsForm, self.SettingsWindow = loadUiType("bosnianSettings.ui")


        self.form = self.MainForm()
        self.window = self.MainWindow()
        self.form.setupUi(self.window)
        
        self.formReceipt = self.ReceiptForm()
        self.windowReceipt = self.ReceiptWindow()
        self.formReceipt.setupUi(self.windowReceipt)
        
        self.formSettings = self.SettingsForm()
        self.windowSettings = self.SettingsWindow()
        self.formSettings.setupUi(self.windowSettings)

    def ui_language_default(self):
        
        return (
            self.form,
            self.window,
            self.formReceipt,
            self.windowReceipt,
            self.formSettings,
            self.windowSettings
        )
        
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

    def run(self):
        self.window.show()
        self.window.showMaximized()
        # window.showFullScreen()
        self.app.exec()