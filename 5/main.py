class Book:
    title = "Война и мир"
    author = "Лев Толстой"
    year = "1869"

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


class Circle(Book):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius


b = Book()
print(b.get_info())
c = Circle(5)
print(c.get_radius())
c.set_radius(10)
print(c.get_radius())
print(c.title)