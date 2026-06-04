class Car:
    def __init__(self, model:str, year:int, color:str):
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        print("Model:",self.model)
        print("Year:", self.year)
        print("Color:",self.color)

    def __str__(self):
        return f"Model: {self.model}, color: {self.color}, year of issue: {self.year}"



car1 = Car("Toyota", 2020, "white" )
print(car1.color)
print(car1)
car1.info()
Car.info(car1)

