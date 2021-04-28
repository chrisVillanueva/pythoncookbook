#
#   from:
#   -------
#   exercise 4 - 02
#
#   reason for approach:
#   ------------------------
#   There are some techniques that can be
#   used to simplify the specification of
#   constraints in classes. One approach
#   is to use a class decorator
#   ex: @check_attributes
#

# Base class. Uses a descriptor to set a value
class Descriptor(object):
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock(object):
    # type constraints no longer here
    # validated with @check_attributes
    # decorator
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# application
s = Stock('ACME', 50, 91.1)
s.name
s.shares = 75

print(f"Structure[Stock] => {s}")
print(f"s.name   => {s.name}")
print(f"s.shares => {s.shares}")


# s.shares = -10  # Results in an error
# s.price = 'a lot'  # Results in an error
# s.name = 'ABRACADABRA'  # Results in an error
