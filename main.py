import os

from window_operator import WindowOperator
from database_management import DataManager
from load_ui import LoadUi


with open("settings.cfg", "+r", encoding="utf-8") as settings_config:
    if not os.path.isfile("settings.cfg"):
        settings_config.write(
            """language=english\nfullscreen=1"""
        )
    if settings_config.read() == "":
        settings_config.seek(0)
        print(settings_config.read())
        settings_config.write(
            """language=english\nfullscreen=1"""
        )
        
db_manager = DataManager("table.db")
entry_window = WindowOperator()

db_manager.db_connect("table.db")
db_manager.db_create_table(
    "customers",
    ["id", "name", "surname", "phone", "vehicle", "plates", "chasis", "archived"],
)
db_manager.db_create_table(
    "receipts",
    [
        "id",
        "customer_id",
        "service",
        "full_price",
    ],
)
db_manager.db_create_table(
    "materials", ["id", "reciept_id", "type", "brand", "amount", "price", "full_amount"]
)

with open("settings.cfg", "r", encoding="utf-8") as settings_config:
    if "english" in settings_config.readlines()[0]:
        language = "english"
    else:
        language = "bosnian"    
    
ui_loader = LoadUi(language, entry_window, db_manager)

if __name__ == "__main__":
    ui_loader.run()
