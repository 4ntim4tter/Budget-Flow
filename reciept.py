class Reciept:
    def __init__(
        self,
        id: int,
        customer: str,
        material: str,
        brand: str,
        price: float,
        amount: float,
        full_amount: float,
        service: float,
        full_price: float,
    ) -> None:
        self.id = id
        self.customer = customer
        self.material = material
        self.brand = brand
        self.price = price
        self.amount = amount
        self.full_amount = full_amount
        self.service = service
        self.full_price = full_price
    
    def get_receipt(self):
        return [
        self.id,
        self.customer,
        self.material,
        self.brand,
        self.price,
        self.amount,
        self.full_amount,
        self.service,
        self.full_price
        ]
