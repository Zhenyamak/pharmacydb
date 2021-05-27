from typing import Optional

from app.model import Ingredient
from app.services.db import session


def add_ingredient(
    component_id: int,
    amount: int,
) -> Ingredient:
    ingredient_record = Ingredient(
        component_id=component_id,
        dose=amount,
    )
    session.add(ingredient_record)
    session.commit()
    return ingredient_record


def get_ingredient_by_id(id_: int) -> Optional[Ingredient]:
    component = session.query(Ingredient).get(id_)
    return component


def set_ingredient_dose(id_: int, dose: int) -> None:
    (
        session.query(Ingredient)
        .filter(id == id_)
        .update({'dose': dose})
    )
    session.commit()
