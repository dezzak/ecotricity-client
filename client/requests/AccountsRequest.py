import urllib.parse
from json import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from client.dto import AccountsResult, Session
from client.exceptions import ApiException
from client.exceptions import EcotricityClientException
from client.exceptions import ResponseDecodeException


class AccountsRequest:
    host: str
    proto: str
    path: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https", path="/customers/v1/"):
        self.host = host
        self.proto = proto
        self.path = path

    def get_accounts(self, session: Session) -> AccountsResult:
        variables = urllib.parse.quote(f'customers/{session.customer_id}/accounts')

        r = Request(f'{self.proto}://{self.host}{self.path}{variables}')
        r.add_header('Authorization', f'Bearer {session.auth_token}')

        try:
            return AccountsResult.from_json(urlopen(r).read().decode())
        except HTTPError as ex:
            raise ApiException("Failed to read from the API", ex)
        except JSONDecodeError as ex:
            raise ResponseDecodeException("Unable to decode response", ex)
        except Exception as ex:
            raise EcotricityClientException("Error while getting readings", ex)
