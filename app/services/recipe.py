from typing import Optional
from datetime import date

from app.model import Client
from app.model import Recipe
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
    ready_time: Optional[date] = None,
) -> Recipe:
    client = session.query(Client).filter(Client.id == client_id).exists()
    if not client:
        return None
    recipe = Recipe(
        doctor=doctor,
        client_id=client_id,
        diagnosis=diagnosis,
        amount=amount,
        consumption_type=consumption_type,
        ready_time=ready_time,
        order_id=order_id,
        medicine_name=medicine_name,
    )
    session.add(recipe)
    session.commit()
    return recipe


def set_order_id(id_: int, order_id: int):
    session.query(Recipe).filter(Recipe.id == id_).update({'order_id': order_id})
    session.commit()


def set_ready_time(id_: int, ready_time: date):
    session.query(Recipe).filter(Recipe.id == id_).update(
        {'ready_time': ready_time}
    )
    session.commit()
