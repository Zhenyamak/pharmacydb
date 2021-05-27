from app.model import Client
from app.services.db import session


def create_client(
    first_name: str,
    last_name: str,
    phone: str,
    address: str,
    age: int,
) -> Client:
    client = Client(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        age=age,
    )
    session.add(client)
    session.commit()
    return client
