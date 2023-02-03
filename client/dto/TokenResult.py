from dataclasses import dataclass
from dataclass_wizard import JSONWizard

from . import TokenData


@dataclass
class TokenResult(JSONWizard):
    data: TokenData
    status: str
