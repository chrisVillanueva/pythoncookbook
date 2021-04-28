#
#   from:
#   -------
#   exercise 5 - 01
#
#   reason for approach:
#   ------------------------
#   You have the name of a method
#   that you want to call on an
#   object stored in a string and
#   you want to execute the method.
#

import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

# application


p = Point(2, 3)

print(f"Structure[Point] => {p}")

# Calls p.distance(0, 0)
d = getattr(p, 'distance')(0, 0)

print(f"getattr(p, 'distance')(0, 0) => {d}")
