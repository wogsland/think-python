from swampy.TurtleWorld import *
import math

for i in range(4):
    print 'Hello!'

world = TurtleWorld()
bob = Turtle()
print bob

def sq(tortuga, side):
    for i in range(4):
        fd(tortuga, side)
        lt(tortuga)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


sq(bob, 85)
polygon(bob, 7, 70)
circle(bob, 100)
circle2(bob, 30)
wait_for_user()
