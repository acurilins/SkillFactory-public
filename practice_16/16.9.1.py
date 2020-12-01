class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getLenght(self):
        return self.length

    def getWidth(self):
        return self.width

rect1 = Rectangle(
    input("Введите х\n"),
    input("Введите y\n"))

print("x = ", rect1.length)
print("y = ", rect1.width)
print("длина =", int(rect1.length) * 10)
print("ширина =", int(rect1.width) * 10)
