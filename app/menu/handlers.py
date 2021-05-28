from sys import exit
from app.model import *

from app.services.db import session

from app.services import component as component_service
from app.services import client as client_service
from app.services import ingredient as ingredient_service
from app.services import critical_norm as cn_service
from app.services import medicine as medicine_service
from app.services import order as order_service
from app.services import supply_request as sr_service
from app.services import recipe as recipe_service
from app.lib import query as q


def create_component_handler():
    name = input('Enter name')
    try:
        price = float(input('Enter price'))
    except (ValueError, TypeError):
        print('Wrong price')
        return
    try:
        amount = float(input('Enter amount'))
    except (ValueError, TypeError):
        print('Wrong amount')
        return
    component = component_service.create_component(
        name=name,
        price=price,
        amount=amount
    )
    print(component)


def create_client_handler():
    first_name = input('Enter first name')
    last_name = input('Enter last name')
    phone = input('Enter phone')
    address = input('Enter address')
    try:
        age = int(input('Enter age'))
    except (ValueError, TypeError):
        print('Wrong age')
        return
    client = client_service.create_client(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        age=age,
    )
    print(client)


def create_ingredient_handler():
    try:
        component_id = input('Enter component id')
    except (ValueError, TypeError):
        print('Wrong component id')
        return
    try:
        amount = input('Enter amount')
    except (ValueError, TypeError):
        print('Wrong amount')
        return
    ingredient = ingredient_service.add_ingredient(
        component_id=component_id,
        dose=amount,
    )
    print(ingredient)


def create_medicine_handler():
    name = input('Enter name')
    try:
        storage_time = input('Enter storage time')
    except (ValueError, TypeError):
        print('Wrong storage time')
        return
    try:
        amount = input('Enter amount')
    except (ValueError, TypeError):
        print('Wrong amount')
        return
    try:
        price = input('Enter price')
    except (ValueError, TypeError):
        print('Wrong price')
        return
    type = input('Enter type')
    medicine = medicine_service.create_medicine(
        name=name,
        storage_time=storage_time,
        amount=amount,
        price=price,
        type=type,
    )
    print(medicine)


def create_order_handler():
    recipe = input('Enter recipe')
    medicine = input('Enter medicine')
    try:
        ready_time = input('Enter ready time')
    except (ValueError, TypeError):
        print('Wrong ready time')
        return
    order = order_service.create_order(
        client_id=recipe.client_id,
        medicine_id=medicine.id,
        status=OrderStatus.in_process
    )
    print(order)


def create_supply_request_handler():
    component_id = input('Enter component id')
    client_id = input('Enter client id')
    supply_request = sr_service.create_supply_request(
        component_id=component_id,
        client_id=client_id,
    )
    print(supply_request)


def set_component_amount_handler():
    try:
        component_id = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    try:
        amount = int(input('Enter new amount'))
    except (ValueError, TypeError):
        print('Error')
        return
    component_service.set_component_amount(component_id, amount)


def set_critical_norm_handler():
    try:
        component_id = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    try:
        cn = int(input('Enter new critical norm'))
    except (ValueError, TypeError):
        print('Error')
        return
    cn_service.set_critical_norm(component_id, cn)


def set_ingredient_dose_handler():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    try:
        dose = int(input('Enter new dose'))
    except (ValueError, TypeError):
        print('Error')
        return
    ingredient_service.set_ingredient_dose(id_, dose)


def get_ingredient_by_id_handler():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    print(component_service.get_ingredient_by_id(id_))


def get_ingredient_by_id_handler_2():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    print(ingredient_service.get_ingredient_by_id(id_))


def get_by_name_handler():
    name = input('Enter name')
    print(medicine_service.get_by_name(name))


def get_all_components():
    res = session.query(Component).all()
    for item in res:
        print(item)


def get_all_clients():
    res = session.query(Client).all()
    for item in res:
        print(item)


def get_cooking_book():
    res = session.query(CookingBook).all()
    for item in res:
        print(item)


def get_critical_norm():
    res = session.query(CriticalNorm).all()
    for item in res:
        print(item)


def get_all_medicines():
    res = session.query(Medicine).all()
    for item in res:
        print(item)


def get_all_orders():
    res = session.query(Order).all()
    for item in res:
        print(item)


def shut_down():
    print("Bye")
    exit()


def help_handler():
    print("""You are using pharmacy database 
                You can enter:""")
    print_available_handlers()
    print("""""")


COMMANDS = {
    '------------ create commands ------------': 1,
    'create client': create_client_handler,
    'create component': create_component_handler,
    'create ingredient': create_ingredient_handler,
    'create medicine': create_medicine_handler,
    'create order': create_order_handler,
    'create supply request': create_supply_request_handler,
    '------------ set commands ------------': 2,
    'set component amount': set_component_amount_handler,
    'set ingredient dose': set_ingredient_dose_handler,
    'set critical norm': set_critical_norm_handler,
    '------------ get commands ------------': 3,
    'get ingredient by id': get_ingredient_by_id_handler,
    'get ingredient by id 2': get_ingredient_by_id_handler_2,
    'get by name medicine': get_by_name_handler,
    'get all components': get_all_components,
    'get all clients': get_all_clients,
    'get cooking book': get_cooking_book,
    'get critical norm': get_critical_norm,
    'get all medicines': get_all_medicines,
    'get all orders': get_all_orders,
    '------------ queries ------------': 4,
    'get_clients_with_not_taken_orders': q.get_clients_with_not_taken_orders,
    'get_clients_waiting_for_ingredients': q.get_clients_waiting_for_ingredients,
    'get_top_ten_most_used_medicines': q.get_top_ten_most_used_medicines,
    '------------ system commands ------------': 5,
    'exit': shut_down,
    'help': help_handler,
}


def print_available_handlers():
    for i in COMMANDS.keys():
        print(i)
