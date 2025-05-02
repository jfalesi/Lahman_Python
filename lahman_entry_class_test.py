from lahman_entry_class import *


def test_init():
    """
    >>> george = player_entry({'player_id': 'george', 'year_id': '2004', 'stint': [1], 'AB': 100, 'H': 28})
    >>> george.player_id
    'george'
    >>> sorted([[key, george['2004'][key]] for key in george['2004']])
    [['AB', 100], ['H', 28], ['player_id', 'george'], ['stint', [1]], ['year_id', '2004']]
    """
    pass

def test_add_year_data():
    """
    >>> george = player_entry({'player_id': 'george', 'year_id': '2004', 'stint': [1], 'AB': 100, 'H': 28})
    >>> george.add_year_data({'player_id': 'george', 'year_id': '2005', 'stint': [1], 'AB': 120, 'H': 33})
    >>> sorted([[key, george['2005'][key]] for key in george['2005']])
    [['AB', 120], ['H', 33], ['player_id', 'george'], ['stint', [1]], ['year_id', '2005']]
    """
    pass
    
def test_add_stint(at_bats, hits):
    """
    >>> george = player_entry({'player_id': 'george', 'year_id': '2004', 'stint': [1], 'AB': 100, 'H': 28})
    >>> george.add_year_data({'player_id': 'george', 'year_id': '2004', 'stint': [2], 'AB': 120, 'H': 33})
    >>> sorted(george['2004'])
    {'player_id': 'george', 'year_id': '2004', 'stint': [1, 2], 'AB': 240, 'H': 61}
    """
    pass

if __name__=="__main__":
    import doctest
    doctest.testmod()
