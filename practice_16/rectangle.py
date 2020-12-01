class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
#Method to calculate rectangle area
    def getArea(self):
        return self.width * self.height