import unittest
from unittest.mock import patch, MagicMock

import jwt

from client.dto import Session, TokensResult, TokensData
from client.service import open_session


class TestSession(unittest.TestCase):
    @patch('client.service.session.TokensRequest')
    def test_open_session(self, tokens_request):
        #  Given a user and password
        username = 'chicken'
        password = 'badger'

        #  And an expected customer ID and token
        customer_id = 'unicorn'
        token = jwt.encode({'data': {'customerId': customer_id}}, "secret", algorithm="HS256")

        #  And a mocked response from Ecotricity
        tokens_data = TokensData(access=token, refresh="refresh")
        mocked_response = TokensResult(data=tokens_data, status="success")
        tokens_request.return_value.get_tokens.return_value = mocked_response

        #  When the open session function is called
        result = open_session(username, password)

        #  Then we get a session object back
        self.assertIsInstance(result, Session)

        #  And it has the correct fields set
        self.assertEqual(token, result.auth_token)
        self.assertEqual(customer_id, result.customer_id)
