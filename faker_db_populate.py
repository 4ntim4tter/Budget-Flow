from random import randint
import sqlite3
from faker import Faker
from faker_vehicle import VehicleProvider

db_connection = sqlite3.connect("table.db")
cursor = db_connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS customers")
# cursor.execute("DROP TABLE IF EXISTS receipts")
# cursor.execute("DROP TABLE IF EXISTS materials")

fake = Faker()
fake.add_provider(VehicleProvider)

#customer
for _ in range(20):
    name = fake.first_name()
    surname = fake.last_name()
    phone = fake.bothify(text="###-###-###")
    vehicle = fake.vehicle_model()
    plates = fake.bothify(text="###-#-???")
    chasis = fake.bothify(text="???###?##??#?#?#??#")
    cursor.execute(
        "INSERT INTO customers (name, surname, phone, vehicle, plates, chasis) VALUES (?, ?, ?, ?, ?, ?)",
        (name, surname, phone, vehicle, plates, chasis),
    )
db_connection.commit()

#receipts
for _ in range(80):
    customer_id_query = "SELECT id FROM customers ORDER BY RANDOM() LIMIT 1"
    cursor.execute(customer_id_query)
    customer_id = cursor.fetchone()[0]
    service = randint(50, 100)
    cursor.execute(
        "INSERT INTO receipts (customer_id, service) VALUES (?, ?)",
        (customer_id, service),
    )
db_connection.commit()

#materials
for i in range(1, 81):
    reciept_id_query = f"SELECT id FROM receipts WHERE id = {i}"
    reciept_service_query = f"SELECT service FROM receipts WHERE id = {i}"
    customer_id_query = "SELECT id FROM customers ORDER BY RANDOM() LIMIT 1"
    cursor.execute(customer_id_query)
    customer_id = cursor.fetchone()[0]
    cursor.execute(reciept_id_query)
    reciept_id = cursor.fetchall()
    cursor.execute(reciept_service_query)
    receipt_service = cursor.fetchone()
    full_price = 0
    for _ in range(randint(2, 5)):
        type = fake.word()
        brand = fake.word()
        amount = randint(1, 5)
        price = randint(5, 70)
        full_amount = amount * price
        full_price += full_amount
        cursor.execute(
            "INSERT INTO materials ('reciept_id', 'type', 'brand', 'amount', 'price', 'full_amount') VALUES (?, ?, ?, ?, ?, ?)",
            (reciept_id[0][0], type, brand, amount, price, full_amount),
        )
    cursor.execute(
        f"UPDATE receipts SET full_price = ? WHERE id = {i}", (full_price+receipt_service[0],))
        
db_connection.commit()
db_connection.close()
