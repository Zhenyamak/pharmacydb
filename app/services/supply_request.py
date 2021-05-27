from app.model import SupplyRequest
from app.services.db import session


def create_supply_request(
    component_id: int,
    clinent_id: int,
) -> SupplyRequest:
    sup_request = SupplyRequest(
        component_id=component_id,
        clinent_id=clinent_id,
    )
    session.add(sup_request)
    session.commit()
    return sup_request
