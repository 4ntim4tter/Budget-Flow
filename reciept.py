class Material:
    def __init__(self) -> None:
        self.data: list = []

    def set_data(self, type: str, brand: str, amount: int, price: int):
        self.data.append(
            {"type": type, "brand": brand, "amount": amount, "price": price}
        )

    def get_data(self):
        return self.data


class Reciept:
    def __init__(self) -> None:
        self.id: int
        self.customer: int
        self.material = Material()
        self.service: float
        self.full_price: float

    def get_data(self):
        return [
            self.id,
            self.customer,
            self.material.get_data(),
            self.service,
            self.full_price,
        ]

    def set_data(self, reciept_data: list):
        self.id = reciept_data[0]
        self.customer = reciept_data[1]
        self.material = reciept_data[2]
        self.service = reciept_data[3]
        self.full_price = reciept_data[4]
