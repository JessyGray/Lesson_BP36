from datetime import date

from lesson17_inheritance.Product import Product
from lesson17_inheritance.ProductDate import ProductDate


class DairyProduct(Product, ProductDate):
    def __init__(self, name: str,
                 price: float,
                 unit: str,
                 code: str,
                 kosher: bool,
                 milk_type: str,
                 manufacture_date: date,
                 self_life_days: int):
        Product.__init__(self, name, price, unit, code, kosher)
        ProductDate.__init__(self, manufacture_date, self_life_days)
        self.milk_type = milk_type

    @property
    def milk_type(self):
        return self.__milk_type

    @milk_type.setter
    def milk_type(self, milk_type):
        allow_types = ["sheep", "lactose-free", "cow", "goat"]
        if isinstance(milk_type, str) and milk_type.strip().lower() in allow_types:
            self.__milk_type = milk_type.strip().lower()
        else:
            raise ValueError(f"Milk type must be one of:{allow_types} ")

    def __str__(self):
        return Product.__str__(self) + f", milk_type: {self.milk_type}, "+ ProductDate.date_info(self)

    def __repr__(self):
        return (f"DairyProduct(name='{self.name}', price= '{self.price}', unit='{self.unit}', "
                f"code='{self.code}', kosher='{self.kosher}', milk_type='{self.milk_type}') ")


milk1 = DairyProduct("butter", 9.9, "200 gr", "1234567", True, "cow", date(2026,6,8),10)

print(milk1)
print(type(milk1))
print(DairyProduct.mro())
