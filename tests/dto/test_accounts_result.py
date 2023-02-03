import unittest

from ecotricity.client.dto import AccountsResult, AccountsData


class TestAccountsResult(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"data": {"results": []}, "status": "success"}'
        entity = AccountsResult.from_json(json)
        self.assertEqual(entity.status, "success")
        self.assertIsInstance(entity.data, AccountsData)
