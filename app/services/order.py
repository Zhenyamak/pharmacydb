from typing import Optional
from datetime import date

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
        status=OrderStatus.in_process
    )
    for ingredient in medicine.ingredients:
        component = ingredient.component

        if ingredient.dose > component.amount:
            sr_service.create_supply_request(component.id, recipe.client_id)
            order.status = OrderStatus.waiting_for_components
        else:
            set_component_amount(component.id, (component.amount-ingredient.dose))
    recipe.order_id = order.id
    recipe.ready_time = ready_time
    session.add_all([recipe, order])
    session.commit()

    return order
