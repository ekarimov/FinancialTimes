#import pytest
import json

from tests.test_basic import TestCaseBase

class Test_API(TestCaseBase):

    def test_get_EUR_currency_code_response_200(self):
        response = self.client.get('/exchange_rates/EUR')
        assert response.status_code == 200

    def test_get_EUR_average_currency_code_response_200(self):
        response = self.client.get('/exchange_rates/EUR/average')
        assert response.status_code == 200