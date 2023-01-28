from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from client.dto.AgreementsData import AgreementsData


@dataclass
class AgreementsResult(JSONWizard):
    data: AgreementsData
    status: str
