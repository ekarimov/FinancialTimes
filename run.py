from app import app
from app.get_historical_data import get_historical_exchange_rates


if __name__ == '__main__':
    get_historical_exchange_rates('EUR', app.config['HISTORICAL_INTERVAL_DAYS'])
    app.run(host="0.0.0.0", port=app.config['PORT'])