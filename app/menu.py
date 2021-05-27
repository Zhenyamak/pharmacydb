from app.services.db import session

from app.services import client as client_service
from app.services import component as component_service
from app.services import medicine as medicine_service
from app.services import critical_norm as cn_service
from app.services import ingredient as ingredient_service
from app.services import cooking_book as cb_service
from app.services import recipe as recipe_service
from app.services import order as order_service
from app.services import supply_request as sr
from app.lib import query as q


def menu(request):
    ingredient_service.add_ingredient
    ingredient_service.get_ingredient_by_id
    ingredient_service.set_ingredient_dose
    client_service.create_client
    client_service.get_client_by_id
    medicine_service.create_medicine
    medicine_service.get_medicine_by_name
    cn_service.create_critical_norm
    cb_service.create_cooking_book
    component_service.create_component
    component_service.get_ingredient_by_id
    component_service.set_ingredient_amount
    recipe_service.create_recipe
    recipe_service.set_order_id
    recipe_service.set_ready_time
    order_service.create_order
    order_service.get_order_by_id
    sr.create_supply_request
    q.get_clients_with_not_taken_orders
    q.get_clients_waiting_for_ingredients
    q.get_top_ten_most_used_medicines
    q.get_component_used_amount
    q.get_client_by_ordered_medicine_type
    q.get_medicine_with_minimal_components_amount
    q.get_orders_amount_in_process_status
    q.get_cooking_book_for_medicine_name
    q.get_cooking_book_for_medicine_type
    q.get_cooking_book_for_orders_in_process
    q.get_price_for_medicine
    q.get_component_price_for_medicine
    q.get_full_medicine_info
    # перед каждой функцией надо слово для вызова в кавычках
    if request is None:
        print("Unknown command")

def help():
    print("""You are using pharmacy database 
                 You can enter:
                 
                 Help - (but you are here)
                 End - to close the program""")# сюда(после You can enter)  надо вставить все вот те команды сверху(ну и которые добавишь)
def End():
    from sys import exit
    print("Program stopped working")
    exit()

