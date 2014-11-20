""" Dice here.
"""

import collections
import random

class Die(object):
    """ A die.
    """

    def __init__(self):
        super().__init__()

    def expected(self):
        """ The expected value of the points it rolls.
        """

    def distribution(self):
        """ Get the distribution of rolled result as a dictionary.
        """

    def roll(self):
        """ Roll the dice and get the result.
        """


class RegularDie(Die):
    """ A dice that rolls numbers from 1 to number of sides.
    """

    def __init__(self, sides):
        super().__init__()
        self._sides = sides
        self._prob = 1 / sides
        self._expect = (sides + 1) / 2

    def expected(self):
        return self._expect

    def distribution(self):
        return collections.defaultdict(
            int,
            ((i, self._prob) for i in range(1, self._sides + 1))
        )

    def roll(self):
        return random.randint(1, self._sides)


class MultipleDice(Die):
    """docstring for MultipleDice"""

    def __init__(self, *dice):
        super().__init__()
        self._dice = tuple(*dice)

    def expected(self):
        return sum(die.expected() for die in self._dice)

    def distribution(self):
        pass

    def roll(self):
        return sum(die.roll() for die in self._dice)


def d(sides):
    """ Shortcut for getting a regular dice.
    """
    return RegularDie(sides)
