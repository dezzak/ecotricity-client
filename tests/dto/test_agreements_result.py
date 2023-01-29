import unittest

from client.dto import AgreementsResult, AgreementsData


class TestAgreementsResult(unittest.TestCase):

    def test_deserialisation(self):
        json = """{"data": {"results": []}, "status": "success"}"""
        entity = AgreementsResult.from_json(json)
        self.assertEqual(entity.status, "success")
        self.assertIsInstance(entity.data, AgreementsData)
        self.assertEqual(len(entity.data.results), 0)
