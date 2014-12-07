""" Test module roller.dice
"""

from nose2.tools import such

def const_die(const):
    """ Shortcut function for getting a const die without import.
    """
    import roller.dice
    return roller.dice.const_die(const)

def regular_die(const):
    """ Shortcut function for getting a const die without import.
    """
    import roller.dice
    return roller.dice.regular_die(const)

with such.A("collection of dice tests") as it:

    def correct_attr(case, die, expected, distribution):
        """ Hard coded attributes tests.
        """
        case.assertAlmostEqual(die.expected, expected)
        die_dist = dict(die.distribution())
        case.assertCountEqual(die_dist.keys(), distribution.keys())
        for key in die_dist:
            case.assertAlmostEqual(die_dist[key], distribution[key])

    @it.should("has correct attributes (const die).")
    def correct_attr_c(case):
        """ Hard coded attributes tests for const die.
        """
        params = (
            (4, 4, {4: 1}),
            (10000000000, 10000000000, {10000000000: 1}),
        )
        for const, expected, distribution in params:
            correct_attr(case, const_die(const), expected, distribution)

    @it.should("has correct attributes (regular die).")
    def correct_attr_d(case):
        """ Hard coded attributes tests for regular die.
        """
        params = (
            (4, 2.5, {i + 1: 0.25 for i in range(4)}),
            (8, 4.5, {i + 1: 0.125 for i in range(8)}),
            (10, 5.5, {i + 1: 0.1 for i in range(10)}),
            (20, 10.5, {i + 1: 0.05 for i in range(20)}),
        )
        for sides, expected, distribution in params:
            correct_attr(case, regular_die(sides), expected, distribution)

    def reasonable_attr(case, die):
        """ Calc expected value by distribution, and the sum of all probability
        in distribution should almost equal to 1.
        """
        expected = sum(res * prob for res, prob in die.distribution())
        case.assertAlmostEqual(expected, die.expected)

        prob_sum = sum(prob for res, prob in die.distribution())
        case.assertAlmostEqual(prob_sum, 1)

    @it.should("has reasonable attributes (const die).")
    def reasonable_attr_c(case):
        """ resonable_attr() for const die
        """
        params = (
            256,
            512,
            12345,
        )
        for const in params:
            reasonable_attr(case, const_die(const))

    @it.should("has resonable attributes (regular die).")
    def resonable_attr_d(case):
        """ resonable_attr() for regular die
        """
        params = (
            512,
            9483
        )
        for sides in params:
            reasonable_attr(case, regular_die(sides))

    @it.should("be comparable (==, !=)")
    def comparable_eq_ne(case):
        """ Test eq and ne operatos.
        """
        params = (
            (const_die(1), regular_die(1), True),
        )
        for ldie, rdie, is_eq in params:
            case.assertEqual(ldie == rdie, is_eq)
            case.assertEqual(ldie != rdie, not is_eq)

    def roll(case, die):
        """ Rolls a die for 100 times.
        """
        for _ in range(100):
            case.assertIn(die.roll(), die.results())

    @it.should("rolls a resonable result (const die).")
    def roll_c(case):
        """ roll() for a const die.
        """
        params = (
            1, 5
        )
        for const in params:
            roll(case, const_die(const))

    @it.should("rolls a resonable result (regular die).")
    def roll_d(case):
        """ roll() for a regular die.
        """
        params = (
            1, 20, 256,
        )
        for sides in params:
            roll(case, regular_die(sides))

    @it.should("calculates binary probability correctly.")
    def binary_prob(case):
        """ Test return value of probability().
        """
        import operator
        operators = (
            operator.lt,
            operator.gt,
            operator.le,
            operator.ge,
            operator.eq,
            operator.ne,
        )
        params = (
            (
                regular_die(6), regular_die(6),
                (5 / 12, 5 / 12, 7 / 12, 7 / 12, 1 / 6, 5 / 6)
            ),
        )
        import roller.dice
        for ldie, rdie, results in params:
            for optr, result in zip(operators, results):
                prob = roller.dice.probability(ldie, rdie, optr)
                case.assertAlmostEqual(prob, result)

it.createTests(globals())
