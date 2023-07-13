class Material:
    def __init__(self) -> None:
        self.type:str
        self.brand:str
        self.amount:int
        self.price:int

    def set_data(self, type:str, brand:str, amount:int, price:int):
        self.type = type
        self.brand = brand
        self.amount = amount
        self.price = price
        
    def get_data(self):
        return {
            'type': self.type,
            'brand': self.brand,
            'amout': self.amount,
            'price': self.price
        }

class Reciept:
    def __init__(self) -> None:
        self.id:int
        self.customer:int
        self.material = Material()
        self.full_amount:float
        self.service:float
        self.full_price:float
    
    def get_data(self):
        return [
        self.id,
        self.customer,
        self.material.get_data(),
        self.full_amount,
        self.service,
        self.full_price
        ]

    def set_data(self, reciept_data:list):
        self.customer = reciept_data[1]
        self.material.set_data(reciept_data[2], reciept_data[3], reciept_data[4], reciept_data[5])
        self.full_amount = reciept_data[6]
        self.service = reciept_data[7]
        self.full_price = reciept_data[8]