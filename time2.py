"""
Starting with code example from Time2
Refactor Time class to be a single int representing seconds since midnight
The test cases in main should not change

"""

from __future__ import print_function, division


class Time:
    """Represents the time of day.
    attributes: second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        second: seconds since midnight
        """
        self.seconds = second + (minute * 60) + (hour * 60 * 60)

    def __str__(self):
        """Returns a string representation of the time."""
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)
    
    def __lt__(self, other):
        return self.time_to_int() < other.time_to_int()

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        return Time(second=(self.seconds + other.seconds))

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        return Time(second=(self.seconds + seconds))

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds > 0 and self.seconds < 24*60*60

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)

    print('example of __lt__')
    print(t1, t2)
    print(t1 < t2)


if __name__ == '__main__':
    main()
