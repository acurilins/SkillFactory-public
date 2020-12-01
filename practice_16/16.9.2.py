class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getLenght(self):
        return self.length

    def getWidth(self):
        return self.width

rect1 = Rectangle(20,16)

print("длина прямоугольника:", rect1.width)
print("ширина прямоугольника:", rect1.length)
