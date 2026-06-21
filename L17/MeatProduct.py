from lesson17_inheritance.Product import Product


class MeatProduct(Product):
    def __init__(self, name: str, price: float, unit: str, code: str, kosher: bool, meat_type: str):
        super().__init__(name, price, unit, code, kosher)
        self.meat_type = meat_type

    @property
    def meat_type(self):
        return self.__meat_type

    @meat_type.setter
    def meat_type(self, meat_type):
        allow_types = ["mutton", "pork", "beef", "turkey", "chicken"]
        if isinstance(meat_type, str) and meat_type.strip().lower() in allow_types:
            self.__meat_type = meat_type.strip().lower()
        else:
            raise ValueError(f"Meat type must be one of:{allow_types} ")

    def __str__(self):
        return super().__str__() + f", meat_type: {self.meat_type}"

    def __repr__(self):
        return (f"MeatProduct(name='{self.name}', price= '{self.price}', unit='{self.unit}', "
                f"code='{self.code}', kosher='{self.kosher}', meat_type='{self.meat_type}') ")