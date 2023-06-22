from customer import Customer


class WindowOperator():
    def __init__(self) -> None:
        pass

    def window_visibility(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()
    
    def hide_opened(self, widget):
        for item in widget:
            if hasattr(item, 'hide'):
                item.hide()

    def get_customer_values(self, form):
        customer = Customer(form.add_customer_name.text(), 
                            form.add_customer_surname.text(), 
                            form.add_customer_phone.text(), 
                            form.add_customer_vehicle.text(), 
                            form.add_customer_plates.text(), 
                            form.add_customer_chasis.text())

        return customer.get_data()
    
    def line_focus_changed(self, new, old):
        placeholder_text = ''
        inputMask = ''
        if old is not None and hasattr(old, 'placeholderText'):
            placeholder_text = old.placeholderText()
            inputMask = old.inputMask()

            if old.placeholderText() == 'Registracija':
                old.setInputMask('NNN-N-NNN')

            if old.placeholderText() == 'Telefon':
                old.setInputMask('999-999-999')

