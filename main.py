import os

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
    
ui_loader = LoadUi(language, entry_window)

if language == "english":
    ui_loader.formSettings.language_combo.setCurrentIndex(0)
else:
    ui_loader.formSettings.language_combo.setCurrentIndex(1)


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
ui_loader.form.cancel_new_customer_button.clicked.connect(
    lambda: entry_window.wipe_customer_window_data(ui_loader.form.customer_entry_box)
)
ui_loader.form.save_new_customer_button.clicked.connect(
    lambda: entry_window.store_entered_data(
        "customers", entry_window.get_customer_values(ui_loader.form), ui_loader.form.customer_entry_box
    )
)

# Customer Search Window
ui_loader.form.cancel_search_customer_button.clicked.connect(
    lambda: entry_window.wipe_customer_window_data(ui_loader.form.customer_search_box)
)
ui_loader.form.search_customer_button.clicked.connect(
    lambda: entry_window.search_for_customer(
        "customers", ui_loader.form.customer_table, ui_loader.form
    )
)

# Customer Table
ui_loader.form.populate_table_button.clicked.connect(
    lambda: db_manager.populate_customer_table(
        "customers", ui_loader.form.customer_table, (), ""
    )
)
ui_loader.form.show_archived_button.clicked.connect(
    lambda: entry_window.populate_customer_table_archived(
        "customers", ui_loader.form.customer_table
    )
)
ui_loader.form.archive_selected_button.clicked.connect(
    lambda: entry_window.change_customer_archive_status(ui_loader.form)
)
ui_loader.form.delete_selected_table_button.clicked.connect(
    lambda: db_manager.delete_selected_customer("customers", ui_loader.form.customer_table)
)

ui_loader.form.customer_table.itemDoubleClicked.connect(
    lambda: entry_window.select_customer_from_table(ui_loader.form, ui_loader.form.customer_table)
)

# Reciepts
ui_loader.form.new_reciept_button.clicked.connect(
    lambda: entry_window.hide_customer_form(
        ui_loader.form.user_data_frame, ui_loader.form.add_new_reciept_frame, ui_loader.form
    )
)
ui_loader.form.cancel_add_reciept_button.clicked.connect(
    lambda: entry_window.close_add_new_receipt(ui_loader.form)
)
ui_loader.form.add_material_button.clicked.connect(
    lambda: entry_window.add_material_to_recipe(
        ui_loader.form.materials_receipt_table,
        ui_loader.form.add_receipt_material,
        ui_loader.form.add_receipt_brand,
        ui_loader.form.add_receipt_price,
        ui_loader.form.add_receipt_amount,
    )
)
ui_loader.form.finish_reciept_button.clicked.connect(
    lambda: entry_window.add_new_receipt(ui_loader.form)
)
ui_loader.form.delete_reciept_button.clicked.connect(
    lambda: entry_window.delete_selected_reciept(ui_loader.form)
)
ui_loader.form.customer_reciepts_table.itemDoubleClicked.connect(
    lambda: entry_window.select_reciept_from_table(ui_loader.form, ui_loader.formReceipt, ui_loader.windowReceipt)
)
ui_loader.form.close_register_button.clicked.connect(
    lambda: entry_window.close_application(ui_loader.get_app())
)
ui_loader.form.settings_button.clicked.connect(
    lambda: entry_window.open_settings(ui_loader.formSettings, ui_loader.windowSettings)
)
ui_loader.formReceipt.print_reciept_button.clicked.connect(
    lambda: entry_window.open_browser_for_print(
        {
            "name": ui_loader.form.name_text_data.text()
            + " "
            + ui_loader.form.surname_text_data.text(),
            "vehicle": ui_loader.form.vehicle_text_data.text(),
            "plates": ui_loader.form.plates_text_data.text(),
        },
        ui_loader.form.customer_reciepts_table.selectedItems(),
        ui_loader.formReceipt.materials_receipt_table,
    )
)
ui_loader.formReceipt.cancel_print_reciept_button.clicked.connect(
    lambda: entry_window.cancel_receipt_printing(
        ui_loader.windowReceipt, ui_loader.form, ui_loader.form.customer_table
    )
)
ui_loader.formReceipt.delete_entry_button.clicked.connect(
    lambda: entry_window.delete_entry_from_receipt(
        ui_loader.formReceipt.materials_receipt_table, ui_loader.form, ui_loader.form.customer_table
    )
)

ui_loader.formReceipt.modify_reciept_button.clicked.connect(
    lambda: entry_window.modify_receipt_entry(
        ui_loader.formReceipt.materials_receipt_table, ui_loader.form, ui_loader.form.customer_table
    )
)

ui_loader.formSettings.cancel_settings_button.clicked.connect(
    lambda: entry_window.cancel_settings(
        ui_loader.formSettings, ui_loader.windowSettings
    )
)

ui_loader.formSettings.save_settings_button.clicked.connect(
    lambda: entry_window.save_settings(
        ui_loader.formSettings, ui_loader.windowSettings, ui_loader
    )
)

if __name__ == "__main__":
    ui_loader.set_style()
    ui_loader.run()
