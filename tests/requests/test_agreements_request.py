import unittest
from json import JSONDecodeError
from urllib.error import HTTPError

import httpretty

from client.dto import AgreementsResult, Session
from client.exceptions import ResponseDecodeException
from client.requests import AgreementsRequest
from client.exceptions import ApiException


class TestAgreementsRequest(unittest.TestCase):
    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_loads_agreements(self):
        #  Given an AgreementsRequest class
        req = AgreementsRequest(proto="http", host="example.com")

        #  And our variables
        customer_id = "chicken"
        account_id = "badger"
        auth = "Bearer someToken"
        session = Session(customer_id, auth)

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.GET,
            f'http://example.com/customers/v1/customers/{customer_id}/accounts/{account_id}/agreements',
            body=self.normal_response_body()
        )

        #  When the method is called
        result = req.get_agreements(session, account_id)

        #  Then we get a sensible result
        self.assertIsInstance(result, AgreementsResult)
        self.assertEqual(result.status, "success")

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_error(self):
        #  Given an AgreementsRequest class
        req = AgreementsRequest(proto="http", host="example.com")

        #  And our variables
        customer_id = "chicken"
        account_id = "badger"
        auth = "Bearer someToken"
        session = Session(customer_id, auth)

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.GET,
            f'http://example.com/customers/v1/customers/{customer_id}/accounts/{account_id}/agreements',
            body=self.unauthorised_response_body(),
            status=401
        )

        #  When the method is called
        with self.assertRaises(ApiException) as context:
            req.get_agreements(session, account_id)

        #  Then we get an exception
        self.assertEqual(context.exception.message, "Failed to read from the API")
        self.assertIsInstance(context.exception.__cause__, HTTPError)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_deserialisation_failure(self):
        #  Given an AgreementsRequest class
        req = AgreementsRequest(proto="http", host="example.com")

        #  And our variables
        customer_id = "chicken"
        account_id = "badger"
        auth = "Bearer someToken"
        session = Session(customer_id, auth)

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.GET,
            f'http://example.com/customers/v1/customers/{customer_id}/accounts/{account_id}/agreements',
            body=self.abnormal_response_body(),
            status=200
        )

        #  When the method is called
        with self.assertRaises(ResponseDecodeException) as context:
            req.get_agreements(session, account_id)

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
