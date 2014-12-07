""" Class Die.
"""

from abc import ABC, abstractmethod
import random

class Die(ABC):
    """ A Die.
    """

    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def expected(self):
        """ The expected value of the points it rolls.
        """

    @abstractmethod
    def prob(self, side):
        """ The occur probability of the specific side.
        """

    @abstractmethod
    def results(self):
        """ Get all possible occurrence.
        """

    def distribution(self):
        """ Get the distribution of rolled result as a dictionary.
        """
        for result in self.results():
            yield result, self.prob(result)

    def roll(self):
        """ Roll the dice and get the result.
        """
        rand = random.random()
        acc = 0.0
        for result, prob in self.distribution():
            acc += prob
            if rand < acc:
                return result

    def __eq__(self, other):
        if isinstance(other, Die):
            return dict(self.distribution()) == dict(other.distribution())
        return NotImplemented

    def __ne__(self, other):
        return not self == other
