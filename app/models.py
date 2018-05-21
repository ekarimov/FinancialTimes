from app import db


class Datapoint(db.Model):

    __table_args__ = (
        db.UniqueConstraint("base_currency_code", "date", "currency_code"),
    )

    id = db.Column(db.Integer, primary_key=True)
    base_currency_code = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    currency_code = db.Column(db.String, nullable=False)

    def __init__(self, base_currency_code, date, rate, currency_code):
        self.base_currency_code = base_currency_code
        self.date = date
        self.rate = rate
        self.currency_code = currency_code

    def upsert(self):
        existing_datapoint = Datapoint.query \
            .filter(Datapoint.base_currency_code == self.base_currency_code) \
            .filter(Datapoint.date == self.date) \
            .filter(Datapoint.currency_code == self.currency_code) \
            .first()
        if existing_datapoint:
            existing_datapoint.rate = self.rate
        else:
            db.session.add(self)