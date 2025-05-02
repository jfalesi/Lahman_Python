from lahman_batting_avg_class import *

def test_batting_avg():
    """
    >>> avg = BattAvg(9, 2)
    >>> avg.print_val()
    0.222
    """
    pass

def test_merge(at_bats, hits):
    """
    >>> avg = BattAvg(9, 3)
    >>> avg.merge(11, 3)
    >>> avg.at_bats
    20
    >>> avg.hits
    6
    >>> avg.print_val()    
    0.300
    """
    pass


if __name__=="__main__":
    import doctest
    doctest.testmod()
