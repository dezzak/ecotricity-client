from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from client.dto.MeterPoint import MeterPoint


@dataclass
class Product(JSONWizard):
    display_name: str
    meter_points: list[MeterPoint]
