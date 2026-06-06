class Computer:
    def __init__(self, brand: str, cpu: str, ram: int, ssd: int):
        self.__brand = brand
        self.__cpu = cpu
        self.__ram = ram
        self.__ssd = ssd

    def info(self):
        print("Brand", self.brand)
        print("CPU", self.cpu)
        print("RAM", self.ram)
        print("SSD", self.ssd)

    def __str__(self):
        return f"My computer is a {self.brand} with {self.cpu} CPU, ~{self.ram} MB RAM, and ~{self.ssd} MB SSD."