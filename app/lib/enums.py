from enum import Enum
from enum import auto


class OrderStatus(Enum):
    in_process = auto()
    waiting_for_components = auto()
    ready = auto()
    closed = auto()


class CookingMethod(Enum):
    mixing = auto()
    creaming = auto()


class MedicineType(Enum):
    pill = auto()
    ointment = auto()
    tincture = auto()
    mixture = auto()
    liquor = auto()
    powder = auto()


class ConsumptionType(Enum):
    internal = auto()
    external = auto()
    mixing = auto()
