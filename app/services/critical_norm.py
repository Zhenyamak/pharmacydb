from app.model import CriticalNorm
from app.services.db import session


def create_critical_norm(
    component_id: int,
    amount: float,
) -> CriticalNorm:
    crit_norm = CriticalNorm(component_id=component_id, amount=amount)
    session.add(crit_norm)
    session.commit()
    return crit_norm


def set_critical_norm(component_id: int, amount: int) -> None:
    (
        session.query(CriticalNorm)
        .filter(CriticalNorm.id == component_id)
        .update({'amount': amount})
    )
    session.commit()
