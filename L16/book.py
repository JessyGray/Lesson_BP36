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


    def __repr__(self):
        return f"{self.title} by {self.author}"

    def info(self):
        print(f"{self.title}")

    def init(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages