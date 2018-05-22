import json
from tests.test_basic import TestCaseBase


class TestAPI(TestCaseBase):

    def test_get_EUR_response_200(self):
        response = self.client.get('/exchange_rates/EUR')
        assert response.status_code == 200

    def test_get_EUR_average_response_200(self):
        response = self.client.get('/exchange_rates/EUR/average')
        assert response.status_code == 200


class TestApiValidateData(TestCaseBase):

    def test_get_EUR(self):
        response = self.client.get('/exchange_rates/EUR')
        self.assertEqual(self.test_data, json.loads(response.get_data(as_text=True)))
