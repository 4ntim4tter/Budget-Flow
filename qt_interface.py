        
class AppInterface():
    def __init__(self, entry_window, db_manager, form, window, formReciept, windowRecepit, formSettings, windowSettings, app, loader):
        self._form = form
        self._window = window
        self._entry_window = entry_window
        self._db_manager = db_manager
        self._formReceipt = formReciept
        self._windowReceipt = windowRecepit
        self._formSettings = formSettings
        self._windowSettings = windowSettings
        self._app = app
        self._loader = loader

        self._form.cancel_new_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self._form.customer_entry_box)
        )
        self._form.save_new_customer_button.clicked.connect(
            lambda: self._entry_window.store_entered_data(
                "customers", self._entry_window.get_customer_values(self._form), self._form.customer_entry_box
            )
        )

        # Customer Search Window
        self._form.cancel_search_customer_button.clicked.connect(
            lambda: self._entry_window.wipe_customer_window_data(self._form.customer_search_box)
        )
        self._form.search_customer_button.clicked.connect(
            lambda: self._entry_window.search_for_customer(
                "customers", self._form.customer_table, self._form
            )
        )

        # Customer Table
        self._form.populate_table_button.clicked.connect(
            lambda: self._db_manager.populate_customer_table(
                "customers", self._form.customer_table, (), ""
            )
        )
        self._form.show_archived_button.clicked.connect(
            lambda: self._entry_window.populate_customer_table_archived(
                "customers", self._form.customer_table
            )
        )
        self._form.archive_selected_button.clicked.connect(
            lambda: self._entry_window.change_customer_archive_status(self._form)
        )
        self._form.delete_selected_table_button.clicked.connect(
            lambda: self._db_manager.delete_selected_customer("customers", self._form.customer_table)
        )

        self._form.customer_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_customer_from_table(self._form, self._form.customer_table)
        )

        # Reciepts
        self._form.new_reciept_button.clicked.connect(
            lambda: self._entry_window.hide_customer_form(
                self._form.user_data_frame, self._form.add_new_reciept_frame, self._form
            )
        )
        self._form.cancel_add_reciept_button.clicked.connect(
            lambda: self._entry_window.close_add_new_receipt(self._form)
        )
        self._form.add_material_button.clicked.connect(
            lambda: self._entry_window.add_material_to_recipe(
                self._form.materials_receipt_table,
                self._form.add_receipt_material,
                self._form.add_receipt_brand,
                self._form.add_receipt_price,
                self._form.add_receipt_amount,
            )
        )
        self._form.finish_reciept_button.clicked.connect(
            lambda: self._entry_window.add_new_receipt(self._form)
        )
        self._form.delete_reciept_button.clicked.connect(
            lambda: self._entry_window.delete_selected_reciept(self._form)
        )
        self._form.customer_reciepts_table.itemDoubleClicked.connect(
            lambda: self._entry_window.select_reciept_from_table(self._form, self._formReceipt, self._windowReceipt)
        )
        self._form.close_register_button.clicked.connect(
            lambda: self._entry_window.close_application(self._app)
        )
        self._form.settings_button.clicked.connect(
            lambda: self._entry_window.open_settings(self._formSettings, self._windowSettings)
        )
        self._formReceipt.print_reciept_button.clicked.connect(
            lambda: self._entry_window.open_browser_for_print(
                {
                    "name": self._form.name_text_data.text()
                    + " "
                    + self._form.surname_text_data.text(),
                    "vehicle": self._form.vehicle_text_data.text(),
                    "plates": self._form.plates_text_data.text(),
                },
                self._form.customer_reciepts_table.selectedItems(),
                self._formReceipt.materials_receipt_table,
            )
        )
        self._formReceipt.cancel_print_reciept_button.clicked.connect(
            lambda: self._entry_window.cancel_receipt_printing(
                self._windowReceipt, self._form, self._form.customer_table
            )
        )
        self._formReceipt.delete_entry_button.clicked.connect(
            lambda: self._entry_window.delete_entry_from_receipt(
                self._formReceipt.materials_receipt_table, self._form, self._form.customer_table
            )
        )

        self._formReceipt.modify_reciept_button.clicked.connect(
            lambda: self._entry_window.modify_receipt_entry(
                self._formReceipt.materials_receipt_table, self._form, self._form.customer_table
            )
        )

        self._formSettings.cancel_settings_button.clicked.connect(
            lambda: self._entry_window.cancel_settings(
                self._formSettings, self._windowSettings
            )
        )

        self._formSettings.save_settings_button.clicked.connect(
            lambda: self._entry_window.save_settings(
                self._formSettings, self._windowSettings, self._loader
            )
        )