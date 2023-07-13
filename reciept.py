class Reciept:
    def __init__(self) -> None:
        self.id: int
        self.customer: int
        self.material:str
        self.service: float
        self.full_price: float

    def get_data(self):
        return [
            self.id,
            self.customer,
            self.material,
            self.service,
            self.full_price,
        ]

    def set_data(self, reciept_data: list):
        self.id = reciept_data[0]
        self.customer = reciept_data[1]
        self.material = reciept_data[2]
        self.service = reciept_data[3]
        self.full_price = reciept_data[4]
