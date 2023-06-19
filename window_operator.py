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