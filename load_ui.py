from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QMainWindow, QDialog

from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow


class LoadUi:
    def __init__(self, language: str):
        self.default_language = language
        self.mainForm:Ui_MainWindow
        self.mainWindow:QMainWindow
        self.receiptForm:Ui_ReceiptWindow
        self.receiptWindow:QDialog
        self.settingsForm:Ui_SettingsWindow
        self.settingsWindow:QDialog
        
        if self.default_language == "english":
            self.mainForm, self.mainWindow = loadUiType("englishMain.ui")
            self.receiptForm, self.receiptWindow = loadUiType("englishRec.ui")
            self.settingsForm, self.settingsWindow = loadUiType("englishSettings.ui")
        else:
            self.mainForm, self.mainWindow = loadUiType("bosnianMain.ui")
            self.receiptForm, self.receiptWindow = loadUiType("bosnianRec.ui")
            self.settingsForm, self.settingsWindow = loadUiType("bosnianSettings.ui")

    def ui_language_default(self):
        return (
            self.mainForm,
            self.mainWindow,
            self.receiptForm,
            self.receiptWindow,
            self.settingsForm,
            self.settingsWindow,
        )
