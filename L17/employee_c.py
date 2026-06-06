class Employee:
    min_salary = 5000
    max_salary = 100000

    def __init__(self, name: str, position: str, salary: float | int, department: str):
        self.__name = "Unknown"
        self.__position = "Unknown"
        self.__salary = 0.0
        self.__department = "Unknown"

        self.set_name(name)
        self.set_position(position)
        self.set_salary(salary)
        self.set_department(department)

    def info(self):
        print("Name", self.__name)
        print("Position", self.__position)
        print("Salary", self.__salary)
        print("Department", self.__department)

    def __str__(self):
        return f"Employee {self.__name}, position: {self.__position}, salary: {self.__salary}, department: {self.__department}"

    def __repr__(self):
        return f"Employee('{self.__name}', '{self.__position}', {self.__salary}, '{self.__department}')"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            name = name.strip()
            if len(name) >= 2:
                self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if isinstance(position, str):
            position = position.strip()
            if len(position) >= 2:
                self.__position = position

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if self.min_salary <= salary <= self.max_salary:
                self.__salary = salary

    def get_department(self):
        return self.__department

    def set_department(self, department):
        if isinstance(department, str):
            department = department.strip()
            if len(department) >= 2:
                self.__department = department