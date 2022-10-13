import math

class circleClass():
    def __init__(self, circleradius):
        self.circleradius = circleradius

    def printArea(self):
        return math.pi*(self.circleradius**2)
circleradius = float(input('Enter some random radius of the circle = '))
circleobj = circleClass(circleradius)
print("The Area of circle with given radius", circleradius,
      '=', round(circleobj.printArea(), 4))