import unittest

from ecotricity.client.dto import MeterReadsResult, MeterRead, MeterReadsData


class TestMeterReadsResult(unittest.TestCase):

    def test_deserialisation(self):
        json = """
        {
            "data":{
                "results":[
                    [
                        {
                            "id":"4c71505d-cbf3-4d2a-9354-21b325d18128",
                            "date":"2023-01-19T00:00:00.000Z",
                            "createdAt":"2023-01-19T18:55:45.769Z",
                            "updatedAt":"2023-01-19T18:55:45.769Z",
                            "source":"SMR",
                            "value":2616,
                            "quality":"Normal",
                            "sequenceType":"Normal",
                            "registerIndustryId":"1",
                            "meterIndustryId":"A1B23456789012",
                            "status":"accepted",
                            "submissionClient":"unknown",
                            "accountId":"9bea007b-05ac-4e4a-b996-230e91b21318",
                            "agreementId":"a50b336b-4fac-4157-95ce-8ef1b0355219",
                            "meterPointIndustryId":"1234567890"
                        }
                    ],
                    [
                        {
                            "id":"c9fd402b-e527-4bd7-be4f-0ff57c3dacdc",
                            "date":"2023-01-18T00:00:00.000Z",
                            "createdAt":"2023-01-18T18:28:09.332Z",
                            "updatedAt":"2023-01-18T18:28:09.332Z",
                            "source":"SMR",
                            "value":2611,
                            "quality":"Normal",
                            "sequenceType":"Normal",
                            "registerIndustryId":"1",
                            "meterIndustryId":"A1B23456789012",
                            "status":"accepted",
                            "submissionClient":"unknown",
                            "accountId":"9bea007b-05ac-4e4a-b996-230e91b21318",
                            "agreementId":"a50b336b-4fac-4157-95ce-8ef1b0355219",
                            "meterPointIndustryId":"1234567890"
                        }
                    ]
                ]
            },
            "status":"success"
        }
        """
        entity = MeterReadsResult.from_json(json)
        self.assertEqual(entity.status, "success")
        self.assertIsInstance(entity.data, MeterReadsData)
        self.assertEqual(len(entity.data.results), 2)
        self.assertEqual(len(entity.data.results[0]), 1)
        self.assertIsInstance(entity.data.results[0][0], MeterRead)
        self.assertEqual(entity.data.results[0][0].id, "4c71505d-cbf3-4d2a-9354-21b325d18128")
        self.assertEqual(entity.data.results[1][0].id, "c9fd402b-e527-4bd7-be4f-0ff57c3dacdc")

