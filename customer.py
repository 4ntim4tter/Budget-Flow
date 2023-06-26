class Customer:
    def __init__(
        self,
        name: str,
        surname: str,
        phone: int,
        vehicle: str,
        registration: str,
        chasis: str,
    ) -> None:
        self.name = name
        self.surname = surname
        self.phone = phone
        self.vehicle = vehicle
        self.registration = registration
        self.chasis = chasis

    def get_data(self):
        return [
            self.name,
            self.surname,
            self.phone,
            self.vehicle,
            self.registration,
            self.chasis,
        ]
