from datetime import datetime
from app.fixer_api_methods import get_historical_currency_rates, get_current_currency_rates
from tests.test_basic import TestCaseBase


class TestFixerAPI(TestCaseBase):

    def test_get_historical_currency_rates(self):
        get_historical_currency_rates('EUR', datetime.strptime("2018-01-01", "%Y-%m-%d").date())
        assert True

    def test_get_current_currency_rates(self):
        get_current_currency_rates('EUR')
        assert True