""" class ImmutableDie.
"""
from roller.dice._die import Die

class ImmutableDie(Die):
    """ A die that has immutable attributes.
    """

    def __init__(self, distribution, expected_hint=None):
        def _normalized_dist_dict(dist_dict):
            """ Make the sum of probability be 1 in a distribution by
            multiplying a constant.
            """
            total_weight = sum(dist_dict.values())
            return dict((k, v / total_weight) for k, v in dist_dict.items())
        super().__init__()
        self._distribution = _normalized_dist_dict(dict(distribution))
        if expected_hint is None:
            self._expected = sum(k * v for k, v in self._distribution.items())
        else:
            self._expected = expected_hint

    @property
    def expected(self):
        return self._expected

    def prob(self, side):
        return self._distribution[side]

    def results(self):
        return self._distribution.keys()

def regular_die(sides):
    """ Shortcut for getting a regular die.  For example, d(4) for a
    d4, d(6) for a d6, and etc.
    """
    return ImmutableDie(
        ((side, 1 / sides) for side in range(1, sides + 1)),
        expected_hint=(sides + 1) / 2
    )

def const_die(const):
    """ Shortcut for getting a const die.  For example, c(3) for a die that
    always rolls 3.
    """
    return ImmutableDie(
        ((const, 1), ),
        expected_hint=const
    )
