#
#   from:
#   -------
#   exercise 5 - 02
#
#   reason for approach:
#   ------------------------
#   An alternative approach is to
#   use operator.methodcaller()
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
p = Point(2, 3)

print(p)

d = operator.methodcaller('distance', 0, 0)(p)

print(d)
