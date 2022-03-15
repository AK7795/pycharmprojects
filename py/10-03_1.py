
'''the following code p class takes 2 arguments
        the SHOW function returns the co-ordinates or point suppose (x,y)
        the MOVE function takes 2 arguments (x1,y1) and moves the (x,y) point by (x1,y1)
        the SHOW function displays the new co-ordinates
'''
class p(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y



p1 = p(1,4)
p2 = p(2,5)
print(p1.show())
print(p2.show())
p1.move(5,6)
p2.move(7,8)
print(p1.show())
print(p2.show())