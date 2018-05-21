import json
import unittest
import os

from datetime import datetime
from flask import current_app
from app import get_app, db
from app.views import exchange_rates_bp
from app.models import Datapoint

class TestCaseBase(unittest.TestCase):

    def _make_app(self):
        app = get_app()
        app.config.from_object('config.TestingConfig')
        db.init_app(app)
        db.create_all(app=app)
        return app, db

    @property
    def test_data(self):
        return self._read_test_data()

    def _read_test_data(self, filename='test_data.json'):
        tests_folder = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(tests_folder, 'test_data', filename)
        with open(path) as file:
            return json.load(file)

    def _prepare_test_data(self):
        for ex_rate in self.test_data:
            self.db.session.add(Datapoint(base_currency_code=ex_rate['base_currency_code'],
                      currency_code=ex_rate['currency_code'],
                      date=datetime.strptime(ex_rate['date'], "%Y-%m-%d").date(),
                      rate=ex_rate['rate']))
        self.db.session.commit()

    def _prepare_app(self):
        self.app, self.db = self._make_app()
        self.app.register_blueprint(exchange_rates_bp)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def setUp(self):
        self._prepare_app()
        self._prepare_test_data()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertTrue(current_app is not None)