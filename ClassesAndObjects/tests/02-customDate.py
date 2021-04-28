#
#   from:
#   -------
#   exercise 2
#
#   reason for approach:
#   ------------------------
#   To customize string formatting, define the
#   **format**() method on a class.
#

# changed format string to represent three
# different options [dash, slash, dot]
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}.{d.month}.{d.year}'
}


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


# custom date
d = Date(2012, 12, 21)
# print('Default date => ' + format(d))
print(f'Default date => {d}')
print(f"Date with mdy arguments => {format(d, 'mdy')}")

# covers all 3 date formats
print('The date is {:ymd} - defined with :ymd arguments'.format(d))
print('The date is {:mdy} - defined with :mdy arguments'.format(d))
print('The date is {:dmy} - defined with :dmy arguments'.format(d))
