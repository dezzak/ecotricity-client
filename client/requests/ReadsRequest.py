import urllib.parse
from client.dto import MeterReadsResult, Session
from client.requests.BaseRequest import BaseRequest


class ReadsRequest(BaseRequest):
    path: str

    def __init__(self, host="api.ecotricity.co.uk", proto="https", path="/meters/v1/"):
        super().__init__(host, proto)
        self.path = path

    def get_reads(self, session: Session, meter_point: str) -> MeterReadsResult:
        variables = urllib.parse.quote(f'customers/{session.customer_id}/meter-points/{meter_point}/reads')

        return self.read_data(self.path, variables, session, MeterReadsResult)
