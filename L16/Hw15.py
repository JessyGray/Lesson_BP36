# TASK 1


class Computer:
    def __init__(self, brand: str, cpu: str, ram: int, ssd: int):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def info(self):
        print("Brand", self.brand)
        print("CPU", self.cpu)
        print("RAM", self.ram)
        print("SSD", self.ssd)

    def __str__(self):
        return f"My computer is a {self.brand} with {self.cpu} CPU, ~{self.ram} MB RAM, and ~{self.ssd} MB SSD."


computer1 = Computer("MSI", "Intel Core i7", 16000, 512000)
computer2 = Computer("Dell", "Intel Core i5", 8000, 256000)
computer3 = Computer("HP", "AMD Ryzen 5", 1000, 256000)
computer4 = Computer("Lenovo", "Intel Core i3", 1500, 128000)
computer5 = Computer("ASUS", "AMD Ryzen 7", 32000, 1024000)

devices = [computer1, computer2, computer3, computer4, computer5]

for computer in devices:
    print(computer)

print()

for computer in devices:
    if computer.ram > 2000:
        print(computer)

print()


# TASK 2
class Product:
    def __init__(self, name: str, price: float, code: int, unit: str):
        self.name = name
        self.price = price
        self.code = code
        self.unit = unit

    def info(self):
        print("Name", self.name)
        print("Price", self.price)
        print("Code", self.code)
        print("Unit", self.unit)

    def __str__(self):
        return f"Product {self.name}, price: {self.price}, code: {self.code}, unit: {self.unit}"


product1 = Product("Onion", 15.2, 23423, "kg")
product2 = Product("Milk", 8.9, 234677, "liter")
product3 = Product("Cheese", 23.4, 238878, "kg")
product4 = Product("Coca-cola", 8.6, 234967, "liter")
product5 = Product("Nuts", 55.5, 232223, "kg")

mini_market = [product1, product2, product3, product4, product5]

for product in mini_market:
    print(product)

print()

for product in mini_market:
    if product.unit == "liter":
        print(product)

print()


# TASK 3

class Employee:
    def __init__(self, name: str, position: str, salary: float, department: str):
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department

    def info(self):
        print("Name", self.name)
        print("Position", self.position)
        print("Salary", self.salary)
        print("Department", self.department)

    def __str__(self):
        return f"Employee {self.name}, position: {self.position}, salary: {self.salary}, department: {self.department}"


employee1 = Employee("Jessy", "Manager", 5000, "Sales")
employee2 = Employee("Alex", "Developer", 7000, "IT")
employee3 = Employee("Kate", "Accountant", 4500, "Finance")
employee4 = Employee("Michel", "System Administrator", 6500, "IT")
employee5 = Employee("John", "HR Specialist", 4000, "HR")

employees = [employee1, employee2, employee3, employee4, employee5]

for employee in employees:
    print(employee)

print()

for employee in employees:
    if employee.department == "IT":
        print(employee)

print()


# TASK 4
class Book:  # title author pages constructor
    title: str
    author: str
    pages: int

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"My book: {self.author} - title: {self.title} {self.pages} pages"


book1 = Book("title1", "author1", 1050)
book2 = Book("title2", "author2", 2050)
book3 = Book("title3", "author1", 1350)

library = [book1, book2, book3]
library_dict = {book1: 5, book2: 2, book3: 15}

for a, b in library_dict.items():
    print(a, ",", b, "copies")
