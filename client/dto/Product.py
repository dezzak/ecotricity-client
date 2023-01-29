from dataclasses import dataclass
from dataclass_wizard import JSONWizard

# FIXME - why can't I just do `from . import MeterPoint`?
from .MeterPoint import MeterPoint


@dataclass
class Product(JSONWizard):
    display_name: str
    meter_points: list[MeterPoint]
