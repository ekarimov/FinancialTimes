from datetime import datetime


class Check:
    """Collectin of argument validation functions."""

    def __init__(self, args):
        self.currency_codes = args.get('currency_codes')
        self.start_date = args.get('start_date')
        self.end_date = args.get('end_date')

    def validate_date_format(self):
        if self.start_date:
            try:
                self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
            except:
                raise ValueError('Incorrect start date format, should be %Y-%m-%d')

        if self.end_date:
            try:
                self.end_date = datetime.strptime(self.end_date, "%Y-%m-%d")
            except:
                raise ValueError('Incorrect end date format, should be %Y-%m-%d')

    def start_is_not_in_future(self):
        if self.start_date:
            current_date = datetime.date(datetime.utcnow())
            if self.start_date > current_date:
                raise ValueError("Start date can't be in future")

    def end_date_after_start_date(self):
        if self.end_date and self.start_date:
            if self.end_date < self.start_date:
                raise ValueError("Start date can't be more than end date")

    def validate(self):
        try:
            self.validate_date_format()
            self.start_is_not_in_future()
            self.end_date_after_start_date()
        except Exception as e:
            return str(e)
        return None