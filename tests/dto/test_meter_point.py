import unittest

from ecotricity.client.dto import MeterPoint


class TestMeterPoint(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"industryId":"1234567890","fuelType":"gas"}'
        entity = MeterPoint.from_json(json)
        self.assertEqual(entity.industry_id, "1234567890")
        self.assertEqual(entity.fuel_type, "gas")
