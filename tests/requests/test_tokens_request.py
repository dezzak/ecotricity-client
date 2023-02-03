import unittest
from json import JSONDecodeError
from urllib.error import HTTPError

import httpretty

from ecotricity.client.exceptions import ResponseDecodeException
from ecotricity.client.dto import TokensResult
from ecotricity.client.exceptions import ApiException
from ecotricity.client.requests import TokensRequest


class TestTokensRequest(unittest.TestCase):
    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_fetches_token(self):
        #  Given a TokensRequest class
        req = TokensRequest(proto="http", host="example.com")

        #  And our variables
        username = "chicken"
        password = "super53cr37"

        #  And we have mocked the http responses
        def request_callback(request, uri, response_headers):
            expected_request = '{"username": "chicken", "password": "super53cr37"}'.encode('utf-8')
            assert request.body == expected_request, 'unexpected body: {}'.format(request.body)
            return [200, response_headers, self.normal_response_body()]

        httpretty.register_uri(
            httpretty.POST,
            f'http://example.com/auth/v2/tokens',
            body=request_callback
        )

        #  When the method is called
        result = req.get_tokens(username, password)

        #  Then we get a sensible result
        self.assertIsInstance(result, TokensResult)
        self.assertEqual(result.status, "success")

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_error(self):
        #  Given a TokensRequest class
        req = TokensRequest(proto="http", host="example.com")

        #  And our variables
        username = "chicken"
        password = "wrongPassword"

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.POST,
            f'http://example.com/auth/v2/tokens',
            body=self.unauthorised_response_body(),
            status=401
        )

        #  When the method is called
        with self.assertRaises(ApiException) as context:
            req.get_tokens(username, password)

        #  Then we get an exception
        self.assertEqual("Failed to read from the API", context.exception.message)
        self.assertIsInstance(context.exception.__cause__, HTTPError)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_handles_deserialisation_failure(self):
        #  Given a TokensRequest class
        req = TokensRequest(proto="http", host="example.com")

        #  And our variables
        username = "chicken"
        password = "wrongPassword"

        #  And we have mocked the http responses
        httpretty.register_uri(
            httpretty.POST,
            f'http://example.com/auth/v2/tokens',
            body=self.abnormal_response_body()
        )

        #  When the method is called
        with self.assertRaises(ResponseDecodeException) as context:
            req.get_tokens(username, password)

        #  Then we get an exception
        self.assertEqual(context.exception.message, "Unable to decode response")
        self.assertIsInstance(context.exception.__cause__, JSONDecodeError)

    @staticmethod
    def normal_response_body() -> str:
        return '{"data":{"access":"access","refresh":"refresh"},"status":"success"}'

    @staticmethod
    def unauthorised_response_body() -> str:
        return """
        {
            "data": {
                "message": "An account with this username or email address and password was not found."
            },
            "status": "fail"
        }
        """

    @staticmethod
    def abnormal_response_body() -> str:
        return '<not>json</not>'
