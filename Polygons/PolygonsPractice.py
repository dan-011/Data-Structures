import unittest
from InheritanceMod import Polygon, Square

class TestPolygon(unittest.TestCase):
    def test_init(self):
        p1 = Polygon("Triangle", 3, 2)
        self.assertEqual(p1.name, "Triangle")
        self.assertEqual(p1.sidelength, 2)
        self.assertEqual(p1.numberOfSides, 3)
    def test_get_shape(self):
        p1 = Polygon("Triangle", 3, 2)
        self.assertEqual(p1.get_shape(), "The shape is Triangle")
    def test_perimeter(self):
        p1 = Polygon("Triangle", 3, 2)
        self.assertEqual(p1.perimeter(), 6)
    
class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.name, "Square")
        self.assertEqual(s1.sidelength, 5)
        self.assertEqual(s1.numberOfSides, 4)
    def test_get_shape(self):
        s1 = Square(5)
        self.assertEqual(s1.get_shape(), "The shape is Square")
    def test_perimeter(self):
        s1 = Square(5)
        self.assertEqual(s1.perimeter(), 20)
    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
    def test_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "Square(side length = 5)")

#unittest.main()

#import InheritanceMod

print("what's up")
if __name__ == '__main__':
    print("the practice isn't being imported")
else:
    print("the practice is being imported")
