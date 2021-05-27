from datetime import date

from app.model import Order
from app.model import Recipe
from app.model import Medicine
from app.lib.enums import OrderStatus
from app.services import supply_request as sr_service
from app.services.db import session


def create_order(
    recipe: Recipe,
    medicine: Medicine,
    ready_time: date,
) -> Order:
    order = Order(
        client_id=recipe.client_id,
        medicine_id=medicine.id,
        status=OrderStatus.in_process
    )
    for ingredient in medicine.ingredients:
        component = ingredient.component

        if ingredient.dose > component.amount:
            sr_service.create_supply_request(component.id, recipe.client_id)
            order.status = OrderStatus.waiting_for_components

    recipe.order_id = order.id
    recipe.ready_time = ready_time
    session.add_all([recipe, order])
    session.commit()

    return order
