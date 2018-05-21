from datetime import datetime
from flask import Blueprint, request, jsonify, current_app, Response, make_response
from sqlalchemy.sql import func
from app.models import Datapoint
from app.validators import Check

exchange_rates_bp = Blueprint('exchange_rates_bp', __name__, url_prefix='/exchange_rates')


@exchange_rates_bp.route('/<base_currency_code>/', methods=['GET'])
def get_exchange_rates(base_currency_code):
    """
    URL examples:
         exchange_rates/EUR?currency_codes=USD,AUD
         exchange_rates/EUR?currency_codes=USD,AUD&start_date=2018-01-31
         exchange_rates/EUR?currency_codes=USD,AUD&start_date=2018-01-31&end_date=2018-02-15
    """

    validation_error = Check(request.args).validate()
    if validation_error is not None:
        return make_response(validation_error, 422)

    currency_codes = request.args.get('currency_codes')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    exchange_rates = Datapoint.query.filter(Datapoint.base_currency_code == base_currency_code)

    if currency_codes is not None:
        currency_codes = currency_codes.split(',')
        exchange_rates = exchange_rates.filter(Datapoint.currency_code.in_(currency_codes))
    if start_date:
        start_date = datetime.strftime(start_date, "%Y-%m-%d")
        exchange_rates = exchange_rates.filter(Datapoint.date >= start_date)
    if end_date:
        end_date = datetime.strftime(end_date, "%Y-%m-%d")
        exchange_rates = exchange_rates.filter(Datapoint.date <= end_date)

    exchange_rates.order_by(Datapoint.base_currency_code, Datapoint.date, Datapoint.currency_code).all()

    return jsonify([ex_rate.serialized for ex_rate in exchange_rates])


@exchange_rates_bp.route('/<base_currency_code>/average', methods=['GET'])
def get_average_rates(base_currency_code):
    """
    URL examples:
         exchange_rates/EUR/average?currency_codes=USD,AUD
         exchange_rates/EUR?currency_codes=USD,AUD&start_date=2018-01-31
         exchange_rates/EUR?currency_codes=USD,AUD&start_date=2018-01-31&end_date=2018-02-15
    """

    validation_error = Check(request.args).validate()
    if validation_error is not None:
        return make_response(validation_error, 422)

    result = []
    currency_codes = request.args.get('currency_codes')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    exchange_rates = Datapoint.query.filter(Datapoint.base_currency_code == base_currency_code)

    if currency_codes is not None:
        currency_codes = currency_codes.split(',')
        exchange_rates = exchange_rates.filter(Datapoint.currency_code.in_(currency_codes))

    if start_date is None:
        start_date = exchange_rates.with_entities(func.min(Datapoint.date).label('min_date')).first()
        start_date = start_date.min_date
    else:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        exchange_rates = exchange_rates.filter(Datapoint.date >= start_date)

    if end_date is None:
        end_date = exchange_rates.with_entities(func.max(Datapoint.date).label('max_date')).first()
        end_date = end_date.max_date
    else:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        end_date = exchange_rates.filter(Datapoint.date >= end_date)

    exchange_rates = exchange_rates.\
        group_by(Datapoint.currency_code).\
        with_entities(Datapoint.currency_code,func.avg(Datapoint.rate).label('average')).\
        all()

    for exchange_rate in exchange_rates:
        result.append({
            'base_currency_code':base_currency_code,
            'currency_code':exchange_rate.currency_code,
            'average_rate':exchange_rate.average,
            'start_date':datetime.strftime(start_date, "%Y-%m-%d"),
            'end_date':datetime.strftime(end_date, "%Y-%m-%d")
        })

    return jsonify(result)