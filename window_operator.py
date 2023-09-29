import datetime
from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QFrame,
    QTableWidgetItem,
    QLabel,
    QCheckBox,
    QLineEdit,
    QDialog,
    QComboBox,
    QApplication,
) 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator
from customer import Customer
from database_management import DataManager
from popup_module import QuestionPopup, WarningPopup
from receipt_html import receipt_table, receipt_data_header, receipt_data
from load_ui import LoadUi
import webbrowser


class WindowOperator:
    def __init__(self, language:str) -> None:
        self._language = language
        self.db_manager = DataManager("table.db", language)
        self.question_box:QuestionPopup = QuestionPopup(self._language)
        self.warning_box:WarningPopup = WarningPopup(self._language)

    def reset_popup_language(self, language:str):
        self.question_box:QuestionPopup = QuestionPopup(language)
        self.warning_box:WarningPopup = WarningPopup(language)
        
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
        if '' in customer:
            self.warning_box.confirmation_dialog()
            return 0 
        accepted = self.db_manager.db_insert_customer(table, customer)
        if accepted:
            self.wipe_entered_data(entry_widget)

    def wipe_customer_window_data(self, window):
        answer = self.question_box.confirmation_dialog()
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
            if old.placeholderText() == "Registracija" or old.placeholderText() == "Registration":
                old.setInputMask("NNN-N-NNN")
            if old.placeholderText() == "Telefon" or old.placeholderText() == "Phone Number":
                old.setInputMask("999-999-999")
            if old.placeholderText() == "Cijena" or old.placeholderText() == "Price":
                old.setValidator(QDoubleValidator())
            if old.placeholderText() == "Količina" or old.placeholderText() == "Amount":
                old.setValidator(QDoubleValidator())
            if old.placeholderText() == "Rad" or old.placeholderText() == "Work":
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
        checkbox:QCheckBox = widget.archive_checkbox
        archived:bool = checkbox.isChecked()
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
        if query_string == "":
            query_string = f"WHERE archived = {int(archived)}"
        else:
            query_string = "WHERE (" + query_string[:-4] + f") AND (archived = {int(archived)})"
        self.db_manager.search_customers_populate_table(
            table, table_widget, tuple(search_param), query_string
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
            self.warning_box.confirmation_dialog()
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
        if (
            materials_input.text() == ""
            or brand_input.text() == ""
            or price_input.text() == ""
            or amount_input.text() == ""
        ):
            self.warning_box.confirmation_dialog()
            return
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
        answer = self.question_box.confirmation_dialog()
        if answer:
            self.wipe_entered_data(form.material_fields_frame)
            self.wipe_entered_data(form.table_service_frame)
            self.hide_customer_form(
                form.user_data_frame, form.add_new_reciept_frame, form
            )

    def add_new_receipt(self, form):
        answer = self.question_box.confirmation_dialog()
        if answer:
            table: QTableWidget = form.materials_receipt_table
            full_parts_price = 0
            for row in range(table.rowCount() - 1):
                full_parts_price += float(table.item(row, 4).text())

            if (
                table.item(0, 0) is None and table.rowCount() <= 1
            ) or form.add_receipt_service.text() == "":
                self.warning_box.set_warning(
                    "Niste unijeli materijal ili cijenu servisa u predračun!"
                )
                self.warning_box.confirmation_dialog()
                return
            reciept_data = [
                form.id_text_data.text(),
                form.add_receipt_service.text(),
                str(full_parts_price + int(form.add_receipt_service.text())),
            ]
            receipt_id = self.db_manager.add_receipt_to_database(reciept_data)
            for row in range(table.rowCount() - 1):
                materials_data = [
                    receipt_id,
                    table.item(row, 0).text(),
                    table.item(row, 1).text(),
                    table.item(row, 2).text(),
                    table.item(row, 3).text(),
                    table.item(row, 4).text(),
                ]
                self.db_manager.add_materials_to_database(materials_data)
            self.wipe_entered_data(form.material_fields_frame)
            self.wipe_entered_data(form.table_service_frame)
            self.hide_customer_form(
                form.user_data_frame, form.add_new_reciept_frame, form
            )

    def delete_selected_reciept(self, form):
        answer = self.question_box.confirmation_dialog_warning()
        if answer:
            reciepts_table: QTableWidget = form.customer_reciepts_table
            if (
                reciepts_table.selectedItems() != []
                and reciepts_table.selectedItems() is not None
            ):
                selected = reciepts_table.selectedItems()[0]
                self.db_manager.delete_reciept_from_database(selected.text())
                reciepts_table.removeRow(reciepts_table.currentRow())
            else:
                self.warning_box.confirmation_dialog()

    def select_reciept_from_table(self, form, receipt_form, receipt_window):
        customer_reciepts_table: QTableWidget = form.customer_reciepts_table
        receipt_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        receipt_window.showFullScreen()
        receipt_window.show()
        receipt_data = self.db_manager.get_selected_reciept_from_database(
            customer_reciepts_table.selectedItems()[0].text()
        )
        materials_table: QTableWidget = receipt_form.materials_receipt_table
        service: QLabel = receipt_form.service_text_label
        full_price: QLabel = receipt_form.full_price_label

        materials_table.clearContents()
        materials_table.setRowCount(0)

        for index, item in enumerate(receipt_data[1]):
            materials_table.insertRow(index)
            materials_table.setItem(index, 0, QTableWidgetItem(f"{item[0]}"))
            materials_table.setItem(index, 1, QTableWidgetItem(f"{item[2]}"))
            materials_table.setItem(index, 2, QTableWidgetItem(f"{item[3]}"))
            materials_table.setItem(index, 3, QTableWidgetItem(f"{item[5]}"))
            materials_table.setItem(index, 4, QTableWidgetItem(f"{item[4]}"))
            materials_table.setItem(index, 5, QTableWidgetItem(f"{item[6]}"))

        service.setText(f"{receipt_data[0][0][2]}")
        full_price.setText(f"{receipt_data[0][0][3]}")

    def open_browser_for_print(
        self, user_data: dict, selected_receipt: list, table_items: QTableWidget
    ):
        service: str = selected_receipt[3].text()
        total_price: str = selected_receipt[2].text()
        final_price: str = selected_receipt[4].text()
        customer_name: str = user_data["name"]
        customer_car: str = user_data["vehicle"]
        customer_plates: str = user_data["plates"]
        to_browser: str = receipt_data_header
        temp: str = ""

        for i in range(table_items.rowCount()):
            temp += receipt_data.format(
                material=table_items.item(i, 1).text(),
                model=table_items.item(i, 2).text(),
                price=table_items.item(i, 3).text(),
                amount=table_items.item(i, 4).text(),
                final_price=table_items.item(i, 5).text(),
            )
            temp += "\n"

        to_browser = to_browser.format(materials=temp)

        with open("data.html", "w", encoding="utf-8") as html_form:
            html_form.write(
                receipt_table.format(
                    todays_date=datetime.date.today().strftime("%d.%m.%Y.g."),
                    customer_name=customer_name,
                    customer_car=customer_car,
                    customer_reg=customer_plates,
                    work_price=service,
                    total_price=total_price,
                    final_price=final_price,
                    to_browser=to_browser,
                )
            )

        webbrowser.open("data.html", 1)

    def populate_customer_table_archived(self,db_table:str, table_widget:QTableWidget):
        rows = self.db_manager.get_archived_entries(db_table)

        table_widget.clearContents()
        table_widget.setRowCount(1)

        for index, row in enumerate(rows):
            temp = ""
            table_widget.setItem(index, 0, QTableWidgetItem(row[1]))
            table_widget.setItem(index, 1, QTableWidgetItem(row[2]))
            table_widget.setItem(index, 2, QTableWidgetItem(row[3]))
            table_widget.setItem(index, 3, QTableWidgetItem(row[4]))
            if int(row[0]) < 10:
                temp = "0000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 100:
                temp = "000" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 1000:
                temp = "00" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            elif int(row[0]) < 10000:
                temp = "0" + str(row[0])
                table_widget.setItem(index, 4, QTableWidgetItem(temp))
            else:
                table_widget.setItem(index, 4, QTableWidgetItem(f"{row[0]}"))
            table_widget.insertRow(index + 1)

    def change_customer_archive_status(self, form_widget):
        answer = self.question_box.confirmation_dialog()
        if answer:
            table_widget:QTableWidget = form_widget.customer_table
            if table_widget.selectedItems() != []:
                self.db_manager.change_archive_status(table_widget.selectedItems()[4].text().lstrip('0'))
            else:
                self.warning_box.confirmation_dialog()
    
    def cancel_receipt_printing(self, receipt_window:QDialog, form, table):
        answer = self.question_box.confirmation_dialog()
        
        if answer:
            customer_reciepts:QTableWidget = form.customer_reciepts_table
            selected_customer = customer_reciepts.selectedItems()[0].row()
            receipt_window.close()
            self.select_customer_from_table(form, table)
            customer_reciepts.selectRow(selected_customer)
            
    def delete_entry_from_receipt(self, reciept_table:QTableWidget, form, form_table:QTableWidget):
        answer = self.question_box.confirmation_dialog_warning()
        if answer:
            if reciept_table.selectedItems() != []:
                customer_reciepts:QTableWidget = form.customer_reciepts_table
                selected_customer = customer_reciepts.selectedItems()[0].row()
                reciept_table.selectRow(reciept_table.currentRow())
                selected_row = reciept_table.selectedItems()[0].text()
                reciept_table.removeRow(reciept_table.currentRow())
                self.db_manager.delete_selected_material(selected_row)
                self.select_customer_from_table(form, form_table)
                self.db_manager.update_selected_reciept_entry(reciept_table)
                customer_reciepts.selectRow(selected_customer)
            else:
                self.warning_box.confirmation_dialog()

    def close_application(self, app:QApplication):
        answer = self.question_box.confirmation_dialog()
        
        if answer:
            app.quit()
            
    def modify_receipt_entry(self, reciept_table: QTableWidget, form, form_table:QTableWidget):
        answer = self.question_box.confirmation_dialog()
        
        if answer:
            difference = self.db_manager.update_selected_reciept_entry(reciept_table)
            customer_reciepts:QTableWidget = form.customer_reciepts_table
            selected_customer = customer_reciepts.selectedItems()[0].row()
            self.select_customer_from_table(form, form_table)
            customer_reciepts.selectRow(selected_customer)
            if not difference:
                self.warning_box.confirmation_dialog()
            
    def open_settings(self, settingsForm, settingsWindow):
        settingsWindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        settingsWindow.show()
    
    def cancel_settings(self, settingsForm, settingsWindow):
        answer = self.question_box.confirmation_dialog()
        if answer:
            settingsWindow.close()
            
    def save_settings(self, settingsForm, ui_loader:LoadUi):
        answer = self.question_box.confirmation_dialog()
        if answer:
            language_box: QComboBox = settingsForm.language_combo
            screen_checkbox: QCheckBox = settingsForm.full_screen_check
            temp=""
            check=False
            with open("settings.cfg", "r", encoding="utf-8") as settings_config:
                temp = settings_config.read()
                settings_config.seek(0)
                language_setting = settings_config.readlines()[0].removeprefix("language=").strip().lower()
                settings_config.seek(0)
                screen_size = settings_config.readlines()[1].removeprefix("fullscreen=").strip().lower()
                selected_language = language_box.currentText().lower().strip()
                screen_check = screen_checkbox.isChecked()
                if selected_language == "engleski":
                    selected_language = "english"
                if selected_language != language_setting:
                    temp = temp.replace(language_setting, selected_language)
                if screen_size != screen_check:
                    temp_num = int(screen_check)
                    temp = temp.replace(screen_size, str(temp_num))
                    check = screen_check
                
            with open("settings.cfg", "w", encoding="utf-8") as settings_config:
                settings_config.write(temp)
            ui_loader.change_language(selected_language)
            ui_loader.change_screen_size(check)
            self.reset_popup_language(selected_language)