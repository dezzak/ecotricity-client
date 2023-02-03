import json
from json import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from client.dto import TokensResult
from client.exceptions import ApiException
from client.exceptions import EcotricityClientException
from client.exceptions import ResponseDecodeException


class TokensRequest:
    host: str
    proto: str
    path: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https", path="/auth/v2/tokens"):
        self.host = host
        self.proto = proto
        self.path = path

    def get_tokens(self, username: str, password: str) -> TokensResult:
        body = str(json.dumps({'username': username, 'password': password})).encode('utf-8')
        r = Request(f'{self.proto}://{self.host}{self.path}')

        try:
            return TokensResult.from_json(urlopen(r, data=body).read().decode())
        except HTTPError as ex:
            raise ApiException("Failed to read from the API", ex)
        except JSONDecodeError as ex:
            raise ResponseDecodeException("Unable to decode response", ex)
        except Exception as ex:
            raise EcotricityClientException("Error while getting readings", ex)
