import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.uic.load_ui import loadUiType

from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow
from qt_interface import AppInterface


class LoadUi:
    def __init__(self, language: str, entry_window, db_manager, screen: bool):
        self.app = QApplication([])
        self._entry_window = entry_window
        self._default_language = language
        self._db_manager = db_manager
        self._screen = screen
        
        if os.path.isfile("englishMain.ui"):
            self.englishMainUi = "englishMain.ui"
            self.englishRecUi = "englishRec.ui"
            self.englishSettingsUi = "englishSettings.ui"   
            
            self.bosnianMainUi = "bosnianMain.ui"
            self.bosnianRecUi = "bosnianRec.ui"
            self.bosnianSettingsUi = "bosnianSettings.ui"
        else:
            self.englishMainUi = "_internal/englishMain.ui"
            self.englishRecUi = "_internal/englishRec.ui"
            self.englishSettingsUi = "_internal/englishSettings.ui"   
            
            self.bosnianMainUi = "_internal/bosnianMain.ui"
            self.bosnianRecUi = "_internal/bosnianRec.ui"
            self.bosnianSettingsUi = "_internal/bosnianSettings.ui"

        self._MainFormEnglish, self._MainWindowEnglish = loadUiType(self.englishMainUi)
        self._ReceiptFormEnglish, self._ReceiptWindowEnglish = loadUiType(self.englishRecUi)
        self._SettingsFormEnglish, self._SettingsWindowEnglish = loadUiType(self.englishSettingsUi)

        self._MainFormBosnian, self._MainWindowBosnian = loadUiType(self.bosnianMainUi)
        self._ReceiptFormBosnian, self._ReceiptWindowBosnian = loadUiType(self.bosnianRecUi)
        self._SettingsFormBosnian, self._SettingsWindowBosnian = loadUiType(self.bosnianSettingsUi)

        if self._default_language == "english":
            self.form: Ui_MainWindow = self._MainFormEnglish()
            self.window: QMainWindow = self._MainWindowEnglish()
            self.form.setupUi(self.window)

            self.formReceipt: Ui_ReceiptWindow = self._ReceiptFormEnglish()
            self.windowReceipt: QDialog = self._ReceiptWindowEnglish()
            self.formReceipt.setupUi(self.windowReceipt)

            self.formSettings: Ui_SettingsWindow = self._SettingsFormEnglish()
            self.windowSettings: QDialog = self._SettingsWindowEnglish()
            self.formSettings.setupUi(self.windowSettings)
        else:
            self.form: Ui_MainWindow = self._MainFormBosnian()
            self.window: QMainWindow = self._MainWindowBosnian()
            self.form.setupUi(self.window)

            self.formReceipt: Ui_ReceiptWindow = self._ReceiptFormBosnian()
            self.windowReceipt: QDialog = self._ReceiptWindowBosnian()
            self.formReceipt.setupUi(self.windowReceipt)

            self.formSettings: Ui_SettingsWindow = self._SettingsFormBosnian()
            self.windowSettings: QDialog = self._SettingsWindowBosnian()
            self.formSettings.setupUi(self.windowSettings)

        self.form.add_new_reciept_frame.hide()
        self.app.focusChanged.connect(self._entry_window.line_focus_changed)

        if self._default_language == "english":
            self.formSettings.language_combo.setCurrentIndex(0)
        else:
            self.formSettings.language_combo.setCurrentIndex(1)

        if self._screen:
            self.window.showFullScreen()
            self.formSettings.full_screen_check.setChecked(True)
            
        self.app_interface = AppInterface(
            self._entry_window,
            self._db_manager,
            self.form,
            self.window,
            self.formReceipt,
            self.windowReceipt,
            self.formSettings,
            self.windowSettings,
            self.app,
            self,
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
            {font-family: Lucida Console;}"""
        )

    def change_language(self, language):
        self.window.hide()
        self.windowReceipt.hide()
        self.windowSettings.hide()
        if language == "english":
            self.form: Ui_MainWindow = self._MainFormEnglish()
            self.window: QMainWindow = self._MainWindowEnglish()
            self.form.setupUi(self.window)

            self.formReceipt: Ui_ReceiptWindow = self._ReceiptFormEnglish()
            self.windowReceipt: QDialog = self._ReceiptWindowEnglish()
            self.formReceipt.setupUi(self.windowReceipt)

            self.formSettings: Ui_SettingsWindow = self._SettingsFormEnglish()
            self.windowSettings: QDialog = self._SettingsWindowEnglish()
            self.formSettings.setupUi(self.windowSettings)
        else:
            self.form: Ui_MainWindow = self._MainFormBosnian()
            self.window: QMainWindow = self._MainWindowBosnian()
            self.form.setupUi(self.window)

            self.formReceipt: Ui_ReceiptWindow = self._ReceiptFormBosnian()
            self.windowReceipt: QDialog = self._ReceiptWindowBosnian()
            self.formReceipt.setupUi(self.windowReceipt)

            self.formSettings: Ui_SettingsWindow = self._SettingsFormBosnian()
            self.windowSettings: QDialog = self._SettingsWindowBosnian()
            self.formSettings.setupUi(self.windowSettings)
            
        self.form.add_new_reciept_frame.hide()
        self.app.focusChanged.connect(self._entry_window.line_focus_changed)

        if language == "english":
            self.formSettings.language_combo.setCurrentIndex(0)
        else:
            self.formSettings.language_combo.setCurrentIndex(1)

        self.app_interface = AppInterface(
            self._entry_window,
            self._db_manager,
            self.form,
            self.window,
            self.formReceipt,
            self.windowReceipt,
            self.formSettings,
            self.windowSettings,
            self.app,
            self,
        )
        self.window.show()

    def get_app(self):
        return self.app
    
    def change_screen_size(self, screen: bool):
        if screen:
            self.window.showFullScreen()
            self.formSettings.full_screen_check.setChecked(True)

    def run(self):
        self.set_style()
        self.window.show()
        self.app.exec()
