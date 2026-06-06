class Computer:
    min_ram = 1024          # 1 GB
    max_ram = 1048576       # 1 TB

    min_ssd = 128           # 128 GB
    max_ssd = 10000000

    def __init__(self, brand: str, cpu: str, ram: int, ssd: int):
        self.__brand = "Unknown"
        self.__cpu = "Unknown"
        self.__ram = 0
        self.__ssd = 0

        self.set_brand(brand)
        self.set_cpu(cpu)
        self.set_ram(ram)
        self.set_ssd(ssd)

    def info(self):
        print("Brand", self.__brand)
        print("CPU", self.__cpu)
        print("RAM", self.__ram)
        print("SSD", self.__ssd)

    def __str__(self):
        return f"My computer is a {self.__brand} with {self.__cpu} CPU, ~{self.__ram} MB RAM, and ~{self.__ssd} MB SSD."

    def __repr__(self):
        return f"Computer('{self.__brand}', '{self.__cpu}', {self.__ram}, {self.__ssd})"

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        if isinstance(brand, str):
            brand = brand.strip()
            if len(brand) >= 2:
                self.__brand = brand

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        if isinstance(cpu, str):
            cpu = cpu.strip()
            if len(cpu) >= 2:
                self.__cpu = cpu

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        if isinstance(ram, int) and not isinstance(ram, bool):
            if self.min_ram <= ram <= self.max_ram:
                self.__ram = ram

    def get_ssd(self):
        return self.__ssd

    def set_ssd(self, ssd):
        if isinstance(ssd, int) and not isinstance(ssd, bool):
            if self.min_ssd <= ssd <= self.max_ssd:
                self.__ssd = ssd