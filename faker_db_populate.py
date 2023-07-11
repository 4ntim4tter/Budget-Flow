from random import randint
import sqlite3
from faker import Faker
from faker_vehicle import VehicleProvider

db_connection = sqlite3.connect("table.db")
cursor = db_connection.cursor()

cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM receipts")

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

for _ in range(80):
    customer_id_query = "SELECT id FROM customers ORDER BY RANDOM() LIMIT 1"  
    cursor.execute(customer_id_query)
    customer_id = cursor.fetchone()[0]
    material = fake.word()
    brand = fake.word()
    price = randint(10, 150)
    amount = randint(1, 6)
    full_amount = price * amount
    service = randint(50, 100)
    full_price = full_amount + service
    cursor.execute ("DELETE FROM sqlite_sequence WHERE name = 'receipts'")
    cursor.execute(
        "INSERT INTO receipts (customer_id, material, brand, price, amount, full_amount, service, full_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (customer_id, material, brand, price, amount, full_amount, service, full_price),
        )
db_connection.commit()
db_connection.close()
