from datetime import date, timedelta


class ProductDate:
    def __init__(self, manufacture_date: date, self_life_days: int):
        self.manufacture_date = manufacture_date
        self.self_life_days = self_life_days

    @property
    def manufacture_date(self):
        return self.__manufacture_date

    @manufacture_date.setter
    def manufacture_date(self, manufacture_date):
        if isinstance(manufacture_date, date):
            self.__manufacture_date = manufacture_date
        else:
            raise ValueError("manufacture date must be date")

    @property
    def self_life_days(self):
        return self.__self_life_days

    @self_life_days.setter
    def self_life_days(self, self_life_days):
        if isinstance(self_life_days, int) and not isinstance(self_life_days, bool) and self_life_days > 0:
            self.__self_life_days = self_life_days
        else:
            raise ValueError("self life days must be a positive number")

    @property
    def expiration_date(self):
        return self.manufacture_date + timedelta(days=self.self_life_days)

    def date_info(self):
        return f"manufacture_date: {self.manufacture_date}, expiration_date: {self.expiration_date}"
