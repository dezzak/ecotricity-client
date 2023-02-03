import unittest

from client.dto import TokensResult, TokensData


class TestTokensResult(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"data":{"access":"aToken","refresh":"unicorn"},"status":"success"}'
        entity = TokensResult.from_json(json)
        self.assertEqual(entity.status, "success")
        self.assertIsInstance(entity.data, TokensData)
