import urllib.parse
from json import JSONDecodeError
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from client.dto.MeterReadsResult import MeterReadsResult
from client.exceptions.ApiException import ApiException
from client.exceptions.EcotricityClientException import EcotricityClientException
from client.exceptions.ResponseDecodeException import ResponseDecodeException


class ReadsRequest:
    host: str
    proto: str
    path: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https", path="/meters/v1/"):
        self.host = host
        self.proto = proto
        self.path = path

    def get_reads(self, customer_id: str, meter_point: str, auth: str) -> MeterReadsResult:
        #  TODO - auth needs handling separately - possibly a session class? customer ID could go there too

        variables = urllib.parse.quote(f'customers/{customer_id}/meter-points/{meter_point}/reads')

        r = Request(f'{self.proto}://{self.host}{self.path}{variables}')
        r.add_header('Authorization', auth)

        try:
            return MeterReadsResult.from_json(urlopen(r).read().decode())
        except HTTPError as ex:
            raise ApiException("Failed to read from the API", ex)
        except JSONDecodeError as ex:
            raise ResponseDecodeException("Unable to decode response", ex)
        except Exception as ex:
            raise EcotricityClientException("Error while getting readings", ex)
