""" class ConstDie
"""
from roller.dice._immutable_die import ImmutableDie

class ConstDie(ImmutableDie):
    """ A die that always rolls a fixed value.
    """
    def __init__(self, const):
        super().__init__(
            ((const, 1), ),
            expected_hint=const
        )
