class Employee:
    def __init__(self, name: str, position: str, salary: float, department: str):
        self.__name = name
        self.__position = position
        self.__salary = salary
        self.__department = department

    def info(self):
        print("Name", self.name)
        print("Position", self.position)
        print("Salary", self.salary)
        print("Department", self.department)

    def __str__(self):
        return f"Employee {self.__name}, position: {self.__position}, salary: {self.__salary}, department: {self.__department}"

    def __repr__(self):
        return f"Employee('{self.__name}', '{self.__position}', {self.__salary}, '{self.__department}')"

    def get.name():
