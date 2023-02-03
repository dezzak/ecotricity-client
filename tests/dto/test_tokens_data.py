import unittest

from client.dto import TokensData


class TestTokensData(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"access":"chicken","refresh":"badger"}'
        entity = TokensData.from_json(json)
        self.assertEqual(entity.access, "chicken")
        self.assertEqual(entity.refresh, "badger")
