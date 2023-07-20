from PyQt6.QtWidgets import QLineEdit, QWidget, QTableWidget, QFrame, QTableWidgetItem
from PyQt6.QtGui import QDoubleValidator
from customer import Customer
from database_management import DataManager
from popup_module import QuestionPopup, WarningPopup


class WindowOperator:
    def __init__(self) -> None:
        self.db_manager = DataManager("table.db")
        self.question_box = QuestionPopup("Yes", "No", "", "")
        self.warning_box = WarningPopup("Upozorenje!", "")

    def question_popup(self, title: str, question: str):
        self.question_box.set_title(title)
        self.question_box.set_question(question)
        answer = self.question_box.confirmation_dialog()
        return answer

    def warning_popup(self, warning: str):
        self.warning_box.set_warning(warning)
        answer = self.warning_box.confirmation_dialog()
        return answer

    def wipe_entered_data(self, widget):
        widgets = widget.children()
        for child in widgets:
            if isinstance(child, QLineEdit):
                p_text = child.placeholderText()
                child.setText("")
                child.setInputMask("")
                child.setPlaceholderText(p_text)
            if isinstance(child, QTableWidget):
                child.clearContents()
                child.setRowCount(1)

    def store_entered_data(self, table: str, customer: list, entry_widget: QWidget):
        accepted = self.db_manager.db_insert_customer(table, customer)
        if accepted:
            self.wipe_entered_data(entry_widget)

    def wipe_customer_window_data(self, window):
        answer = self.question_popup("Prekid", "Da li želite obrisati unesene podatke?")
        if answer:
            self.wipe_entered_data(window)

    def get_customer_values(self, widget):
        customer = Customer(
            widget.add_customer_name.text(),
            widget.add_customer_surname.text(),
            widget.add_customer_phone.text(),
            widget.add_customer_vehicle.text(),
            widget.add_customer_plates.text(),
            widget.add_customer_chasis.text(),
        )

        return customer.get_data()

    def line_focus_changed(self, new, old: QLineEdit):
        if old is not None and hasattr(old, "placeholderText"):
            if old.placeholderText() == "Registracija":
                old.setInputMask("NNN-N-NNN")
            if old.placeholderText() == "Telefon":
                old.setInputMask("999-999-999")
            if old.placeholderText() == "Cijena":
                old.setValidator(QDoubleValidator())
            if old.placeholderText() == "Količina":
                old.setValidator(QDoubleValidator())

    def search_for_customer(self, table: str, table_widget: QTableWidget, widget):
        customer = Customer(
            widget.search_customer_name.text(),
            widget.search_customer_surname.text(),
            widget.search_customer_phone.text(),
            widget.search_customer_vehicle.text(),
            widget.search_customer_plates.text(),
            widget.search_customer_chasis.text(),
        )
        temporary_params = []
        all_queries = [
            "name LIKE ? COLLATE NOCASE",
            "surname LIKE ?",
            "phone LIKE ?",
            "vehicle LIKE ?",
            "plates LIKE ?",
            "chasis LIKE ?",
        ]
        query = []
        for index, item in enumerate(customer.get_data()):
            if item != "" and item != None and item != "--":
                temporary_params.append(item)
                query.append(all_queries[index])

        search_param = []
        query_string = ""
        for index, item in enumerate(temporary_params):
            temp = "%"
            for part in item.split("-"):
                if part != "":
                    temp += part + "%"
            if temp != "%":
                search_param.append(temp)
                query_string += query[index] + " OR "
            elif item != "":
                search_param.append(item)
                query_string += query[index] + " OR "

        query_string = "WHERE " + query_string
        self.db_manager.search_customers_populate_table(
            table, table_widget, tuple(search_param), query_string[:-4]
        )

    def select_customer_from_table(self, form, table_widget: QTableWidget):
        customer_displayed = self.db_manager.veiw_selected_customer(
            "customers", tuple([table_widget.selectedItems()[4].text()])
        )[0]
        form.id_text_data.setText(str(customer_displayed[0]))
        form.name_text_data.setText(str(customer_displayed[1]))
        form.surname_text_data.setText(str(customer_displayed[2]))
        form.phone_text_data.setText(str(customer_displayed[3]))
        form.vehicle_text_data.setText(str(customer_displayed[4]))
        form.plates_text_data.setText(str(customer_displayed[5]))
        form.chasis_text_data.setText(str(customer_displayed[6]))

        self.db_manager.customer_receipts_populate_table(
            "receipts", form.customer_reciepts_table, int(customer_displayed[0])
        )

    def hide_customer_form(self, customer_form: QFrame, add_reciept: QFrame, form):
        if form.name_text_data.text() == "":
            self.warning_popup(
                "Ne možete dodati novi predračun bez selektiranja mušterije!"
            )
            return
        if customer_form.isHidden() and not add_reciept.isHidden():
            customer_form.show()
            add_reciept.hide()
        else:
            customer_form.hide()
            add_reciept.show()

    def add_material_to_recipe(
        self,
        materials_table: QTableWidget,
        materials_input: QLineEdit,
        brand_input: QLineEdit,
        price_input: QLineEdit,
        amount_input: QLineEdit,
    ):
        materials_table.setItem(
            materials_table.rowCount() - 1,
            0,
            QTableWidgetItem(f"{materials_input.text()}"),
        )
        materials_table.setItem(
            materials_table.rowCount() - 1, 1, QTableWidgetItem(brand_input.text())
        )
        materials_table.setItem(
            materials_table.rowCount() - 1, 2, QTableWidgetItem(price_input.text())
        )
        materials_table.setItem(
            materials_table.rowCount() - 1, 3, QTableWidgetItem(amount_input.text())
        )
        materials_table.setItem(
            materials_table.rowCount() - 1,
            4,
            QTableWidgetItem(f"{int(price_input.text())*int(amount_input.text())}"),
        )
        materials_table.insertRow(materials_table.rowCount())

    def close_add_new_receipt(self, form):
        answer = self.question_popup("Prekid", "Prekinuti unos novog predračuna?")
        if answer:
            self.wipe_entered_data(form.material_fields_frame)
            self.wipe_entered_data(form.table_service_frame)
            self.hide_customer_form(
                form.user_data_frame, form.add_new_reciept_frame, form
            )

    def add_new_receipt(self, form):
        answer = self.question_popup("Završi", "Završiti i dodati novi predračun?")
        if answer:
            table: QTableWidget = form.materials_receipt_table
            full_parts_price = 0
            for row in range(table.rowCount() - 1):
                full_parts_price += float(table.item(row, 4).text())
            reciept_data = [
                form.id_text_data.text(),
                form.add_receipt_service.text(),
                str(full_parts_price + int(form.add_receipt_service.text())),
            ]
            receipt_id = self.db_manager.add_receipt_to_database(reciept_data)
            for row in range(table.rowCount() - 1):
                materials_data = [receipt_id,
                    table.item(row,0).text(),
                    table.item(row,1).text(),
                    table.item(row,2).text(),
                    table.item(row,3).text(),
                    table.item(row,4).text(),
                ]
                self.db_manager.add_materials_to_database(materials_data)
            self.wipe_entered_data(form.material_fields_frame)
            self.wipe_entered_data(form.table_service_frame)
            self.hide_customer_form(
                form.user_data_frame, form.add_new_reciept_frame, form
            )
