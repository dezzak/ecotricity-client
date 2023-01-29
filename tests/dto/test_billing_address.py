import unittest

from client.dto import BillingAddress


class TestBillingAddress(unittest.TestCase):

    def test_deserialisation_short_address(self):
        json = """{
            "postcode": "AB1 2CD",
            "address4": "SOMETOWN",
            "address1": "123 Any Street",
            "countryCode": "GB"
        }
        """
        entity = BillingAddress.from_json(json)
        self.assertEqual(entity.postcode, "AB1 2CD")
        self.assertEqual(entity.address1, "123 Any Street")
        self.assertEqual(entity.address4, "SOMETOWN")
        self.assertEqual(entity.country_code, "GB")

    #  The following is an assumption of how this would be formed
    def test_deserialisation_long_address(self):
        json = """{
            "postcode": "AB1 2CD",
            "address4": "SOMETOWN",
            "address1": "Unit 1",
            "address2": "123 Any Street",
            "address3": "Some Village",
            "countryCode": "GB"
        }
        """
        entity = BillingAddress.from_json(json)
        self.assertEqual(entity.postcode, "AB1 2CD")
        self.assertEqual(entity.address1, "Unit 1")
        self.assertEqual(entity.address2, "123 Any Street")
        self.assertEqual(entity.address3, "Some Village")
        self.assertEqual(entity.address4, "SOMETOWN")
        self.assertEqual(entity.country_code, "GB")
