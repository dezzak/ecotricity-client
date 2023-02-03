import unittest

from client.dto import TokenData


class TestTokenData(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"access":"chicken","refresh":"badger"}'
        entity = TokenData.from_json(json)
        self.assertEqual(entity.access, "chicken")
        self.assertEqual(entity.refresh, "badger")
