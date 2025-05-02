def merge_batting_stints(batting_stint_1, batting_stint_2):
    """
    Merges two pitching stints into a single entry.
    :param batting_stint_1: 
    :param batting_stint_2: 
    >>> stint1 = {'playerID':'George', 'yearID':2004, 'stint':1, 'G': 7}
    >>> stint2 = {'playerID':'George', 'yearID':2004, 'stint':2, 'G': 8}
    >>> merged = merge_batting_stints(stint1, stint2)
    >>> sorted([[key, merged[key]] for key in merged])
    [['G', 15], ['playerID', 'George'], ['stint', 2], ['yearID', 2004]]
    """
    merged_entry = dict()
    string_fields = ['playerID', 'yearID', 'teamID', 'lgID']
    integer_fields = ['G', 'G_batting', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS',
                      'BB', 'SO', 'IBB', 'SH', 'SH', 'GIDP', 'G_old']
    for key in batting_stint_1:
        if key == 'stint':  # merged stint is the number of stints
            merged_entry[key] = max(batting_stint_1[key], batting_stint_2[key])
        elif key in string_fields:  # merged string is the same if equal, otherwise the string
            #'<first>, <second>'
            merged_entry[key] = merge_item(batting_stint_1[key], batting_stint_2[key])
        elif key in integer_fields:  # integer fields are added
            merged_entry[key] = merge_item(batting_stint_1[key], batting_stint_2[key])
    return merged_entry



