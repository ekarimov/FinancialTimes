#import pytest
import json

from tests.test_basic import TestCaseBase

class Test_basic_rates_API_parameters(TestCaseBase):

    def test_get_EUR_with_start_date_response_200(self):
        payload = {"start_date":"2018-05-14"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_end_date_response_200(self):
        payload = {"end_date":"2018-05-14"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_start_end_date_response_200(self):
        payload = {"start_date":"2018-05-14", "end_date":"2018-05-15"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_incorrect_start_date_response_422(self):
        payload = {"start_date":"incorrect"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 422

    def test_get_EUR_with_incorrect_end_date_response_422(self):
        payload = {"end_date":"incorrect"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 422

    def test_get_EUR_with_start_date_more_than_end_date_response_422(self):
        payload = {"start_date": "2018-05-15", "end_date": "2018-05-14"}
        response = self.client.get('/exchange_rates/EUR', query_string=payload)
        assert response.status_code == 422


class Test_average_rates_API_parameters(TestCaseBase):

    def test_get_EUR_with_start_date_response_200(self):
        payload = {"start_date":"2018-05-14"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_end_date_response_200(self):
        payload = {"end_date":"2018-05-15"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_start_end_date_response_200(self):
        payload = {"start_date":"2018-05-14", "end_date":"2018-05-15"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 200

    def test_get_EUR_with_incorrect_start_date_response_422(self):
        payload = {"start_date":"incorrect"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 422

    def test_get_EUR_with_incorrect_end_date_response_422(self):
        payload = {"end_date":"incorrect"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 422

    def test_get_EUR_with_start_date_more_than_end_date_response_422(self):
        payload = {"start_date": "2018-05-15", "end_date": "2018-05-14"}
        response = self.client.get('/exchange_rates/EUR/average', query_string=payload)
        assert response.status_code == 422