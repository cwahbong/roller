""" Some shortcut functions.
"""

import roller.dice

def d(sides):
    """ Shortcut for getting a regular die.  For example, d(4) for a
    d4, d(6) for a d6, and etc.
    """
    return roller.dice.RegularDie(sides)

def c(const):
    """ Shortcut for getting a const die.  For example, c(3) for a die that
    always rolls 3.
    """
    return roller.dice.ConstDie(const)

def p(prob):
    """ Shortcut to let user write expressions as below:

        p(d(4) > 2)
    """
    return prob.value
