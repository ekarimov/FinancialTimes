from app import app
from app.db_methods import post_historical_exchange_rates, post_latest_exchange_rates


if __name__ == '__main__':
    post_historical_exchange_rates('EUR', app.config['HISTORICAL_INTERVAL_DAYS'])
    app.run(host="0.0.0.0", port=app.config['PORT'])