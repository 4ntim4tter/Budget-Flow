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
        customer = []
        customer.append(form.add_customer_name.text())
        customer.append(form.add_customer_phone.text())
        customer.append(form.add_customer_surname.text())
        customer.append(form.add_customer_vehicle.text())
        customer.append(form.add_customer_plates.text())
        customer.append(form.add_customer_chasis.text())
        return customer