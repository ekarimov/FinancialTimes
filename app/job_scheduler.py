from apscheduler.schedulers.blocking import BlockingScheduler
from app.db_methods import post_latest_exchange_rates


scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour=12)
def post_latest_EUR_exchage_rates():
    post_latest_exchange_rates('EUR')


if __name__ == '__main__':
    scheduler.start()
