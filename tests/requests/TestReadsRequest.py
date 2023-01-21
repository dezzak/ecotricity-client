import unittest
from json import JSONDecodeError
from urllib.error import HTTPError

import httpretty

from client.exceptions.ResponseDecodeException import ResponseDecodeException
from client.requests.ReadsRequest import ReadsRequest
from client.dto.MeterReadsResult import MeterReadsResult
from client.exceptions.ApiException import ApiException


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

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_error(self):
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
            body=self.unauthorised_response_body(),
            status=401
        )

        #  When the method is called
        with self.assertRaises(ApiException) as context:
            req.get_reads(customer_id, meter_point, auth)

        #  Then we get an exception
        self.assertEqual(context.exception.message, "Failed to read from the API")
        self.assertIsInstance(context.exception.__cause__, HTTPError)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_deserialisation_failure(self):
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
            body=self.abnormal_response_body(),
            status=200
        )

        #  When the method is called
        with self.assertRaises(ResponseDecodeException) as context:
            req.get_reads(customer_id, meter_point, auth)

        #  Then we get an exception
        self.assertEqual(context.exception.message, "Unable to decode response")
        self.assertIsInstance(context.exception.__cause__, JSONDecodeError)

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

    @staticmethod
    def unauthorised_response_body() -> str:
        return """
        {
            "status": "fail",
            "data": {
                "message": "Unauthorized"
            }
        }
        """

    @staticmethod
    def abnormal_response_body() -> str:
        return '<not>json</not>'
