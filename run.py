from app import app, db
from app.db_methods import post_historical_exchange_rates
from app.views import exchange_rates_bp


if __name__ == '__main__':
    db.create_all(app=app)
    post_historical_exchange_rates('EUR', app.config['HISTORICAL_INTERVAL_DAYS'])
    app.register_blueprint(exchange_rates_bp)
    app.run(host="0.0.0.0", port=app.config['PORT'])