import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.lib.enums import ConsumptionType
from app.lib.enums import MedicineType
from app.lib.enums import CookingMethod
from app.lib.enums import OrderStatus


Base = declarative_base()

# many-to-many relationships tables

ingredient_medicine = sa.Table(
    'ingredient_medicine',
    Base.metadata,
    sa.Column('ingredient_id', sa.Integer, sa.ForeignKey('ingredient.id')),
    sa.Column('medicine_id', sa.Integer, sa.ForeignKey('medicine.id'))
)


# tables

class Client(Base):
    __tablename__ = 'client'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(60))
    last_name = sa.Column(sa.String(60))
    phone = sa.Column(sa.String(20))
    address = sa.Column(sa.String(120))
    age = sa.Column(sa.SmallInteger)

    def __repr__(self):
        return f'Client(id={self.id}, first_name={self.first_name,}, last_name={self.last_name})'


class Medicine(Base):
    __tablename__ = 'medicine'

    TYPE_ENUM = MedicineType

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(120), unique=True)
    storage_time = sa.Column(sa.Date)
    amount = sa.Column(sa.Float)
    price = sa.Column(sa.Float)
    ingredients = relationship(
        'Ingredient',
        secondary=ingredient_medicine,
        backref="medicines"
    )
    type = sa.Column(sa.Enum(MedicineType))

    def __repr__(self):
        return f'Medicine(id={self.id}, name={self.name})'


class Order(Base):
    __tablename__ = 'orders'

    STATUSES = OrderStatus
    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.Enum(OrderStatus), nullable=False)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('client.id'))
    client = relationship('Client')
    medicine_id = sa.Column(sa.Integer, sa.ForeignKey('medicine.id'))
    medicine = relationship('Medicine')
    date_created = sa.Column(sa.Date, nullable=False,
                             default=datetime.date.today)

    def __repr__(self) -> str:
        return (
            f'Order(id={self.id}, status={self.status}, medicine_id={self.medicine_id}, date_created={self.date_created})'
        )


class CookingBook(Base):
    __tablename__ = 'cooking_book'

    METHODS_ENUM = CookingMethod

    id = sa.Column(sa.Integer, primary_key=True)
    medicine_id = sa.Column(sa.Integer, sa.ForeignKey('medicine.id'))
    method = sa.Column(sa.Enum(CookingMethod))

    def __repr__(self):
        return f'CookingBook(id={self.id}, medicine_id={self.medicine_id}, method={self.method})'


class CriticalNorm(Base):
    __tablename__ = 'critical_norm'

    id = sa.Column(sa.Integer, primary_key=True)
    component_id = sa.Column(sa.Integer, sa.ForeignKey('component.id'))
    amount = sa.Column(sa.Float)

    def __repr__(self):
        return f'CriticalNorm(id={self.id}, component_id={self.component_id}, amount={self.amount})'


class Component(Base):
    __tablename__ = 'component'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(120), unique=True)
    price = sa.Column(sa.Float)
    amount = sa.Column(sa.Float)

    def __repr__(self):
        return f'Component(id={self.id}, name={self.name}, price={self.price}, amount={self.amount})'


class Recipe(Base):
    __tablename__ = 'recipe'

    id = sa.Column(sa.Integer, primary_key=True)
    medicine_name = sa.Column(sa.String(120))
    doctor = sa.Column(sa.String(255))
    client_id = sa.Column(sa.Integer, sa.ForeignKey('client.id'))
    diagnosis = sa.Column(sa.String(255))
    amount = sa.Column(sa.Float)
    consumption_type = sa.Column(sa.Enum(ConsumptionType))
    ready_time = sa.Column(sa.Date)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.id'))

    def __repr__(self):
        return f'Recipe(id={self.id}, medicine_name={self.medicine_name}, client_id={self.client_id}, ready_time={self.ready_time})'


class SupplyRequest(Base):
    __tablename__ = 'supply_request'

    id = sa.Column(sa.Integer, primary_key=True)
    component_id = sa.Column(sa.Integer, sa.ForeignKey('component.id'))
    client_id = sa.Column(sa.Integer, sa.ForeignKey('client.id'))
    client = relationship('Client')

    def __repr__(self):
        return f'SupplyRequest(id={self.id}, component_id={self.component_id}, client_id={self.client_id})'


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = sa.Column(sa.Integer, primary_key=True)
    component_id = sa.Column(sa.Integer, sa.ForeignKey('component.id'))
    component = relationship('Component')
    dose = sa.Column(sa.Float)

    def __repr__(self):
        return f'Ingredient(id={self.id}, component_id={self.component_id}, dose={self.dose})'
