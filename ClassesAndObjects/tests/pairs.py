#
# from:
# exercise 1
#

class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)

# standard behavior
print('standard p output => {p}')

# use custom **repr**()
print('custom **repr** p output => {0!r}'.format(p))

# use standard **str**
print('standard **str** p output =>  {0}'.format(p))
