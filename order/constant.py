
from enum import IntEnum as BaseIntEnum

from django.db import models


class IntEnum(BaseIntEnum):
    def dump(self):
        name = getattr(self, 'label', self.value)
        return dict(
            name=self.name,
            label=name,
            value=self.value,
        )
class BusssinessPartType(IntEnum):
    TYRE = 1
    WALL_BOX = 2
    OIL_CHEMICAL = 3
    MAINTENANCE = 4
    GENERAL_REPAIR_PARTS = 5
    TAC = 6

    @classmethod
    def get_by_pm_value(cls, val):
        try:
            return [s for s in cls if s.name == val][0]
        except IndexError:
            return cls.TYRE



class OrderBussinessType(models.TextChoices):
    TAC= "TAC","精品"
    TYRE= "TYRE","轮胎"
class OrderStatus(models.IntegerChoices):
    CONFIRMED = 0
    PENDING = 1  # -> DONE, FAILED, CANCELLING
    DONE = 2
    # pending arrived only used for display
    PENDING_ARRIVED = 3
    REJECTED = 4
    CANCELLING = 5  # -> CANCELLED, PENDING
    CANCELLED = 6
    FAILED = -2  # -> NEW
    NEW = -1  # -> PENDING, FAILED
