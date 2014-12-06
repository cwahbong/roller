""" Probability related functions.
"""

def probability(ldie, rdie, optr):
    """ Returns the probability that a binary operator optr returns true for a
    rolled ldie and rdie.
    """
    result = 0.0
    for l_res, l_prob in ldie.distribution():
        for r_res, r_prob in rdie.distribution():
            if optr(l_res, r_res):
                result += l_prob * r_prob
    return result
