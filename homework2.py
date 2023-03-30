class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1  # (x1 = coor1[0], y1 = coor1[1])
        self.coor2 = coor2  # (x2 = coor2[0], y2 = coor2[1])

    def distance(self):
        # d = math.sqrt((x2 – x1)² + (y2 – y1)²)
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (((x1-x2)**2 + (y1-y2)**2)**0.5)

    def slope(self):
        # m = (y2 - y1) / (x2 - x1)
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (abs(y1 - y2) / abs(x1 - x2))


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14

    def volume(self):
        #  V = pi * r**2 * h
        print(self.pi * self.radius**2 * self.height)
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        #  SA = 2*B + 2*pi*r*h
        top = self.pi * self.radius**2
        print(top*2 + 2 * self.pi * self.radius * self.height)
        return top*2 + 2*self.pi*self.radius*self.height


# EXAMPLE OUTPUT
coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
li.distance()
li.slope()


# EXAMPLE OUTPUT
c = Cylinder(2, 3)
c.volume()
c.surface_area()
