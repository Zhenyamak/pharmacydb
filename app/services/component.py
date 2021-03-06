from typing import Optional

from app.model import Component
from app.services.db import session


def create_component(name: str, price: float, amount: float) -> Component:
    com = Component(name=name, price=price, amount=amount)
    session.add(com)
    session.commit()
    return com


def get_component_by_id(id_: int) -> Optional[Component]:
    component = session.query(Component).get(id_)
    return component


def set_component_amount(component_id: int, amount: int) -> None:
    (
        session.query(Component)
        .filter(Component.id == component_id)
        .update({'amount': amount})
    )
    session.commit()
