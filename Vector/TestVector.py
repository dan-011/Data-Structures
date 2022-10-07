import unittest
from Vector import Vector, RecVec, PolVec

class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(NotImplementedError):
            v1 = Vector()
    def test_add(self):
        with self.assertRaises(TypeError):
            r1 = RecVec(3,4)
            r1 + 1
    def test_sub(self):
        with self.assertRaises(TypeError):
            p2 = PolVec(5, 30)
            p2 - 2
    def test_eq(self):
        with self.assertRaises(TypeError):
            r3 = RecVec(5,6)
            r3 == 3
            #return a typeerror for add, sub, and eq if the inputs aren't vectors

    #def test
    #self.assertEqual()

#do the test cases have to be different or can they just all be the same
#Also, is there a better way to do this than just copying and pasting the test object
#should we test the init function
class TestRecVec(unittest.TestCase):
    def test_init(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
    def test_str(self):
        r1 = RecVec(3, 4)
        self.assertEqual(str(r1), "RecVec(x = 3, y = 4)")
    def test_add(self):
        #is this working as intended
        r1 = RecVec(3, 4)
        r2 = RecVec(5, 6)
        self.assertEqual(r1 + r2, RecVec(8, 10))
    def test_sub(self):
        r1 = RecVec(3, 4)
        r2 = RecVec(5, 6)
        self.assertEqual(r1 - r2, RecVec(-2, -2))
    def test_eq(self):
        r1 = RecVec(3, 3)
        r2 = RecVec(3, 3)
        self.assertEqual(r1 == r2, True)
    def test_rectangular(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(p1.rectangular(), RecVec(3, 4))
    def test_polar(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.polar(), PolVec(5, 53.13))
    def test_get_x(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.get_x(), 3)
    def test_get_y(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.get_y(), 4)
    def test_get_mag(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.get_mag(), 5)
    def test_get_ang(self):
        r1 = RecVec(3, 4)
        self.assertEqual(round(r1.get_ang(),3), 53.130)

class TestPolVec(unittest.TestCase):
    def test_init(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(p1.mag, 5)
        self.assertEqual(p1.angle, 53.13)
    def test_str(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(str(p1), "PolVec(mag = 5, angle = 53.13)")
    def test_add(self):
        #is this working as intended
        p1 = PolVec(5, 53.13)
        p2 = PolVec(6, 30)
        self.assertEqual(p1 + p2, PolVec(10.779, 40.500))
    def test_sub(self):
        p1 = PolVec(5, 53.13)
        p2 = PolVec(6, 30)
        self.assertEqual(p1 - p2, PolVec(2.413, -24.483))
    def test_eq(self):
        p1 = PolVec(5, 53.13)
        p2 = PolVec(5, 53.13)
        self.assertEqual(p1 == p2, True)
    def test_rectangular(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(p1.rectangular(), RecVec(3, 4))
    def test_polar(self):
        r1 = RecVec(3, 4)
        self.assertEqual(r1.polar(), PolVec(5, 53.13))
    def test_get_x(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(round(p1.get_x(), 3), 3) #may need to remove round
    def test_get_y(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(round(p1.get_y(), 3), 4) #may need to remove round
    def test_get_mag(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(p1.get_mag(), 5)
    def test_get_ang(self):
        p1 = PolVec(5, 53.13)
        self.assertEqual(p1.get_ang(), 53.13)

unittest.main()