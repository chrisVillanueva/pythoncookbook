#
#   from:
#   -------
#   exercise 3 - 01
#
#   reason for approach:
#   ------------------------
#   You can often generalize the initialization
#   of data structures into a single ** init**()
#   function defined in a common base class.
#

# definition

class Structure(object):  # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# class use-case definitions

if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2

# application
s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)
# s2 = Stock('ACME', 50)  # Results in an error

print(s)
print(p)
print(c)
