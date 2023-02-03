import unittest

from client.dto import TokenResult, TokenData


class TestTokenResult(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"data":{"access":"aToken","refresh":"unicorn"},"status":"success"}'
        entity = TokenResult.from_json(json)
        self.assertEqual(entity.status, "success")
        self.assertIsInstance(entity.data, TokenData)
