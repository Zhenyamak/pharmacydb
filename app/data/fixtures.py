from datetime import date
from datetime import timedelta

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
solt = component_service.create_component('solt', 50.0, 1000.0)
sugar = component_service.create_component('sugar', 76.5, 1800.0)
alcohol = component_service.create_component('alcohol', 300.0, 1300.0)

ing_water = ingredient_service.add_ingredient(water.id, 100.0)
ing_herbs = ingredient_service.add_ingredient(herbs.id, 150.0)
ing_solt = ingredient_service.add_ingredient(solt.id, 100.0)
ing_sugar = ingredient_service.add_ingredient(sugar.id, 180.0)
ing_alcohol = ingredient_service.add_ingredient(alcohol.id, 130.0)

cn_service.create_critical_norm(water.id, 100)
cn_service.create_critical_norm(herbs.id, 150)
cn_service.create_critical_norm(solt.id, 100)
cn_service.create_critical_norm(sugar.id, 180)
cn_service.create_critical_norm(alcohol.id, 130)


cl1 = client_service.create_client(
    first_name='first',
    last_name='first',
    phone='+380507777777',
    address='Novikova 11, 202',
    age=44,
)

cl2 = client_service.create_client(
    first_name='second',
    last_name='second',
    phone='+380506666666',
    address='Novikova 13, 2',
    age=15,
)

cl3 = client_service.create_client(
    first_name='third',
    last_name='third',
    phone='+380505555555',
    address='Kosmonavtov 3, 14',
    age=21,
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
    [ing_solt.id, ing_water.id, ing_herbs.id],
)


r1 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl1.id,
    'cancer',
    300.0,
    ConsumptionType.external,
    'brilliant green'
)

r2 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl2.id,
    'flu',
    150.0,
    ConsumptionType.internal,
    'pills not for kids'
)

r3 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl3.id,
    'flu',
    200.0,
    ConsumptionType.internal,
    'doctor mom'
)

r4 = recipe_service.create_recipe(
    'Doctor I Bolit',
    cl1.id,
    'flu',
    250.0,
    ConsumptionType.external,
    'doctor mom'
)



order_service.create_order(r1.id, m1.id, date.today() + timedelta(days=1))
order_service.create_order(r1.id, m1.id, date.today() + timedelta(days=2))
or1 = order_service.create_order(r2.id, m2.id, date.today() - timedelta(days=2))
or1.status = Order.STATUSES.ready
or2 = order_service.create_order(r3.id, m3.id, date.today() + timedelta(days=7))
or3 = order_service.create_order(r4.id, m3.id, date.today() + timedelta(days=3))
or3.status = Order.STATUSES.waiting_for_components
session.add_all([or1, or2, or3])
session.commit()

oil = component_service.create_component('oil', 100.0, 90.0)
cn_service.create_critical_norm(oil.id, 100.0)
