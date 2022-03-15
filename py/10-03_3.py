class circle():

    def __init__(self,r):
        self.rad=r

    def area(self):
        return self.rad**2*3.14

    def peri(self):
        return self.rad*2*3.14


circle2 = circle(4)
print(circle2.area())
print(circle2.peri())