class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return (((self.x)**2)+((self.y)**2))**(1/2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin() 
    
    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __str__(self):
        return "Point({}, {})".format(self.x,self.y)

if __name__ == '__main__':
    p1 = Point(3, 4)    #dist = 5
    p2 = Point(5, 6)    #dist = 7.81 = sqrt(61)
    p3 = Point(4, 3)    #dist = 5
    p4 = Point(5, 6)    #dist = 7.81 = sqrt(61)
    
    assert p1.x == 3
    assert p1.y == 4
    
    assert (p1 == p2) == False  #(3,4) == (5,6)
    assert (p4 == p2) == True   #(5,6) == (5,6)
    assert (p3 == p1) == False  #(4,3) == (3,4)
    
    assert (p4 > p1) == True    #7.81 > 5
    assert (p1 > p4) == False   #5 > 7.81
    assert (p1 > p3) == False   #5 > 5
    
    assert (p4 < p1) == False   #7.81 < 5
    assert (p1 < p4) == True    #5 < 7.81
    assert (p1 < p3) == False   #5 < 5
    
    assert p1.dist_from_origin() == 5
    assert p2.dist_from_origin() == (61 ** 0.5)
    assert p3.dist_from_origin() == 5

    assert ("Point(3, 4)" == "{}".format(p1)) == True
    assert ("Point(3, 4)" == "{}".format(p2)) == False
    assert ("Point(3, 4)" == "{}".format(p3)) == False