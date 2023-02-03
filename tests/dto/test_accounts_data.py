import unittest

from ecotricity.client.dto import AccountsData, Account


class TestAccountsData(unittest.TestCase):

    def test_deserialisation(self):
        json = """{
            "results": [
                {
                    "id": "91e51860-07c1-422c-bd04-1026065d2b5b",
                    "fromDate": "2014-01-01",
                    "balance": -12.34,
                    "displayNumber": "12345678",
                    "billingMethod": "ebilling",
                    "displayBillingAddress": {
                        "postcode": "AB1 2CD",
                        "address4": "SOMETOWN",
                        "address1": "123 Any Street",
                        "countryCode": "GB"
                    },
                    "paymentMethod": "direct-debit",
                    "accountClass": "Invoice",
                    "inDunning": false
                }
            ]
        }
        """
        entity = AccountsData.from_json(json)
        self.assertEqual(len(entity.results), 1)
        self.assertIsInstance(entity.results[0], Account)
