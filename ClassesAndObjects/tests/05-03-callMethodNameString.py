#
#   from:
#   -------
#   exercise 5 - 03
#
#   reason for approach:
#   ------------------------
#   operator.methodcaller() may be useful
#   if you want to look up a method by name
#   and supply the same arguments over
#   and over again.
#

import math
import operator


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


# application

points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]

print('initial points => ')
print(points)

points.sort(key=operator.methodcaller('distance', 0, 0))


print('sorted points => ')
print(points)
# TODO: understand this sort.  Not sure about the order.
