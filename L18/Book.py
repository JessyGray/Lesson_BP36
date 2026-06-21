class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and title.strip():
            self.__title = title
        else:
            raise ValueError("title must be a non-empty string")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and author.strip():
            self.__author = author
        else:
            raise ValueError("author must be a non-empty string")

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if isinstance(pages, int) and not isinstance(pages, bool) and pages > 0:
            self.__pages = pages
        else:
            raise ValueError("pages must be a positive integer")

    def __str__(self):
        return f"Book: title: {self.title}, author: {self.author}, pages: {self.pages}"

    def __repr__(self):
        return self.__str__()


class FictionBook(Book):
    def __init__(self, title: str, author: str, pages: int, genre: str):
        super().__init__(title, author, pages)
        self.genre = genre

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and genre.strip():
            self.__genre = genre
        else:
            raise ValueError("genre must be a non-empty string")

    def __str__(self):
        return f"{super().__str__()}, genre: {self.genre}"

    def __repr__(self):
        return self.__str__()


class KidsFictionBook(FictionBook):
    min_age = 0
    max_age = 18

    def __init__(self, title: str, author: str, pages: int, genre: str, age: int):
        super().__init__(title, author, pages, genre)
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if (
            isinstance(age, int)
            and not isinstance(age, bool)
            and self.min_age <= age <= self.max_age
        ):
            self.__age = age
        else:
            raise ValueError("age must be an integer from 0 to 18")

    def __str__(self):
        return f"{super().__str__()}, age: {self.age}"

    def __repr__(self):
        return self.__str__()


class EducationBook(Book):
    def __init__(self, title: str, author: str, pages: int, subject: str):
        super().__init__(title, author, pages)
        self.subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if isinstance(subject, str) and subject.strip():
            self.__subject = subject
        else:
            raise ValueError("subject must be a non-empty string")

    def __str__(self):
        return f"{super().__str__()}, subject: {self.subject}"

    def __repr__(self):
        return self.__str__()


class SchoolBook(EducationBook):
    min_age = 6
    max_age = 18

    def __init__(self, title: str, author: str, pages: int, subject: str, age: int):
        super().__init__(title, author, pages, subject)
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if (
            isinstance(age, int)
            and not isinstance(age, bool)
            and self.min_age <= age <= self.max_age
        ):
            self.__age = age
        else:
            raise ValueError("age must be an integer from 6 to 18")

    def __str__(self):
        return f"{super().__str__()}, age: {self.age}"

    def __repr__(self):
        return self.__str__()


book1 = Book("Clean Code", "Robert Martin", 464)
book2 = Book("Python Basics", "John Smith", 250)

fiction1 = FictionBook("Harry Potter", "J. K. Rowling", 350, "Fantasy")
fiction2 = FictionBook("Sherlock Holmes", "Arthur Conan Doyle", 300, "Detective")

kids1 = KidsFictionBook("Alice in Wonderland", "Lewis Carroll", 180, "Fantasy", 10)
kids2 = KidsFictionBook("The Little Prince", "Antoine de Saint-Exupery", 120, "Adventure", 8)

education1 = EducationBook("Physics Fundamentals", "David Halliday", 500, "Physics")
education2 = EducationBook("English Grammar", "Raymond Murphy", 390, "English")

school1 = SchoolBook("Algebra 7", "Brown", 220, "Mathematics", 13)
school2 = SchoolBook("Biology 9", "Miller", 280, "Biology", 15)

books = [
    book1,
    book2,
    fiction1,
    fiction2,
    kids1,
    kids2,
    education1,
    education2,
    school1,
    school2,
]

for book in books:
    print(book)