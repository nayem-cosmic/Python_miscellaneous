class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_squared = (self.x-other.x)**2
        y_diff_squared = (self.x-other.y)**2
        return (x_diff_squared+y_diff_squared)**0.5

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate({},{})".format(self.x, self.y)

c = Coordinate(3, 4)
other = Coordinate(5, 6)

print(c.distance(other))

