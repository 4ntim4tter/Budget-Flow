from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow


class LoadUi:
    def __init__(self, language: str, entry_window, db_manager):
        self.app = QApplication([])
        self._entry_window = entry_window
        self._default_language = language
        self._db_manager = db_manager

        self._MainFormEnglish, self._MainWindowEnglish = loadUiType("englishMain.ui")
        self._ReceiptFormEnglish, self._ReceiptWindowEnglish = loadUiType("englishRec.ui")
        self._SettingsFormEnglish, self._SettingsWindowEnglish = loadUiType("englishSettings.ui")
        
        self._MainFormBosnian, self._MainWindowBosnian = loadUiType("bosnianMain.ui")
        self._ReceiptFormBosnian, self._ReceiptWindowBosnian = loadUiType("bosnianRec.ui")
        self._SettingsFormBosnian, self._SettingsWindowBosnian = loadUiType("bosnianSettings.ui")

        if self._default_language == "english":
            self.form:Ui_MainWindow = self._MainFormEnglish()
            self.window:QMainWindow = self._MainWindowEnglish()
            self.form.setupUi(self.window)
            
            self.formReceipt:Ui_ReceiptWindow = self._ReceiptFormEnglish()
            self.windowReceipt:QDialog = self._ReceiptWindowEnglish()
            self.formReceipt.setupUi(self.windowReceipt)
            
            self.formSettings:Ui_SettingsWindow = self._SettingsFormEnglish()
            self.windowSettings:QDialog = self._SettingsWindowEnglish()
            self.formSettings.setupUi(self.windowSettings)
        else:
            self.form:Ui_MainWindow = self._MainFormBosnian()
            self.window:QMainWindow = self._MainWindowBosnian()
            self.form.setupUi(self.window)
            
            self.formReceipt:Ui_ReceiptWindow = self._ReceiptFormBosnian()
            self.windowReceipt:QDialog = self._ReceiptWindowBosnian()
            self.formReceipt.setupUi(self.windowReceipt)
            
            self.formSettings:Ui_SettingsWindow = self._SettingsFormBosnian()
            self.windowSettings:QDialog = self._SettingsWindowBosnian()
            self.formSettings.setupUi(self.windowSettings)
        
        self.form.add_new_reciept_frame.hide()
        self.app.focusChanged.connect(self._entry_window.line_focus_changed)
        
        if self._default_language == "english":
            self.formSettings.language_combo.setCurrentIndex(0)
        else:
            self.formSettings.language_combo.setCurrentIndex(1)
        
        self.form.cancel_new_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self.form.customer_entry_box)
        )
        self.form.save_new_customer_button.clicked.connect(
            lambda: self._entry_window.store_entered_data(
                "customers", self._entry_window.get_customer_values(self.form), self.form.customer_entry_box
            )
        )

        # Customer Search Window
        self.form.cancel_search_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self.form.customer_search_box)
        )
        self.form.search_customer_button.clicked.connect(
            lambda: self._entry_window.search_for_customer(
                "customers", self.form.customer_table, self.form
            )
        )

        # Customer Table
        self.form.populate_table_button.clicked.connect(
            lambda: self._db_manager.populate_customer_table(
                "customers", self.form.customer_table, (), ""
            )
        )
        self.form.show_archived_button.clicked.connect(
            lambda: self._entry_window.populate_customer_table_archived(
                "customers", self.form.customer_table
            )
        )
        self.form.archive_selected_button.clicked.connect(
            lambda: self._entry_window.change_customer_archive_status(self.form)
        )
        self.form.delete_selected_table_button.clicked.connect(
            lambda: self._db_manager.delete_selected_customer("customers", self.form.customer_table)
        )

        self.form.customer_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_customer_from_table(self.form, self.form.customer_table)
        )

        # Reciepts
        self.form.new_reciept_button.clicked.connect(
            lambda: self._entry_window.hide_customer_form(
                self.form.user_data_frame, self.form.add_new_reciept_frame, self.form
            )
        )
        self.form.cancel_add_reciept_button.clicked.connect(
            lambda: self._entry_window.close_add_new_receipt(self.form)
        )
        self.form.add_material_button.clicked.connect(
            lambda: self._entry_window.add_material_to_recipe(
                self.form.materials_receipt_table,
                self.form.add_receipt_material,
                self.form.add_receipt_brand,
                self.form.add_receipt_price,
                self.form.add_receipt_amount,
            )
        )
        self.form.finish_reciept_button.clicked.connect(
            lambda: self._entry_window.add_new_receipt(self.form)
        )
        self.form.delete_reciept_button.clicked.connect(
            lambda: self._entry_window.delete_selected_reciept(self.form)
        )
        self.form.customer_reciepts_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_reciept_from_table(self.form, self.formReceipt, self.windowReceipt)
        )
        self.form.close_register_button.clicked.connect(
            lambda: self._entry_window.close_application(self.get_app())
        )
        self.form.settings_button.clicked.connect(
            lambda: self._entry_window.open_settings(self.formSettings, self.windowSettings)
        )
        self.formReceipt.print_reciept_button.clicked.connect(
            lambda: self._entry_window.open_browser_for_print(
                {
                    "name": self.form.name_text_data.text()
                    + " "
                    + self.form.surname_text_data.text(),
                    "vehicle": self.form.vehicle_text_data.text(),
                    "plates": self.form.plates_text_data.text(),
                },
                self.form.customer_reciepts_table.selectedItems(),
                self.formReceipt.materials_receipt_table,
            )
        )
        self.formReceipt.cancel_print_reciept_button.clicked.connect(
            lambda: self._entry_window.cancel_receipt_printing(
                self.windowReceipt, self.form, self.form.customer_table
            )
        )
        self.formReceipt.delete_entry_button.clicked.connect(
            lambda: self._entry_window.delete_entry_from_receipt(
                self.formReceipt.materials_receipt_table, self.form, self.form.customer_table
            )
        )

        self.formReceipt.modify_reciept_button.clicked.connect(
            lambda: self._entry_window.modify_receipt_entry(
                self.formReceipt.materials_receipt_table, self.form, self.form.customer_table
            )
        )

        self.formSettings.cancel_settings_button.clicked.connect(
            lambda: self._entry_window.cancel_settings(
                self.formSettings, self.windowSettings
            )
        )

        self.formSettings.save_settings_button.clicked.connect(
            lambda: self._entry_window.save_settings(
                self.formSettings, self.windowSettings, self
            )
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

    def change_language(self, language):
        #I HATE THIS DUPLICATE CODE BUT I CAN'T FIGURE OUT A BETTER WAY
        self.window.hide()
        if language == "english":
            self.form:Ui_MainWindow = self._MainFormEnglish()
            self.window:QMainWindow = self._MainWindowEnglish()
            self.form.setupUi(self.window)
            
            self.formReceipt:Ui_ReceiptWindow = self._ReceiptFormEnglish()
            self.windowReceipt:QDialog = self._ReceiptWindowEnglish()
            self.formReceipt.setupUi(self.windowReceipt)
            
            self.formSettings:Ui_SettingsWindow = self._SettingsFormEnglish()
            self.windowSettings:QDialog = self._SettingsWindowEnglish()
            self.formSettings.setupUi(self.windowSettings)
        else:
            self.form:Ui_MainWindow = self._MainFormBosnian()
            self.window:QMainWindow = self._MainWindowBosnian()
            self.form.setupUi(self.window)
            
            self.formReceipt:Ui_ReceiptWindow = self._ReceiptFormBosnian()
            self.windowReceipt:QDialog = self._ReceiptWindowBosnian()
            self.formReceipt.setupUi(self.windowReceipt)
            
            self.formSettings:Ui_SettingsWindow = self._SettingsFormBosnian()
            self.windowSettings:QDialog = self._SettingsWindowBosnian()
            self.formSettings.setupUi(self.windowSettings)
        
        self.form.add_new_reciept_frame.hide()
        self.app.focusChanged.connect(self._entry_window.line_focus_changed)
        
        if language == "english":
            self.formSettings.language_combo.setCurrentIndex(0)
        else:
            self.formSettings.language_combo.setCurrentIndex(1)
        
        self.form.cancel_new_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self.form.customer_entry_box)
        )
        self.form.save_new_customer_button.clicked.connect(
            lambda: self._entry_window.store_entered_data(
                "customers", self._entry_window.get_customer_values(self.form), self.form.customer_entry_box
            )
        )

        # Customer Search Window
        self.form.cancel_search_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self.form.customer_search_box)
        )
        self.form.search_customer_button.clicked.connect(
            lambda: self._entry_window.search_for_customer(
                "customers", self.form.customer_table, self.form
            )
        )

        # Customer Table
        self.form.populate_table_button.clicked.connect(
            lambda: self._db_manager.populate_customer_table(
                "customers", self.form.customer_table, (), ""
            )
        )
        self.form.show_archived_button.clicked.connect(
            lambda: self._entry_window.populate_customer_table_archived(
                "customers", self.form.customer_table
            )
        )
        self.form.archive_selected_button.clicked.connect(
            lambda: self._entry_window.change_customer_archive_status(self.form)
        )
        self.form.delete_selected_table_button.clicked.connect(
            lambda: self._db_manager.delete_selected_customer("customers", self.form.customer_table)
        )

        self.form.customer_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_customer_from_table(self.form, self.form.customer_table)
        )

        # Reciepts
        self.form.new_reciept_button.clicked.connect(
            lambda: self._entry_window.hide_customer_form(
                self.form.user_data_frame, self.form.add_new_reciept_frame, self.form
            )
        )
        self.form.cancel_add_reciept_button.clicked.connect(
            lambda: self._entry_window.close_add_new_receipt(self.form)
        )
        self.form.add_material_button.clicked.connect(
            lambda: self._entry_window.add_material_to_recipe(
                self.form.materials_receipt_table,
                self.form.add_receipt_material,
                self.form.add_receipt_brand,
                self.form.add_receipt_price,
                self.form.add_receipt_amount,
            )
        )
        self.form.finish_reciept_button.clicked.connect(
            lambda: self._entry_window.add_new_receipt(self.form)
        )
        self.form.delete_reciept_button.clicked.connect(
            lambda: self._entry_window.delete_selected_reciept(self.form)
        )
        self.form.customer_reciepts_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_reciept_from_table(self.form, self.formReceipt, self.windowReceipt)
        )
        self.form.close_register_button.clicked.connect(
            lambda: self._entry_window.close_application(self.get_app())
        )
        self.form.settings_button.clicked.connect(
            lambda: self._entry_window.open_settings(self.formSettings, self.windowSettings)
        )
        self.formReceipt.print_reciept_button.clicked.connect(
            lambda: self._entry_window.open_browser_for_print(
                {
                    "name": self.form.name_text_data.text()
                    + " "
                    + self.form.surname_text_data.text(),
                    "vehicle": self.form.vehicle_text_data.text(),
                    "plates": self.form.plates_text_data.text(),
                },
                self.form.customer_reciepts_table.selectedItems(),
                self.formReceipt.materials_receipt_table,
            )
        )
        self.formReceipt.cancel_print_reciept_button.clicked.connect(
            lambda: self._entry_window.cancel_receipt_printing(
                self.windowReceipt, self.form, self.form.customer_table
            )
        )
        self.formReceipt.delete_entry_button.clicked.connect(
            lambda: self._entry_window.delete_entry_from_receipt(
                self.formReceipt.materials_receipt_table, self.form, self.form.customer_table
            )
        )

        self.formReceipt.modify_reciept_button.clicked.connect(
            lambda: self._entry_window.modify_receipt_entry(
                self.formReceipt.materials_receipt_table, self.form, self.form.customer_table
            )
        )

        self.formSettings.cancel_settings_button.clicked.connect(
            lambda: self._entry_window.cancel_settings(
                self.formSettings, self.windowSettings
            )
        )

        self.formSettings.save_settings_button.clicked.connect(
            lambda: self._entry_window.save_settings(
                self.formSettings, self.windowSettings, self
            )
        )
        self.window.show()
        
    def get_app(self):
        return self.app
    
    def run(self):
        self.set_style()
        self.window.show()
        self.app.exec()