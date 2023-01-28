import urllib.parse
from json import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from client.dto.AgreementsResult import AgreementsResult
from client.exceptions.ApiException import ApiException
from client.exceptions.EcotricityClientException import EcotricityClientException
from client.exceptions.ResponseDecodeException import ResponseDecodeException


class AgreementsRequest:
    host: str
    proto: str
    path: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https", path="/customers/v1/"):
        self.host = host
        self.proto = proto
        self.path = path

    def get_agreements(self, customer_id: str, account_id: str, auth: str) -> AgreementsResult:
        #  TODO - auth needs handling separately - possibly a session class? customer ID could go there too

        variables = urllib.parse.quote(f'customers/{customer_id}/accounts/{account_id}/agreements')

        r = Request(f'{self.proto}://{self.host}{self.path}{variables}')
        r.add_header('Authorization', auth)

        try:
            return AgreementsResult.from_json(urlopen(r).read().decode())
        except HTTPError as ex:
            raise ApiException("Failed to read from the API", ex)
        except JSONDecodeError as ex:
            raise ResponseDecodeException("Unable to decode response", ex)
        except Exception as ex:
            raise EcotricityClientException("Error while getting readings", ex)
