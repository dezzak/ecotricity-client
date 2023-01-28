import unittest

from client.dto.Product import Product


class TestMeterPoint(unittest.TestCase):

    def test_deserialisation(self):
        json = '{"displayName":"Green Gas","meterPoints":[{"industryId":"1234567890","fuelType":"gas"}]}'
        entity = Product.from_json(json)
        self.assertEqual(entity.display_name, "Green Gas")
        self.assertEqual(entity.meter_points[0].industry_id, "1234567890")
