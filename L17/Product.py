class Product:
    def __init__(self, name: str, price: float, unit: str, code: str, kosher: bool):
        self.name = name
        self.price = price
        self.unit = unit
        self.code = code
        self.kosher = kosher

    def __str__(self):
        return (
            f"name: {self.name}, "
            f"price: {self.price}, "
            f"unit: {self.unit}, "
            f"code: {self.code}, "
            f"kosher: {self.kosher}"
        )

    def __repr__(self):
        return (
            f"Product(name='{self.name}', price={self.price}, unit='{self.unit}', "
            f"code={self.code}, kosher={self.kosher})"
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float | int) and not isinstance(price, bool) and price > 0:
            self.__price = price
        else:
            raise ValueError("Name must be a non-negative number")

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if isinstance(unit, str) and unit.strip():
            self.__unit = unit.strip()
        else:
            raise ValueError("Unit must be a non-empty string")

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        if isinstance(code, str) and code.isdigit():
            self.__code = code

        else:
            raise ValueError("Code must be a non-empty string")

    @property
    def kosher(self):
        return self.__kosher

    @kosher.setter
    def kosher(self, kosher):
        if isinstance(kosher, bool):
            self.__kosher = kosher
        else:
            raise ValueError("Kosher must be True or False")

"""
                Book                       Age
                 -----
                 title
                 author
                 pages
      |              |                
    FictionBook    EducationBook
    -----------    ------------
    genre             subject  
       |                    |
    KidsFictionBook (age)  SchoolBook(age)
    --------------         ----------------
    age
10 obj
"""