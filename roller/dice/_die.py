""" Class Die.
"""

import operator
import random

from roller.prob import Prob

class Die:
    """ A Die.
    """

    def __init__(self):
        super().__init__()

    @property
    def expected(self):
        """ The expected value of the points it rolls.
        """
        raise NotImplementedError()

    def prob(self, side):
        """ The occur probability of the specific side.
        """
        raise NotImplementedError()

    def results(self):
        """ Get all possible occurrence.
        """
        raise NotImplementedError()

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
        return not self.__eq__(other)

    @staticmethod
    def _cmp_helper(ldie, rdie, optr):
        """ Helper for implementing cmp functions.
        Returns the probability that a binary operator returns true for a rolled
        ldie and ride.
        """
        prob = 0.0
        for l_res, l_prob in ldie.distribution():
            for r_res, r_prob in rdie.distribution():
                if optr(l_res, r_res):
                    prob += l_prob * r_prob
        return prob

    def __lt__(self, other):
        return Prob(Die._cmp_helper(self, other, operator.lt))

    def __le__(self, other):
        return Prob(Die._cmp_helper(self, other, operator.le))

    def __gt__(self, other):
        return Prob(Die._cmp_helper(self, other, operator.gt))

    def __ge__(self, other):
        return Prob(Die._cmp_helper(self, other, operator.ge))

