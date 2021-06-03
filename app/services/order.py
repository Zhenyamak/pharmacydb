from typing import Optional
from datetime import date
import warnings
from sqlalchemy import exc as sa_exc

from app.model import Order
from app.model import Recipe
from app.model import Medicine
from app.lib.enums import OrderStatus
from app.services import supply_request as sr_service
from app.services.db import session
from app.services.component import set_component_amount


def create_order(
    recipe_id: int,
    medicine_id: int,
    ready_time: date,
) -> Optional[Order]:
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    medicine = session.query(Medicine).filter(
        Medicine.id == medicine_id).first()
    if not (recipe and medicine):
        return None
    order = Order(
        client_id=recipe.client_id,
        medicine_id=medicine.id,
        status=OrderStatus.in_process,
        ready_time = ready_time
    )
    for ingredient in medicine.ingredients:
        component = ingredient.component

        if recipe.amount * ingredient.dose > component.amount:
            sr_service.create_supply_request(component.id, recipe.client_id)
            order.status = OrderStatus.waiting_for_components
        else:
            set_component_amount(component.id, (component.amount-recipe.amount * ingredient.dose))
    session.add(order)
    session.commit()
    recipe.order_id = order.id
    session.add(recipe)
    session.commit()

    return order


def set_ready_time(id_: int, ready_time: date):
    session.query(Order).filter(Order.id == id_).update(
        {'ready_time': ready_time}
    )
    session.commit()


def take_order(order_id: int):
    session.query(Order)\
        .filter(Order.id == order_id) \
        .filter(Order.status == Order.STATUSES.ready)\
        .update({'status': Order.STATUSES.closed})
    session.commit()


def check_readiness():
    session.query(Order) \
        .filter(Order.status == Order.STATUSES.in_process)\
        .filter(Order.ready_time <= date.today())\
        .update({'status': Order.STATUSES.ready})
    session.commit()
