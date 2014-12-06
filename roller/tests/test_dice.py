""" Test module roller.dice
"""

from nose2.tools import params

from roller.shortcuts import d

@params(
    (d(4), 2.5, {i + 1: 0.25 for i in range(4)}),
    (d(8), 4.5, {i + 1: 0.125 for i in range(8)}),
    (d(10), 5.5, {i + 1: 0.1 for i in range(10)}),
    (d(20), 10.5, {i + 1: 0.05 for i in range(20)}),
)
def test_dice_attr(dice, expected, distribution):
    """ Test the attributes of a dice.
    """
    assert dice.expected == expected
    dice_dist = dict(dice.distribution())
    assert set(dice_dist.keys()) == set(distribution.keys())
    for key in dice_dist:
        assert round(dice_dist[key], 15) == round(distribution[key], 15)
