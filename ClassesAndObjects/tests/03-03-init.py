#
#   from:
#   -------
#   exercise 3 - 03
#
#   reason for approach:
#   ------------------------
#  Another possible choice is to use
#  keyword arguments as a means for
#  adding additional attributes to
#   the structure not specified in _fields.
#


# definition

class Structure(object):
    # Class variable that
    # specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


# application

if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 52, 91.2, date='8/2/2012')

print("s1")
print(s1.name)
print(s1.shares)
print(s1.price)

print("\ns2")
print(s2.name)
print(s2.shares)
print(s2.price)
print(s2.date)
