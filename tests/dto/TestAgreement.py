import datetime
import unittest

from client.dto.Agreement import Agreement


class TestAgreement(unittest.TestCase):

    def test_deserialisation(self):
        json = """{
            "id": "49ec16cb-8627-4968-ae71-b96438b22a89",
            "displayNumber": "012345678901234567",
            "fromDate": "2014-01-01",
            "fuelType": "electricity",
            "products": [
                {
                    "displayName": "Green Electricity",
                    "meterPoints": []
                }
            ]
        }"""
        entity = Agreement.from_json(json)
        self.assertEqual(entity.id, "49ec16cb-8627-4968-ae71-b96438b22a89")
        self.assertEqual(entity.display_number, "012345678901234567")
        self.assertEqual(entity.from_date, datetime.date.fromisoformat('2014-01-01'))
        self.assertEqual(entity.fuel_type, "electricity")
        self.assertEqual(len(entity.products), 1)
        self.assertEqual(entity.products[0].display_name, "Green Electricity")
