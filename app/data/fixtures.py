from datetime import date
from datetime import timedelta
from datetime import datetime

from app.services.db import session

from app.services import client as client_service
from app.services import component as component_service
from app.services import medicine as medicine_service
from app.services import critical_norm as cn_service
from app.services import ingredient as ingredient_service
from app.services import recipe as recipe_service
from app.services import order as order_service
from app.lib.enums import MedicineType
from app.lib.enums import CookingMethod
from app.lib.enums import ConsumptionType
from app.model import Order


water = component_service.create_component('water', 100.0, 1000.0)
herbs = component_service.create_component('herbs', 105.0, 1500.0)
salt = component_service.create_component('salt', 50.0, 1000.0)
sugar = component_service.create_component('sugar', 76.5, 1800.0)
alcohol = component_service.create_component('alcohol', 300.0, 1300.0)
oil = component_service.create_component('oil', 100.0, 90.0)

ing_water = ingredient_service.add_ingredient(water.id, 100)
ing_herbs = ingredient_service.add_ingredient(herbs.id, 150)
ing_salt = ingredient_service.add_ingredient(salt.id, 100)
ing_sugar = ingredient_service.add_ingredient(sugar.id, 180)
ing_alcohol = ingredient_service.add_ingredient(alcohol.id, 130)

cn_service.create_critical_norm(water.id, 100)
cn_service.create_critical_norm(herbs.id, 150)
cn_service.create_critical_norm(salt.id, 100)
cn_service.create_critical_norm(sugar.id, 180)
cn_service.create_critical_norm(alcohol.id, 130)
cn_service.create_critical_norm(oil.id, 100.0)


cl1 = client_service.create_client(
    first_name='Funny',
    last_name='Valentine',
    phone='+380507777777',
    address='Novikova 11, 202',
    age=48,
)

cl2 = client_service.create_client(
    first_name='Gyro',
    last_name='Zeppeli',
    phone='+380506666666',
    address='Novikova 13, 2',
    age=24,
)

cl3 = client_service.create_client(
    first_name='Hot',
    last_name='Pants',
    phone='+380505555555',
    address='Kosmonavtov 3, 14',
    age=23,
)


m1 = medicine_service.create_medicine(
    'brilliant green',
    date(year=2021, month=12, day=22),
    200.0,
    50.0,
    MedicineType.liquor,
    CookingMethod.creaming,
    [ing_water.id, ing_herbs.id]
)

m2 = medicine_service.create_medicine(
    'pills not for kids',
    date(year=2022, month=12, day=22),
    1000.0,
    10000.0,
    MedicineType.pill,
    CookingMethod.mixing,
    [ing_sugar.id, ing_herbs.id, ing_alcohol.id]
)

m3 = medicine_service.create_medicine(
    'doctor mom',
    date(year=2022, month=10, day=1),
    1000.0,
    40.0,
    MedicineType.ointment,
    CookingMethod.creaming,
    [ing_salt.id, ing_water.id, ing_herbs.id],
)

r1 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl1.id,
    'cancer',
    3.0,
    ConsumptionType.external,
    'brilliant green'
)

r2 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl2.id,
    'flu',
    15.0,
    ConsumptionType.internal,
    'pills not for kids'
)

r3 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl3.id,
    'flu',
    2.0,
    ConsumptionType.external,
    'doctor mom'
)

r4 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl1.id,
    'flu',
    2.0,
    ConsumptionType.external,
    'doctor mom'
)


or1 = order_service.create_order(r1.id, m2.id, datetime.strptime('21-06-21', '%d-%m-%y'))
or2 = order_service.create_order(r2.id, m2.id, datetime.strptime('31-05-21', '%d-%m-%y'))
or3 = order_service.create_order(r3.id, m3.id, datetime.strptime('29-05-21', '%d-%m-%y'))
or4 = order_service.create_order(r4.id, m3.id, datetime.strptime('21-09-21', '%d-%m-%y'))
session.commit()


