from sys import exit
from app.model import *

from app.services.db import session

from app.services import component as component_service
from app.services import client as client_service
from app.services import ingredient as ingredient_service
from app.services import critical_norm as cn_service
from app.services import medicine as medicine_service
from app.services import order as order_service
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
        component_id = int(input('Enter component id'))
    except (ValueError, TypeError):
        print('Wrong component id')
        return
    try:
        dose = int(input('Enter amount'))
    except (ValueError, TypeError):
        print('Wrong amount')
        return
    ingredient = ingredient_service.add_ingredient(
        component_id=component_id,
        dose=dose
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


def create_recipe_handler():
    doctor = input('Enter doctor')
    client_id = input('Enter client id')

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


# 1
def get_clients_with_not_taken_orders_handler():
    res = q.get_clients_with_not_taken_orders()
    for item in res:
        print(item)


# 2
def get_clients_waiting_for_ingredients_handler():
    res = q.get_clients_waiting_for_ingredients()
    for item in res:
        print(item)


# 3
def get_top_ten_most_used_medicines_handler():
    res = q.get_top_ten_most_used_medicines()
    for item in res:
        print(item)


# 6
def get_components_with_critical_norm_handler():
    res = q.get_components_with_critical_norm()
    for item in res:
        print(item)


# 7
def get_medicine_with_minimal_components_amount_handler():
    type_ = input('Enter type')
    print(q.get_medicine_with_minimal_components_amount(type_))


# 8
def get_orders_amount_in_process_status_handler():
    res = q.get_orders_amount_in_process_status()
    for item in res:
        print(item)


# 9
def get_medicine_in_waiting_for_components_status_handler():
    res = q.get_medicine_in_waiting_for_components_status()
    for item in res:
        print(item)


# 10
def get_cooking_book_for_medicine_name_handler():
    name = input('Enter name')
    print(q.get_cooking_book_for_medicine_name(name))


def get_cooking_book_for_medicine_type_handler():
    type_ = input('Enter type')
    print(q.get_cooking_book_for_medicine_type(type_))


# 11
def get_price_for_medicine_handler():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    print(q.get_price_for_medicine(id_))


def get_component_price_for_medicine_handler():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    print(q.get_component_price_for_medicine(id_))


# 12
def get_orders_for_most_popular_medicine_handler():
    res = q.get_orders_for_most_popular_medicine()
    for item in res:
        print(item)


# 13
def get_full_medicine_info_handler():
    try:
        id_ = int(input('Enter id'))
    except (ValueError, TypeError):
        print('Error')
        return
    print(q.get_full_medicine_info(id_))


COMMANDS = {
    '------------ create commands ------------': 1,
    'create client': create_client_handler,
    'create component': create_component_handler,
    'create ingredient': create_ingredient_handler,
    'create medicine': create_medicine_handler,
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
    'get clients with not taken orders': get_clients_with_not_taken_orders_handler,  # 1
    'get clients waiting for ingredients': get_clients_waiting_for_ingredients_handler,  # 2
    'get top ten most used medicines': get_top_ten_most_used_medicines_handler,  # 3
    'get components with critical norm': get_components_with_critical_norm_handler,  # 6
    'get medicine with minimal components amount': get_medicine_with_minimal_components_amount_handler,  # 7 ?
    'get orders amount in process status': get_orders_amount_in_process_status_handler,  # 8
    'get medicine in waiting for components status': get_medicine_in_waiting_for_components_status_handler,  # 9
    'get cooking book for medicine name': get_cooking_book_for_medicine_name_handler,  # 10 ?
    'get cooking book for medicine type': get_cooking_book_for_medicine_type_handler,
    'get price for medicine': get_price_for_medicine_handler,  # 11
    'get component price for medicine': get_component_price_for_medicine_handler,
    'get orders for most popular medicine': get_orders_for_most_popular_medicine_handler,  # 12 ?
    'get full medicine info': get_full_medicine_info_handler,  # 13
    '------------ system commands ------------': 5,
    'exit': shut_down,
    'help': help_handler,
}


def print_available_handlers():
    for i in COMMANDS.keys():
        print(i)
