import sqlite3
from faker import Faker
from faker_vehicle import VehicleProvider

db_connection = sqlite3.connect("table.db")
cursor = db_connection.cursor()

cursor.execute("DELETE FROM customers")

fake = Faker()
fake.add_provider(VehicleProvider)

for _ in range(20):
    name = fake.first_name()
    surname = fake.last_name()
    phone = fake.bothify(text="###-###-###")
    vehicle = fake.vehicle_model()
    plates = fake.bothify(text="###-#-???")
    chasis = fake.bothify(text="???###?##??#?#?#??#")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'customers'")
    cursor.execute(
        "INSERT INTO customers (name, surname, phone, vehicle, plates, chasis) VALUES (?, ?, ?, ?, ?, ?)",
        (name, surname, phone, vehicle, plates, chasis),
    )

db_connection.commit()
db_connection.close()
