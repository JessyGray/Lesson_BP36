class Product:
    def __init__(self, name: str, price: float, unit: str, code: str, kosher: bool):
        self.__name = "Unknown"
        self.__price = 0
        self.__unit = "unit"
        self.__code = "0000"
        self.__kosher = False

        self.set_name(name)
        self.set_price(price)
        self.set_unit(unit)
        self.set_code(code)
        self.set_kosher(kosher)

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"({self.__name}, {self.__price})"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_price(self, price):
        if isinstance(price, float | int) and not isinstance(price, bool):
            if price > 0:
                self.__price = price

    def get_price(self):
        return self.__price

    def get_unit(self):
        return self.__unit

    def set_unit(self, unit):
        if isinstance(unit, str):
            self.__unit = unit

    def get_code(self):
        return self.__code

    def set_code(self, code):
        if isinstance(code, str) and code.isdigit():
            self.__code = code

    def get_kosher(self):
        return self.__kosher

    def set_kosher(self, kosher):
        if isinstance(kosher, bool):
            self.__kosher = kosher
# getters setters
