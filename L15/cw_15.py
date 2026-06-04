class Book:
    def __init__(self, author: str, title: str, pages: int):
        self.author = author
        self.title = title
        self.pages = pages

    def info(self):
        print("Author", self.author)
        print("Title", self.title)
        print("Pages", self.pages)

    def __str__(self):
        return f"Book of Title is {self.title}, writen by: {self.author}, pages of {self.pages}"


book1 = Book("Elatli", "Detective", 123)
book1.info()
print(book1)