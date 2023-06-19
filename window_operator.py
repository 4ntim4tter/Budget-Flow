class WindowOperator():
    def __init__(self, window) -> None:
        self.window = window
    
    def window_visibility(self):
        if self.window.isHidden():
            self.window.show()
        else:
            self.window.hide()