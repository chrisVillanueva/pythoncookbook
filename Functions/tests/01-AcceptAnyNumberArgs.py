#
#   from:
#   -------
#   Functions That Accept Any Number of Arguments
#
#   reason for approach:
#   ------------------------
#   You want to write a function that accepts
#   any number of input arguments.To write a
#   function that accepts any number of positional
#   arguments, use a \* argument.
#


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


avg1 = avg(1, 2)
avg2 = avg(1, 2, 3, 4)
avg3 = avg(1, 2, 3, 4, 5, 6, 7, 8)

# standard behavior
print(f'avg(1, 2) => {avg1}')

print(f'avg(1, 2, 3, 4) => {avg2}')

print(f'avg(1, 2, 3, 4, 5, 6, 7, 8) => {avg3}')
