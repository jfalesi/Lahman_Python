def merge_pitching_stints(pitch_stint_1, pitch_stint_2):
    """
    Merges two pitching stints into a single entry.
    :param pitch_stint_1:
    :param pitch_stint_2:
    >>> stint1 = {'playerID':'George', 'yearID':2004, 'stint':1, 'W': 7, 'BAOpp': 0.33, 'H': 10, 'IPouts': 25, 'ER': 3, 'ERA': 3.2} # H = 10, AB = 30, AVG = 0.333; IP = 25/3 = 8.33, ERA = 3.24
    >>> stint2 = {'playerID':'George', 'yearID':2004, 'stint':2, 'W': 8, 'BAOpp': 0.27, 'H': 8, 'IPouts': 23, 'ER': 2, 'ERA': 2.4} # H = 8, AB = 30, AVG = 0.267; IP = 23/3 = 7.67, ERA = 2.35
    >>> merged = merge_pitching_stints(stint1, stint2) # merged BA = (10 + 8)/(10/.33 + 8/.27) = 0.300; merged ERA = (3+2)/(8.33 + 7.67)*9 = 2.81
    >>> sorted([[key, merged[key]] for key in merged])
    [['BAOpp', 0.3], ['ER', 5], ['ERA', 2.81], ['H', 18], ['IPouts', 48], ['W', 15], ['playerID', 'George'], ['stint', 2], ['yearID', 2004]]
    """
    merged_entry = dict()
    string_fields = ['playerID', 'yearID', 'teamID', 'lgID']
    integer_fields = ['W', 'L', 'G', 'GS', 'CG', 'SHO', 'SV', 'IPouts', 'H', 'ER', 'HR',
                      'BB', 'SO', 'IBB', 'WP', 'HBP', 'BK', 'BFP', 'GF', 'R', 'SH', 'SF', 'GIDP']
    for key in pitch_stint_1:
        if key == 'BAOpp':  # merge opponent batting average
            opponents_batting_avg_1, opponents_batting_avg_2 = float(pitch_stint_1[key]), float(pitch_stint_2[key])
            opponents_hits_1, opponents_hits_2 = int(pitch_stint_1['H']), int(pitch_stint_2['H'])
            opponents_at_bats_1, opponents_at_bats_2 = get_at_bats(opponents_batting_avg_1, opponents_hits_1),\
                get_at_bats(opponents_batting_avg_2, opponents_hits_2)
            merged_opponents_at_bats = opponents_at_bats_1 + opponents_at_bats_2
            merged_opponents_hits = opponents_hits_1 + opponents_hits_2
            if merged_opponents_at_bats == 0:
                merged_opponents_batting_avg = 0.0
            else:
                merged_opponents_batting_avg = round(merged_opponents_hits / float(merged_opponents_at_bats), 3)
            merged_entry[key] = merged_opponents_batting_avg
        elif key == 'ERA':  # merge ERA
            earned_runs_1, earned_runs_2 = pitch_stint_1['ER'], pitch_stint_2['ER']
            innings_pitched_1, innings_pitched_2 = (get_innings(pitch_stint_1['IPouts']),
                                                    get_innings(pitch_stint_2['IPouts']))
            merged_entry[key] = round((earned_runs_1 + earned_runs_2) / (innings_pitched_1 + innings_pitched_2) * 9, 2)
        elif key == 'stint':  # merged stint is the number of stints
            merged_entry[key] = max(pitch_stint_1[key], pitch_stint_2[key])
        elif key in string_fields:  # merged string is the same if equal, otherwise the string
            # '<first>, <second>'
            merged_entry[key] = merge_item(pitch_stint_1[key], pitch_stint_2[key])
        elif key in integer_fields:  # integer fields are added
            merged_entry[key] = merge_item(pitch_stint_1[key], pitch_stint_2[key])
    return merged_entry



