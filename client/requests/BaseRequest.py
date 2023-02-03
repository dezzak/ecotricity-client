from json import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from dataclass_wizard import JSONWizard
from client.dto import Session
from client.exceptions import ApiException, ResponseDecodeException, EcotricityClientException


class BaseRequest:
    host: str
    proto: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https"):
        self.host = host
        self.proto = proto

    def read_data(self, path: str, variables: str, session: Session, target: type[JSONWizard]):
        r = Request(f'{self.proto}://{self.host}{path}{variables}')
        r.add_header('Authorization', f'Bearer {session.auth_token}')

        try:
            return target.from_json(urlopen(r).read().decode())
        except HTTPError as ex:
            raise ApiException("Failed to read from the API", ex)
        except JSONDecodeError as ex:
            raise ResponseDecodeException("Unable to decode response", ex)
        except Exception as ex:
            raise EcotricityClientException("Error while getting readings", ex)