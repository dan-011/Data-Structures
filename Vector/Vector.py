from math import sin, cos, tan, asin, acos, atan, pi
class Vector:
    #is what I did, puting a hidden x attribute in the PolVec class, allowed?
    def __init__(self):
        raise NotImplementedError
    def __add__(self, other):
        if not(isinstance(self, Vector)) or not(isinstance(other, Vector)):
            raise TypeError
        x1 = self.x + other.x
        y1 = self.y + other.y
        #do both have to be the same?
        #is there a smoother way to do this than checking the type of the vector?
        if isinstance(self, RecVec):
            return RecVec(x1, y1)
        elif isinstance(self, PolVec):
            return RecVec(x1, y1).polar()
        else:
            return Vector(x1, y1)
    def __sub__(self, other):
        if not(isinstance(self, Vector)) or not(isinstance(other, Vector)):
            raise TypeError
        x1 = self.x - other.x
        y1 = self.y - other.y
        if isinstance(self, RecVec):
            return RecVec(x1, y1)
        elif isinstance(self, PolVec):
            return RecVec(x1, y1).polar()
        else:
            return Vector(x1, y1)
    def __eq__(self, other):
        if not(isinstance(self, Vector)) or not(isinstance(other, Vector)):
            raise TypeError
        obj1 = self.rectangular()
        obj2 = other.rectangular()
        return (round(obj1.x,3) == round(obj2.x, 3)) and (round(obj1.y,3) == round(obj2.y, 3))
    def rectangular(self):
        return RecVec(self.x, self.y)
    def polar(self):
        return PolVec(self.mag, self.angle)

class RecVec(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = ((x**2)+(y**2))**(1/2)
        self.angle = atan(y/x)*(180/pi)
    def __str__(self):
        return "RecVec(x = {}, y = {})".format(self.x, self.y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_mag(self):
        return self.mag
    def get_ang(self):
        return self.angle

class PolVec(Vector):
    def __init__(self, mag, angle):
        self.mag = mag
        self.angle = angle
        #are we treating these like private variables?
        self.x = round(mag*cos(angle*(pi/180)), 3)
        self.y = round(mag*sin(angle*(pi/180)), 3)
        #how do we implement the parent in this initiate method
    def __str__(self):
        return "PolVec(mag = {}, angle = {})".format(self.mag, self.angle)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_mag(self):
        return self.mag
    def get_ang(self):
        return self.angle
#r1 = RecVec(3,4)
#print(r1.polar())
#print(p1.rectangular())
#r2 = RecVec(5, 6)
#p2 = PolVec((5**2 + 6**2)**(1/2), atan(6/5)*(180/pi))
#p1 = PolVec(5, 53.13)

