import unittest

from ecotricity.client.dto import AgreementsData, Agreement


class TestAgreementsData(unittest.TestCase):

    def test_deserialisation(self):
        json = """{
            "results": [
                {
                    "id": "489b54f8-e2a3-444b-bcd8-baa57f79db12",
                    "displayNumber": "012345678901234567",
                    "fromDate": "2014-01-01",
                    "fuelType": "electricity",
                    "products": []
                }
            ]
        }"""
        entity = AgreementsData.from_json(json)
        self.assertEqual(len(entity.results), 1)
        self.assertIsInstance(entity.results[0], Agreement)
        self.assertEqual(entity.results[0].id, "489b54f8-e2a3-444b-bcd8-baa57f79db12")
