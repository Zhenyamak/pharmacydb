import typing as t
from itertools import groupby
from operator import itemgetter
from datetime import date

from sqlalchemy import distinct, func, text

from app.lib.enums import MedicineType
from app.model import Client, Component, CookingBook, CriticalNorm, Ingredient, Medicine, Order, Recipe
from app.services.db import session


# 1
def get_clients_with_not_taken_orders() -> t.List[Client]:
    query = (
        session.query(Recipe, Client)
        .join(Client)
        .join(Order)
        .filter(Order.status == Order.STATUSES.ready)
        .filter(Recipe.ready_time < date.today())
    )
    return [r[1] for r in query.all()]


# 2
def get_clients_waiting_for_ingridients() -> t.List[Client]:
    query = (
        session.query(Client, Order.status)
        .join(Client, Order.client_id == Client.id)
        .filter(Order.status == Order.STATUSES.waiting_for_components)
    )

    return [i[0] for i in query.all()]


# 3
def get_top_ten_most_used_medicines() -> t.List[str]:
    query = (
        session.query(
            Medicine.name,
            func.count(Order.medicine_id).label('total')
        )
        .join(Order, Order.medicine_id == Medicine.id)
        .group_by(Order.medicine_id)
        .order_by(text('total DESC'))
        .limit(10)
    )
    return [r[0] for r in query.all()]


# 4
def get_component_used_amount(
    name: str,
    start_date: date,
    end_date: date,
) -> t.List[t.Tuple[str, int]]:
    query = (
        session.query(
            func.avg(Order.date_created),
            Component.name,
            func.sum(Ingredient.dose),
        )
        .join(Medicine)
        .join(Medicine.ingredients)
        .join(Ingredient.component)
        .filter(Order.date_created > start_date)
        .filter(Order.date_created <= end_date)
        .filter(Component.name == name)
        .group_by(Component.name)
    )

    return [(r[1], r[2]) for r in query.all()]


# 5
def get_client_by_ordered_medicine_type(
    type: MedicineType,
    start_date: t.Optional[date] = None,
    end_date: t.Optional[date] = None,
) -> t.List[Client]:
    query = (
        session.query(Order, Medicine.type, Client)
        .join(Medicine)
        .join(Client)
        .filter(Medicine.type == type)
    )
    if start_date:
        query = query.filter(Order.date_created > start_date)
    if end_date:
        query = query.filter(Order.date_created <= end_date)
    return [r[2] for r in query.all()]


# 6
def get_components_with_critical_norm():
    query = (
        session.query(CriticalNorm.amount, Component)
        .join(Component)
        .filter(Component.amount <= CriticalNorm.amount)
    )
    return [r[1] for r in query.all()]


# 7
def get_medicine_with_minimal_components_amount(
    type: t.Optional[MedicineType] = None
) -> t.List[str]:
    min_query = (
        session.query(func.min(Component.amount))
        .join(Medicine.ingredients)
        .join(Component)
        .scalar_subquery()
    )
    query = (
        session.query(distinct(Medicine.name))
        .join(Medicine.ingredients)
        .join(Component)
        .filter(Component.amount == min_query)
    )

    if type:
        query = query.filter(Medicine.type == type)

    return [r[0] for r in query.all()]


# 8
def get_orders_amount_in_process_status():
    query = (
        session.query(func.count(Order.id))
        .filter(Order.status == Order.STATUSES.in_process)
    )

    return query.scalar()


# 9
def get_medicine_in_waiting_for_components_status():
    query = (
        session.query(Order.status, Medicine)
        .join(Medicine)
        .filter(Order.status == Order.STATUSES.waiting_for_components)
    )

    return [r[1] for r in query.all()]


# 10
def get_cooking_book_for_madicine_name(
    name: str
) -> t.Optional[CookingBook]:
    query = (
        session.query(CookingBook)
        .join(Medicine)
        .filter(Medicine.name == name)
    )
    return query.all()


def get_cooking_book_for_madicine_type(
    type: MedicineType
) -> t.Optional[CookingBook]:
    query = (
        session.query(CookingBook)
        .join(Medicine)
        .filter(Medicine.type == type)
    )
    return query.all()


def get_cooking_book_for_orders_in_process() -> t.Optional[CookingBook]:
    medicine_ids_query = (
        session.query(Order, Medicine.id)
        .join(Medicine)
        .filter(Order.status == Order.STATUSES.in_process)
    )

    medicine_ids = set(r[1] for r in medicine_ids_query.all())

    cooking_books_query = (
        session.query(CookingBook)
        .join(Medicine)
        .filter(Medicine.id.in_(medicine_ids))
    )

    return cooking_books_query.all()


# 11
def get_price_for_medicine(medicine_id: int) -> int:
    query = (
        session.query(Medicine.price)
        .filter(Medicine.id == medicine_id)
    )

    return query.scalar()


def get_component_price_for_medicine(
    medicine_id: int,
) -> t.Dict[str, t.List[t.Tuple[str, float]]]:
    query = (
        session.query(Medicine.name, Ingredient.component_id,
                      Component.name, Component.price)
        .join(Medicine.ingredients)
        .join(Component)
        .filter(Medicine.id == medicine_id)
    )

    return {
        medicine_name: [(r[2], r[3]) for r in records]
        for medicine_name, records
        in groupby(
            sorted(
                query,
                key=itemgetter(0),
            ),
            key=itemgetter(0),
        )
    }


# 12
def get_orders_for_most_popular_medicine():
    most_popular_medicine_id = (
        session.query(
            Order.medicine_id,
            func.count(Order.medicine_id).label('order_amount')
        )
        .group_by(Order.medicine_id)
        .order_by(text('order_amount DESC'))
        .limit(1)
        .first()
    )
    if most_popular_medicine_id:
        query = (
            session.query(Order)
            .filter(Order.medicine_id == most_popular_medicine_id[0])
        )
        return query.all()
    else:
        return None


# 13
def get_full_medicine_info(medicine_id: int) -> t.Optional[Medicine]:
    return session.query(Medicine).filter(Medicine.id == medicine_id).first()
