class Book:  # title author pages constructor
    # My book: <author> - title: <title> <pages> pages
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
# print(book1)
book2 = Book("title2", "author2", 2050)
book3 = Book("title3", "author1", 1350)

library = [book1, book2, book3]

for b in library:
    print(b)

print("+" * 30)
for b in library:
    if b.author == "author1":
        print(b)
