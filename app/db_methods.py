from datetime import datetime, timedelta
from app import db
from app.models import Datapoint
from app.fixer_api_methods import get_historical_currency_rates, get_current_currency_rates


def post_historical_exchange_rates(base_currency_code:str, time_interval_days:int):
    exchange_date = datetime.utcnow().date()
    target_date = exchange_date - timedelta(days=time_interval_days)
    historical_datapoints = Datapoint.query.with_entities(Datapoint.date).\
        distinct(Datapoint.date).\
        filter(Datapoint.base_currency_code == base_currency_code).\
        filter(Datapoint.date >= target_date).\
        order_by(Datapoint.date.desc()).\
        all()
    historical_datapoints_dates = [dp.date for dp in historical_datapoints]
    while exchange_date != target_date:
        exchange_date = exchange_date - timedelta(days=1)
        if exchange_date not in historical_datapoints_dates:
            exchange_rates = get_historical_currency_rates(base_currency_code, exchange_date)
            for currency_code, rate in exchange_rates.items():
                datapoint = Datapoint(base_currency_code=base_currency_code,
                                      date=exchange_date,
                                      rate=rate,
                                      currency_code=currency_code)
                datapoint.upsert()
            db.session.commit()


def post_latest_exchange_rates(base_currency_code:str):
    exchange_date = datetime.utcnow().date()
    exchange_rates = get_current_currency_rates(base_currency_code)
    for currency_code, rate in exchange_rates.items():
        datapoint = Datapoint(base_currency_code=base_currency_code,
                              date=exchange_date,
                              rate=rate,
                              currency_code=currency_code)
        datapoint.upsert()
    db.session.commit()
