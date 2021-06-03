from app.services.db import engine
from sqlalchemy import text


def create_client_table():
    sql = text("""CREATE TABLE IF NOT EXISTS client (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(60), 
    last_name VARCHAR(60), 
    phone VARCHAR(20), 
    address VARCHAR(120), 
    age SMALLINT, 
    PRIMARY KEY (id)
)""")
    engine.execute(sql)


def create_component_table():
    sql = text("""CREATE TABLE IF NOT EXISTS component (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(120), 
    price FLOAT, 
    amount FLOAT, 
    PRIMARY KEY (id), 
    UNIQUE (name), 
    UNIQUE (name)
)""")
    engine.execute(sql)


def create_medicine_table():
    sql = text("""CREATE TABLE IF NOT EXISTS medicine (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(120), 
    storage_time DATE, 
    amount FLOAT, 
    price FLOAT, 
    type ENUM('pill','ointment','tincture','mixture','liquor','powder'), 
    PRIMARY KEY (id), 
    UNIQUE (name), 
    UNIQUE (name)
)""")
    engine.execute(sql)


def create_cooking_book_table():
    sql = text("""CREATE TABLE IF NOT EXISTS cooking_book (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    medicine_id INTEGER, 
    method ENUM('mixing','creaming'), 
    PRIMARY KEY (id), 
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_critical_norm_table():
    sql = text("""CREATE TABLE IF NOT EXISTS critical_norm (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    amount FLOAT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_ingredient_table():
    sql = text("""CREATE TABLE IF NOT EXISTS ingredient (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    dose FLOAT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_orders_table():
    sql = text("""CREATE TABLE IF NOT EXISTS orders (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    `status` ENUM('in_process','waiting_for_components','ready','closed') NOT NULL, 
    client_id INTEGER, 
    medicine_id INTEGER, 
    date_created DATE NOT NULL, 
    ready_time DATE,
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE, 
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_supply_request_table():
    sql = text("""CREATE TABLE IF NOT EXISTS supply_request (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    client_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE, 
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_ingredient_medicine_table():
    sql = text("""CREATE TABLE IF NOT EXISTS ingredient_medicine (
    ingredient_id INTEGER, 
    medicine_id INTEGER, 
    FOREIGN KEY(ingredient_id) REFERENCES ingredient (id) ON DELETE CASCADE, 
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_recipe_table():
    sql = text("""CREATE TABLE IF NOT EXISTS recipe (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    medicine_name VARCHAR(120), 
    doctor VARCHAR(255), 
    client_id INTEGER, 
    diagnosis VARCHAR(255), 
    amount FLOAT, 
    consumption_type ENUM('internal','external','mixing'),  
    order_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE,
    FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE CASCADE
)""")
    engine.execute(sql)


def create_all_tables():
    create_client_table()
    create_component_table()
    create_medicine_table()
    create_cooking_book_table()
    create_critical_norm_table()
    create_ingredient_table()
    create_orders_table()
    create_supply_request_table()
    create_ingredient_medicine_table()
    create_recipe_table()


def full_drop():
    engine.execute(text("""SET FOREIGN_KEY_CHECKS=0"""))
    engine.execute(text("""drop table if exists client cascade"""))
    engine.execute(text("""drop table if exists component cascade"""))
    engine.execute(text("""drop table if exists medicine cascade"""))
    engine.execute(text("""drop table if exists ingredient cascade"""))
    engine.execute(text("""drop table if exists orders cascade"""))
    engine.execute(text("""drop table if exists cooking_book"""))
    engine.execute(text("""drop table if exists critical_norm"""))
    engine.execute(text("""drop table if exists supply_request"""))
    engine.execute(text("""drop table if exists ingredient_medicine"""))
    engine.execute(text("""drop table if exists recipe"""))
    engine.execute(text("""SET FOREIGN_KEY_CHECKS=1"""))
