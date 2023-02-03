from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class TokenData(JSONWizard):
    access: str
    refresh: str
