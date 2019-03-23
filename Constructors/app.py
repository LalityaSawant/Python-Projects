class Point:
    def __init__(self,x,y): # this is the constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 30
print(point.x)
print(point.y)