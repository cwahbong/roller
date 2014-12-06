""" Test module roller.dice
"""

from nose2.tools import params, such

from roller.dice import const_die as c
from roller.dice import regular_die as d

with such.A("collection of dice tests") as it:

    @it.should("has correct attributes")
    @params(
        (c(4), 4, {4: 1}),
        (c(10000000000), 10000000000, {10000000000: 1}),
        (d(4), 2.5, {i + 1: 0.25 for i in range(4)}),
        (d(8), 4.5, {i + 1: 0.125 for i in range(8)}),
        (d(10), 5.5, {i + 1: 0.1 for i in range(10)}),
        (d(20), 10.5, {i + 1: 0.05 for i in range(20)}),
    )
    def correct_attr(case, die, expected, distribution):
        """ Hard coded attributes tests.
        """
        case.assertAlmostEqual(die.expected, expected)
        die_dist = dict(die.distribution())
        case.assertCountEqual(die_dist.keys(), distribution.keys())
        for key in die_dist:
            case.assertAlmostEqual(die_dist[key], distribution[key])

    @it.should("has reasonable attributes.")
    @params(
        c(256),
        d(512),
        d(9483),
    )
    def reasonable_attr(case, die):
        """ Calc expected value by distribution, and the sum of all probability
        in distribution should almost equal to 1.
        """
        expected = sum(res * prob for res, prob in die.distribution())
        case.assertAlmostEqual(expected, die.expected)

        prob_sum = sum(prob for res, prob in die.distribution())
        case.assertAlmostEqual(prob_sum, 1)

it.createTests(globals())
