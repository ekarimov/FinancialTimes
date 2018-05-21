#import pytest
import json

from tests.test_basic import TestCaseBase

class Test_API_parameters(TestCaseBase):

    def test_get_EUR__with_start_date_response_200(self):
        payload = {"start_date":"2018-05-14"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR__with_incorrect_start_date_response_422(self):
        payload = {"start_date":"incorrect"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 422