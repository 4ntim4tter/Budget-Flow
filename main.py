import os
from re import S
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow
from englishSettings_ui import Ui_SettingsWindow

from window_operator import WindowOperator
from database_management import DataManager
from load_ui import LoadUi


with open("settings.cfg", "+r", encoding="utf-8") as settings_config:
    if not os.path.isfile("settings.cfg"):
        settings_config.write(
            """language=english\nfullscreen=1"""
        )
    if settings_config.read() == "":
        settings_config.seek(0)
        print(settings_config.read())
        settings_config.write(
            """language=english\nfullscreen=1"""
        )
        
db_manager = DataManager("table.db")
entry_window = WindowOperator()

with open("settings.cfg", "r", encoding="utf-8") as settings_config:
    if "english" in settings_config.readlines()[0]:
        language = "english"
    else:
        language = "bosnian"    
    
ui_loader = LoadUi(language)
    
window:QMainWindow = ui_loader.ui_language_default()[1]
formMain:Ui_MainWindow = ui_loader.ui_language_default()[0]
receiptWindow:QDialog = ui_loader.ui_language_default()[3]
receiptForm:Ui_ReceiptWindow = ui_loader.ui_language_default()[2]
settingsWindow:QDialog = ui_loader.ui_language_default()[5]
settingsForm:Ui_SettingsWindow = ui_loader.ui_language_default()[4]

formMain.add_new_reciept_frame.hide()
new_customer_window = formMain.customer_entry_box
customer_search_window = formMain.customer_search_box

if language == "english":
    settingsForm.language_combo.setCurrentIndex(0)
else:
    settingsForm.language_combo.setCurrentIndex(1)


db_manager.db_connect("table.db")
db_manager.db_create_table(
    "customers",
    ["id", "name", "surname", "phone", "vehicle", "plates", "chasis", "archived"],
)
db_manager.db_create_table(
    "receipts",
    [
        "id",
        "customer_id",
        "service",
        "full_price",
    ],
)
db_manager.db_create_table(
    "materials", ["id", "reciept_id", "type", "brand", "amount", "price", "full_amount"]
)

# Customer Entry Window
formMain.cancel_new_customer_button.clicked.connect(
    lambda: entry_window.wipe_customer_window_data(new_customer_window)
)
formMain.save_new_customer_button.clicked.connect(
    lambda: entry_window.store_entered_data(
        "customers", entry_window.get_customer_values(formMain), new_customer_window
    )
)

# Customer Search Window
formMain.cancel_search_customer_button.clicked.connect(
    lambda: entry_window.wipe_customer_window_data(customer_search_window)
)
formMain.search_customer_button.clicked.connect(
    lambda: entry_window.search_for_customer(
        "customers", formMain.customer_table, formMain
    )
)

# Customer Table
formMain.populate_table_button.clicked.connect(
    lambda: db_manager.populate_customer_table(
        "customers", formMain.customer_table, (), ""
    )
)
formMain.show_archived_button.clicked.connect(
    lambda: entry_window.populate_customer_table_archived(
        "customers", formMain.customer_table
    )
)
formMain.archive_selected_button.clicked.connect(
    lambda: entry_window.change_customer_archive_status(formMain)
)
formMain.delete_selected_table_button.clicked.connect(
    lambda: db_manager.delete_selected_customer("customers", formMain.customer_table)
)

formMain.customer_table.itemDoubleClicked.connect(
    lambda: entry_window.select_customer_from_table(formMain, formMain.customer_table)
)

# Reciepts
formMain.new_reciept_button.clicked.connect(
    lambda: entry_window.hide_customer_form(
        formMain.user_data_frame, formMain.add_new_reciept_frame, formMain
    )
)
formMain.cancel_add_reciept_button.clicked.connect(
    lambda: entry_window.close_add_new_receipt(formMain)
)
formMain.add_material_button.clicked.connect(
    lambda: entry_window.add_material_to_recipe(
        formMain.materials_receipt_table,
        formMain.add_receipt_material,
        formMain.add_receipt_brand,
        formMain.add_receipt_price,
        formMain.add_receipt_amount,
    )
)
formMain.finish_reciept_button.clicked.connect(
    lambda: entry_window.add_new_receipt(formMain)
)
formMain.delete_reciept_button.clicked.connect(
    lambda: entry_window.delete_selected_reciept(formMain)
)
formMain.customer_reciepts_table.itemDoubleClicked.connect(
    lambda: entry_window.select_reciept_from_table(formMain, receiptForm, receiptWindow)
)
formMain.close_register_button.clicked.connect(
    lambda: entry_window.close_application(ui_loader.get_app())
)
formMain.settings_button.clicked.connect(
    lambda: entry_window.open_settings(settingsForm, settingsWindow)
)
receiptForm.print_reciept_button.clicked.connect(
    lambda: entry_window.open_browser_for_print(
        {
            "name": formMain.name_text_data.text()
            + " "
            + formMain.surname_text_data.text(),
            "vehicle": formMain.vehicle_text_data.text(),
            "plates": formMain.plates_text_data.text(),
        },
        formMain.customer_reciepts_table.selectedItems(),
        receiptForm.materials_receipt_table,
    )
)
receiptForm.cancel_print_reciept_button.clicked.connect(
    lambda: entry_window.cancel_receipt_printing(
        receiptWindow, formMain, formMain.customer_table
    )
)
receiptForm.delete_entry_button.clicked.connect(
    lambda: entry_window.delete_entry_from_receipt(
        receiptForm.materials_receipt_table, formMain, formMain.customer_table
    )
)

receiptForm.modify_reciept_button.clicked.connect(
    lambda: entry_window.modify_receipt_entry(
        receiptForm.materials_receipt_table, formMain, formMain.customer_table
    )
)

settingsForm.cancel_settings_button.clicked.connect(
    lambda: entry_window.cancel_settings(
        settingsForm, settingsWindow
    )
)

settingsForm.save_settings_button.clicked.connect(
    lambda: entry_window.save_settings(
        settingsForm, settingsWindow, ui_loader
    )
)

if __name__ == "__main__":
    ui_loader.set_style()
    ui_loader.run()
