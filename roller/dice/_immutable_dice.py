""" class ImmutableDice.
"""

from roller.dice._immutable_die import ImmutableDie

class ImmutableDice(ImmutableDie):
    """ XXX docstring for ImmutableDice"""

    def __init__(self, *im_dice):
        self._im_dice = tuple(*im_dice)
        super().__init__(
            None,
            sum(im_die.expected() for im_die in self._im_dice),
        )

    def prob(self, side):
        pass

    def results(self):
        pass

    def distribution(self):
        pass

    def roll(self):
        return sum(im_die.roll() for im_die in self._im_dice)
