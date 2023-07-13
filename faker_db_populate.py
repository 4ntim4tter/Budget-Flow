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

for _ in range(80):
    customer_id_query = "SELECT id FROM customers ORDER BY RANDOM() LIMIT 1"  
    cursor.execute(customer_id_query)
    customer_id = cursor.fetchone()[0]
    fake_material = [fake.word(), fake.word()]
    full_amount = randint(50,100)
    service = randint(50, 100)
    full_price = full_amount + service
    cursor.execute(
        "INSERT INTO receipts (customer_id, material, service, full_price) VALUES (?, ?, ?, ?)",
        (customer_id, str(fake_material), service, full_price),
        )
db_connection.commit()

for i in range(1, 80):
    reciept_id_query = f"SELECT id FROM receipts WHERE id = {i}"
    cursor.execute(reciept_id_query)
    reciept_id = cursor.fetchall()
    for _ in range(randint(2,5)):
        type = fake.word()
        brand = fake.word()
        amount = randint(1,5)
        price = randint(5,70)
        full_amount = amount * price
        cursor.execute(
            "INSERT INTO materials ('reciept_id', 'type', 'brand', 'amount', 'price', 'full_amount') VALUES (?, ?, ?, ?, ?, ?)",
            (reciept_id[0][0], type, brand, amount, price, full_amount),
            )
db_connection.commit()

# cursor.execute("SELECT * FROM receipts")
# all = cursor.fetchall()
# for item in all:
#     cursor.execute(
#         f"SELECT type FROM materials WHERE reciept_id = {item[0]}"
#     )
#     reciept_materials = cursor.fetchall()
#     print(reciept_materials)

db_connection.commit()
db_connection.close()
