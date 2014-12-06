""" Prob class
"""

class Prob:
    """ Represents a probability value
    """

    def __init__(self, value):
        if value > 1.0 or value < 0.0:
            raise ValueError("Prob value should be in [0.0, 1.0].")
        self._value = value

    @property
    def value(self):
        """ Get the value of a probability
        """
        return self._value

    def __bool__(self):
        return self._value == 1

    def __repr__(self):
        return "Prob({})".format(repr(self._value))

