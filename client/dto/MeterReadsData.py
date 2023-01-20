from dataclasses import dataclass
from dataclass_wizard import JSONWizard

from client.dto.MeterRead import MeterRead


@dataclass
class MeterReadsData(JSONWizard):
    results: list[list[MeterRead]]
