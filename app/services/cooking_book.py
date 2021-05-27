from app.model import CookingBook
from app.services.db import session
from app.lib.enums import CookingMethod


def create_cooking_book(medicine_id: int, method: CookingMethod) -> CookingBook:
    cooking_book = CookingBook(medicine_id=medicine_id, method=method)
    session.add(cooking_book)
    session.commit()
    return cooking_book
