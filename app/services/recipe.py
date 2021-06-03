from typing import Optional
from datetime import date

from app.model import Client
from app.model import Recipe
from app.model import Medicine
from app.services.db import session
from app.lib.enums import ConsumptionType


def create_recipe(
    doctor: str,
    client_id: int,
    diagnosis: str,
    amount: float,
    consumption_type: ConsumptionType,
    medicine_name: str,
    order_id: Optional[int] = None,
) -> Recipe:
    client = session.query(Client).filter(Client.id == client_id).first()
    if not client:
        return None
    recipe = Recipe(
        doctor=doctor,
        client_id=client_id,
        diagnosis=diagnosis,
        amount=amount,
        consumption_type=consumption_type,
        order_id=order_id,
        medicine_name=medicine_name,
    )
    session.add(recipe)
    session.commit()
    return recipe


def delete_recipe(order_id: int):
    session.query(Recipe).filter(Recipe.order_id == order_id) \
        .delete()
    session.commit()
