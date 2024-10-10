class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year
  def get_info(self):
    return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

class Circle:
  def __init__(self, radius):
    self.radius = radius
  def get_radius(self):
    return self.radius
  def set_radius(self,radius):
    self.radius = radius

b=Book("Война и мир", "Лев Толстой", "1869")
print(b.get_info())
c=Circle(5)
print(c.get_radius())
c.set_radius(10)
print(c.get_radius())