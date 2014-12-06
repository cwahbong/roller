""" class RegularDie.
"""

from roller.dice._immutable_die import ImmutableDie

class RegularDie(ImmutableDie):
    """ A dice that rolls numbers from 1 to number of sides.
    """

    def __init__(self, sides):
        super().__init__(
            ((side, 1 / sides) for side in range(1, sides + 1)),
            expected_hint=(sides + 1) / 2
        )
