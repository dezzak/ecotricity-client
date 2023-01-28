import datetime
import unittest

from client.dto import MeterRead


class TestMeterRead(unittest.TestCase):

    def test_deserialisation(self):
        json = """
        {
            "id": "91b06eb6-0698-4cf1-bbf6-025a4de0d521",
            "date": "2023-01-18T00:00:00.000Z",
            "createdAt": "2023-01-18T18:14:14.282Z",
            "updatedAt": "2023-01-18T18:14:14.282Z",
            "source": "SMR",
            "value": 9385,
            "quality": "Normal",
            "sequenceType": "Normal",
            "registerIndustryId": "1",
            "meterIndustryId": "19A1234567",
            "status": "accepted",
            "submissionClient": "unknown",
            "accountId": "87ff8cfb-8cf3-4d7c-9e3e-0b41ea11f913",
            "agreementId": "d0989caf-ecf3-4264-a574-c34233037cde",
            "meterPointIndustryId": "1234567890123"
        }
        """
        entity = MeterRead.from_json(json)
        self.assertEqual(entity.id, "91b06eb6-0698-4cf1-bbf6-025a4de0d521")
        self.assertEqual(entity.date, datetime.datetime.fromisoformat("2023-01-18T00:00:00+00:00"))
        self.assertEqual(entity.created_at, datetime.datetime.fromisoformat("2023-01-18T18:14:14.282+00:00"))
        self.assertEqual(entity.updated_at, datetime.datetime.fromisoformat("2023-01-18T18:14:14.282+00:00"))
        self.assertEqual(entity.source, "SMR")
        self.assertEqual(entity.value, 9385)
        self.assertEqual(entity.quality, "Normal")
        self.assertEqual(entity.sequence_type, "Normal")
        self.assertEqual(entity.register_industry_id, '1')
        self.assertEqual(entity.meter_industry_id, "19A1234567")
        self.assertEqual(entity.status, "accepted")
        self.assertEqual(entity.submission_client, "unknown")
        self.assertEqual(entity.account_id, "87ff8cfb-8cf3-4d7c-9e3e-0b41ea11f913")
        self.assertEqual(entity.agreement_id, "d0989caf-ecf3-4264-a574-c34233037cde")
        self.assertEqual(entity.meter_point_industry_id, "1234567890123")
