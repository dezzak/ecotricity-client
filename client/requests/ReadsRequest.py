import urllib.parse
from urllib.request import Request, urlopen
from client.dto.MeterReadsResult import MeterReadsResult


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

        return MeterReadsResult.from_json(urlopen(r).read().decode())
