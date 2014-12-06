""" Die related functions.
"""

from roller.dice._immutable_die import ImmutableDie

def d(sides):
    """ Shortcut for getting a regular die.  For example, d(4) for a
    d4, d(6) for a d6, and etc.
    """
    return ImmutableDie(
        ((side, 1 / sides) for side in range(1, sides + 1)),
        expected_hint=(sides + 1) / 2
    )

def c(const):
    """ Shortcut for getting a const die.  For example, c(3) for a die that
    always rolls 3.
    """
    return ImmutableDie(
        ((const, 1), ),
        expected_hint=const
    )

def prob(ldie, rdie, optr):
    """ Returns the probability that a binary operator optr returns true for a
    rolled ldie and rdie.
    """
    result = 0.0
    for l_res, l_prob in ldie.distribution():
        for r_res, r_prob in rdie.distribution():
            if optr(l_res, r_res):
                result += l_prob * r_prob
    return result
