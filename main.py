from PyQt6.uic.load_ui import loadUiType
from PyQt6.QtWidgets import QApplication, QMainWindow
from bosnianMain_ui import Ui_MainWindow
from bosnianRec_ui import Ui_ReceiptWindow

from window_operator import WindowOperator
from database_management import DataManager

Form, Window = loadUiType("englishMain.ui")
Receipt, ReceiptWindow = loadUiType("englishRec.ui")

app = QApplication([])

window: QMainWindow = Window()
formMain: Ui_MainWindow = Form()
formMain.setupUi(window)

receiptWindow = ReceiptWindow()
receiptForm: Ui_ReceiptWindow = Receipt()
receiptForm.setupUi(receiptWindow)

db_manager = DataManager("table.db")
entry_window = WindowOperator()
formMain.add_new_reciept_frame.hide()
new_customer_window = formMain.customer_entry_box
customer_search_window = formMain.customer_search_box

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

# focus changed signal
app.focusChanged.connect(entry_window.line_focus_changed)

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
    lambda: entry_window.close_application(app)
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


def main():
    window.show()
    app.setStyleSheet(
        """QLabel,
        QPushButton, 
        QLineEdit, 
        QTableWidget, 
        QTableWidgetItem,
        QTableView,
        QHeaderView::section
        {font-family: Rec Mono Casual;}"""
    )
    window.showMaximized()
    # window.showFullScreen()
    app.exec()


if __name__ == "__main__":
    main()
