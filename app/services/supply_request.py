from app.model import SupplyRequest
from app.services.db import session
from app.model import Component

def create_supply_request(
    component_id: int,
    client_id: int,
) -> SupplyRequest:
    component = session.query(Component).filter(Component.id == component_id).exists()
    if not component:
        return None
    sup_request = SupplyRequest(
        component_id=component_id,
        client_id=client_id,
    )
    session.add(sup_request)
    session.commit()
    return sup_request
