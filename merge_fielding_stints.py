def merge_fielding_stints(fielding_stint_1, fielding_stint_2):
    """
    Merges two fielding stints into a single entry.

    Note that stats at different positions within the same stint are merged.  This is
     probably not ideal but currently I'm not really doing anything with fielding stats.
     
    :param fielding_stint_1: 
    :param fielding_stint_2: 
    >>> stint1 = {'playerID':'George', 'yearID':2004, 'stint':1, 'G':7, 'RF1':1.2}
    >>> stint2 = {'playerID':'George', 'yearID':2004, 'stint':2, 'G':8, 'RF1':0.8}
    >>> merged = merge_fielding_stints(stint1, stint2)
    >>> sorted([[key, merged[key]] for key in merged])
    [['G', 15], ['RF1', 1.0], ['playerID', 'George'], ['stint', 2], ['yearID', 2004]]
    """
    merged_entry = dict()
    string_fields = ['playerID', 'yearID', 'teamID', 'lgID', 'POS']
    integer_fields = ['G', 'GS', 'InnOuts', 'PO', 'A', 'E', 'DP', 'PB', 'WP', 'SB', 'CS',
                      'ZR', 'Cability', 'Carm', 'OFarm', 'IndPO', 'IndA']
    float_fields = ['RF1', 'RF3']
    for key in fielding_stint_1:
        if key == 'stint':  # merged stint is the number of stints
            merged_entry[key] = max(fielding_stint_1[key], fielding_stint_2[key])
        elif key in string_fields:  # merged string is the same if equal, otherwise the string
            #'<first>, <second>'
            merged_entry[key] = merge_item(fielding_stint_1[key], fielding_stint_2[key])
        elif key in integer_fields:  # integer fields are added
            merged_entry[key] = merge_item(fielding_stint_1[key], fielding_stint_2[key])
        elif key in float_fields:  # float fields are averaged
            merged_entry[key] = merge_item(fielding_stint_1[key], fielding_stint_2[key])
    return merged_entry


