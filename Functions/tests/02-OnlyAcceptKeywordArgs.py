#
#   from:
#   -------
#   Functions That Only Accept Keyword Arguments
#
#   reason for approach:
#   ------------------------
#   You want a function to only accept certain
#   arguments by keyword.  This feature is easy to
#   implement if you place the keyword arguments
#   after a _ argument or a single unnamed _ .
#   Keyword-only arguments are often a good way to
#   enforce greater code clarity when specifying
#   optional function arguments.
#


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


min1 = minimum(1, 5, 2, -5, 10)
# => -5
min2 = minimum(1, 5, 2, -5, 10, clip=0)
# => 0
print('minimum(1, 5, 2, -5, 10) => ' + str(min1))
print('minimum(1, 5, 2, -5, 10, clip=0) => ' + str(min2))

# help(minimum)
