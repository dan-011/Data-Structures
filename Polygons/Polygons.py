class Polygon:
    def __init__(self, name, numberOfSides, sidelength):
        self.name = name
        self.numberOfSides = numberOfSides
        self.sidelength = sidelength
        self._no = True

    def get_shape(self):
        return "The shape is {}".format(self.name)
    
    def perimeter(self):
        return self.numberOfSides * self.sidelength
    def get_no(self):
        return self._no

class Square(Polygon):
    def __init__(self, sidelength):
        super().__init__("Square", 4, sidelength)
        
    def area(self):
        return self.sidelength**2

    def __str__(self):
        return "Square(side length = {})".format(self.sidelength)


print("hello there")
if __name__ == '__main__':
    print("this isn't being imported")
else:
    print("the mod is being imported")

p1 = Polygon("Triangle", 3, 2)
print(p1.get_no())
s1 = Square(5)
print(s1.get_no())
