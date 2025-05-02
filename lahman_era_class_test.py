from lahman_era_class import *

def test_era_init():
    """
    >>> era = Era(9, 2)
    >>> era.print_val()
    2.00
    >>> era = Era(7, 2)
    >>> era.print_val()
    2.57
    >>> era = Era()
    >>> era.print_val()
    0.00
    >>> era = Era(3, 0)
    >>> era.print_val()
    0.00
    >>> era = Era(0, 4)
    >>> era.print_val()
    inf
    """
def merge():
    """
    >>> era = Era(7, 2)
    >>> era.merge(9, 2)
    >>> era.print_val()
    2.25
    """

if __name__=="__main__":
    import doctest
    doctest.testmod()
