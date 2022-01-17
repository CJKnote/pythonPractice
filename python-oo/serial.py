"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """creates a new generator, starting at the value of start"""
        self.start = start
        self.origin = start

    def generate(self):
        """returns the next number in the sequence"""
        self.start +=1
        return self.start -1

    def reset(self):
        """resets generator to the original start value"""
        self.start = self.origin



