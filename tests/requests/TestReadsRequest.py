import unittest

import httpretty

from client.requests.ReadsRequest import ReadsRequest
from client.dto.MeterReadsResult import MeterReadsResult


class TestReadsRequest(unittest.TestCase):
    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_loads_meter_readings(self):
        #  Given a ReadsRequest class
        req = ReadsRequest(proto="http", host="example.com")

        #  And our variables
        customer_id = "chicken"
        meter_point = "12"
        auth = "Bearer someToken"

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.GET,
            f'http://example.com/meters/v1/customers/{customer_id}/meter-points/{meter_point}/reads',
            body=self.normal_response_body()
        )

        #  When the method is called
        result = req.get_reads(customer_id, meter_point, auth)

        #  Then we get a sensible result
        self.assertIsInstance(result, MeterReadsResult)
        self.assertEqual(result.status, "success")

    @staticmethod
    def normal_response_body() -> str:
        return """
        {
            "data":{
                "results":[]
            },
            "status":"success"
        }
        """
