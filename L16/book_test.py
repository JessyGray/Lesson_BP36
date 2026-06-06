from lesson16_class.book import Book
from data17_10 import summ

book1 = Book("title1", "author1", 1050)
print(book1)
book2 = Book("title2", "author2", 2050)
book3 = Book("title3", "author1", 1350)
library_dict = {
    book1:5,
    book2:2,
    book3:15
}

# print(library_dict)
# for b,c in library_dict.items():
#     print(f"{b} - {c} copies")
#
# total_copies = sum(library_dict.values())
# different_book = len(library_dict)
# print( total_copies)
# print(different_book)

# book5 =Book()
# book1.info()
# book1.init("bbbbbb","ttttt",1000000)
# print(book1)
# print(summ(10,15))
print(book1.title)
book1.title="ogogogog"
print(book1.title)
book1.pages =-10000
print(book1)