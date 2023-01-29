import datetime
import unittest

from client.dto import Account


class TestAccount(unittest.TestCase):

    def test_deserialisation(self):
        json = """{
            "id": "c3f24aad-2476-4395-9053-f8ba43aa5b5a",
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
        """
        entity = Account.from_json(json)
        self.assertEqual(entity.id, "c3f24aad-2476-4395-9053-f8ba43aa5b5a")
        self.assertEqual(entity.from_date, datetime.date.fromisoformat('2014-01-01'))
        self.assertEqual(entity.balance, -12.34)
        self.assertEqual(entity.display_number, "12345678")
        self.assertEqual(entity.billing_method, "ebilling")
        self.assertEqual(entity.display_billing_address.country_code, "GB")
        self.assertEqual(entity.payment_method, "direct-debit")
        self.assertEqual(entity.account_class, "Invoice")
        self.assertFalse(entity.in_dunning)
