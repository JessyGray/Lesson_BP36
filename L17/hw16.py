#@property

class Computer:
    def __init__(self, brand: str, cpu: str, ram: int, ssd: int):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand:str):
        if isinstance(brand, str) and brand.strip():
            self.__brand = brand.strip()
        else:
            raise ValueError("Brand must be a non empty string")

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        if isinstance(cpu, str) and cpu.strip():
            self.__cpu = cpu.strip()
        else:
            raise ValueError("Cpu must be a non empty string")

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram):
        if isinstance(ram, int) and not isinstance(ram, bool) and ram>0:
            self.__ram = ram
        else:
            raise ValueError("Ram must be a positive integer")

    @property
    def ssd(self):
        return self.__ssd

    @ssd.setter
    def ssd(self, ssd):
        if isinstance(ssd, int) and not isinstance(ssd, bool) and ssd > 0:
            self.__ssd = ssd
        else:
            raise ValueError("Ssd must be a positive integer")

    def __str__(self):
        return f"Computer: brand {self.brand}, cpu {self.cpu}, ram {self.ram}, ssd {self.ssd}"


    def __repr__(self):
        return f"\nComputer( brand='{self.brand}', cpu='{self.cpu}', ram='{self.ram}, ssd='{self.ssd}')"
try:
    comp1 = Computer("Brand1", "CPU1", 1600, 256)
except ValueError as e:
    print(f"Error: {e}")
comp2 = Computer("Brand2", "CPU2", 4096, 512)
comp3 = Computer("Brand1", "CPU3", 8192, 1024)
comp4 = Computer("Brand3", "CPU4", 4096, 1024)

try:
    comp5 = Computer(1111, "CPU1", -1600, -256)
except ValueError as e:
    print(f"Error: {e}")
# print(comp5)
comps = [comp1, comp2, comp3, comp4]

print("All computers")
# for c in comps:
#     print(c)
print(comps)
print("Computers with RAM > 2000 MB:")
for c in comps:
    if c.ram > 2000:
        print(c)

print(comp1.ram)
comp1.ram = 2000
print(comp1.ram)
#comp1.set_ram(1000) comp1.get_ram()
# class Product:
#     def __init__(self, name: str, price: float, code: int, unit: str):
#         self.name = name
#         self.price = price
#         self.code = code
#         self.unit = unit
#
#     def __str__(self):
#         return f"Product: name: {self.name}, price {self.price}, code {self.code}, unit {self.unit}"
#
#
# p1 = Product("Name1", 7.9, 101, "1 liter")
# p2 = Product("Name2", 17.9, 102, "1 item")
# p3 = Product("Name3", 3., 103, "1.5 liter")
# p4 = Product("Name4", 117.9, 104, "1 kg")
# p5 = Product("Name5", 10.5, 105, "2 liter")
#
# mini_market = [p1, p2, p3, p4, p5]
# print("All products")
# for p in mini_market:
#     print(p)
# print("Products with unit liter")
# for p in mini_market:
#     if "liter" in p.unit:
#        print(p)
#
#
# class Movie:
#     def __init__(self, title:str, genre: str, year: int, rating: float):
#         self.title = title
#         self.genre = genre
#         self.year = year
#         self.rating = rating
#
#     def __str__(self):
#         return f"Movie: {self.title}, {self.genre}, {self.year}, rating: {self.rating}"
#
#     def __repr__(self):
#         return f"Movie:(title={self.title}, genre={self.genre}, year={self.year}, rating={self.rating})"
#
# m1 = Movie("M1", "g1", 2014, 8.7)
# m2 = Movie("M2", "g1", 2024, 9.7)
# m3 = Movie("M3", "g2", 2000, 6.8)
# m4 = Movie("M4", "g3", 2020, 7.3)
#
# movies = [m1,m2,m3,m4]
# print("All movies")
# for m in movies:
#     print(m)
#
# print(movies)
#
# class Book:  # title author pages constructor
#     # My book: <author> - title: <title> <pages> pages
#     title: str
#     author: str
#     pages: int
#
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"My book: {self.author} - title: {self.title} {self.pages} pages"
#
#
#     def __repr__(self):
#         return f"{self.title} by {self.author}"
#
# book1 = Book("title1", "author1", 1050)
# # print(book1)
# book2 = Book("title2", "author2", 2050)
# book3 = Book("title3", "author1", 1350)
# library_dict = {
#     book1:5,
#     book2:2,
#     book3:15
# }
#
# print(library_dict)
# for b,c in library_dict.items():
#     print(f"{b} - {c} copies")
#
# total_copies = sum(library_dict.values())
# different_book = len(library_dict)
# print( total_copies)
# print(different_book)
