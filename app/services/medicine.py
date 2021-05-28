import typing as t
from datetime import date


from app.model import Medicine
from app.services.db import session
from app.lib.enums import MedicineType
from app.lib.enums import CookingMethod
from app.services import cooking_book as cb_service
from app.model import Ingredient


def create_medicine(
    name: str,
    storage_time: date,
    amount: float,
    price: float,
    type: MedicineType,
    cooking_method: CookingMethod,
    ingredients_ids: t.List[int] = [],
) -> Medicine:
    med = Medicine(
        name=name,
        storage_time=storage_time,
        amount=amount,
        price=price,
        type=type,
    )
    ingredients = (
        session.query(Ingredient)
        .filter(Ingredient.id.in_(ingredients_ids))
    )
    if ingredients:
        med.ingredients.extend(ingredients)
    session.add(med)
    session.commit()

    cb_service.create_cooking_book(med.id, cooking_method)
    return med


def get_by_name(name: str) -> t.Optional[Medicine]:
    return session.query(Medicine).filter(name == name).fisrt()
