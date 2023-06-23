from PyQt6.QtWidgets import QLineEdit
from customer import Customer


class WindowOperator():
    def __init__(self) -> None:
        pass

    def window_visibility(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()
            widgets = widget.children()
            for child in widgets:
                if isinstance(child, QLineEdit):
                    child.setText('')
        
    def hide_opened(self, widget):
        for item in widget:
            if hasattr(item, 'hide'):
                item.hide()

    def get_customer_values(self, widget):
        customer = Customer(widget.add_customer_name.text(), 
                            widget.add_customer_surname.text(), 
                            widget.add_customer_phone.text(), 
                            widget.add_customer_vehicle.text(), 
                            widget.add_customer_plates.text(), 
                            widget.add_customer_chasis.text())

        return customer.get_data()
    
    def line_focus_changed(self, new, old):
        if old is not None and hasattr(old, 'placeholderText'):
            if old.placeholderText() == 'Registracija':
                old.setInputMask('NNN-N-NNN')
            if old.placeholderText() == 'Telefon':
                old.setInputMask('999-999-999')
