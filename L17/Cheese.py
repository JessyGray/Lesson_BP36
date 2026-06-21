from lesson17_inheritance.DairyProduct import DairyProduct


class Cheese(DairyProduct):
    #type_cheese  camembert maasdam gouda brie
    def __init__(self, name: str, price: float, unit: str, code: str, kosher: bool, milk_type: str, type_cheese: str):
        super().__init__(name, price, unit, code, kosher, milk_type)
        self.type_cheese = type_cheese

    @property
    def type_cheese(self):
        return self.__type_cheese

    @type_cheese.setter
    def type_cheese(self, type_cheese):
        allow_types3 = ["camembert", "maasdam", "gouda", "brie"]
        if isinstance(type_cheese, str) and type_cheese.strip().lower() in allow_types3:
            self.__type_cheese = type_cheese
        else:
            raise ValueError(f"Cheese type must be one of: {allow_types3}")

    def __str__(self):
        return super().__str__() + f", type_cheese: {self.type_cheese}"

    def __repr__(self):
        return (f"DairyProduct(name='{self.name}', price='{self.price}', unit='{self.unit}', "
                f"code='{self.code}', kosher='{self.kosher}', milk_type='{self.milk_type}', type_cheese='{self.type_cheese}')")


cheese1 = Cheese("brie1", 19.9, "150 gr", "12344707", False, "cow", "brie")
print(cheese1)
print(Cheese.mro())