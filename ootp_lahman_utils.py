# coding=utf-8
# lahmanator_fns
"""
docstring
"""

import os
import progress_bar as pb


def convert_to_number(item):
    """
    Converts entry to either an int or a float. If int(entry) == float(entry), converts
    entry to int.  Otherwise converts to float.  If entry is not a string, returns it
    unconverted.

    :rtype : int or float if convertible, otw string if item is string, otw returns item
    :param item: expected to be string representing a number
    """
    if type(item) != str:
        return item
    try:
        int_item = int(item)
        return int_item
    except ValueError:
        try:
            float_num = float(item)
            return float_num
        except ValueError:
            return item


def merge_item(item_1, item_2, key):
    """
    Merges two individual data items as follows:
    strings:    If they're identical, returns the string
                otw returns '<item_1>, <item_2>'

    int:
        key = 'stint': returns max
        key = 'yearID': returns item_1 (they should be the same)
        otw returns item_1 +  item_2

    float:  returns average of item_1 and item_2

    :rtype : item_1 type
    :param item_1: first item to merge
    :param item_2: second item to merge
    :param key:  name of item to merge
    """

    try:
        assert type(item_1) == type(item_2)
    except AssertionError:
        print ("Assertion error encountered in 'merge_items' with " + str(item_1) + ' and ' + str(item_2)
               + '. Returning ' + str(item_1) + '.')
        return item_1

    try:
        if type(item_1) == str:  # if they're strings,
            if item_1 == item_2:  # and they're the same,
                return item_1  # just return their value (e.g. same player_id)
            else:
                return item_1 + ', ' + item_2  # if they're different, glue them together
                # (e.g. different teams, leagues)
        elif type(item_1) == int:  # if they're integers
            if key == 'stint':  # if they're stints,
                return max(item_1, item_2)  # just return the max as this will be the number
                #  of stints encountered so far
            elif key == 'yearID':  # if they're years,
                return item_1  # they should be the same
        elif type(item_1) == float:
            return item_1 + item_2  # add the items

    except TypeError:
        print "Type error encountered in 'merge_items' with " + str(item_1) + ' and ' + str(item_2) + '. Returning ' \
              + str(item_1) + '.'
        return item_1


def merge_stints(data_dict1, data_dict2):
    """
    This function is no longer required for merging batting and pitching stints.
    Instead use merge_batting_stints and merge_pitching_stints.  May be useful for other data sets.
    
    :rtype : dict
    :param data_dict1: first dictionary entry
    :param data_dict2: dictionary entry
    """
    merged_data_dict = dict()
    for key in data_dict1:
        merged_data_dict[key] = merge_item(data_dict1[key], data_dict2[key], key)
    return merged_data_dict


def get_at_bats(batting_avg, hits):
    """
    Given batting average and hits, computes at-bats
    :rtype : int
    :param batting_avg: player batting average
    :param hits: player hits
    """
    if batting_avg == 0:  # note that batting_avg = 0 implies that H = 0.  However, there are some entries
        # in 'Batting.csv' for which BA = 0 but H != 0.  In these cases,
        # the number of at bats in the merged data will be incorrect.
        return 0
    return int(round(hits / batting_avg, 0))


def get_innings(inning_outs):
    """
    Given number of pitching outs, computes innings pitched
    :param inning_outs: 
    """
    return inning_outs / 3.


def compute_avg(player_data, header_type_dict):
    """
    player_data is typically a player entry, e.g. from 'fielding2.csv'
    :param player_data: 
    :param header_type_dict: 
    """
    data_length = len(player_data.keys())
    avg_dict = dict()

    for category in player_data[player_data.keys()[0]].keys():
        if header_type_dict[category] == str:
            first_year = player_data.keys()[0]
            first_year_data = player_data[first_year]
            first_year_data_category = first_year_data[category]
            avg_dict[category] = first_year_data_category
        else:
            category_total = 0.0
            for year in player_data.keys():
                year_data = player_data[year]
                category_data = year_data[category]
                category_total += category_data
            if header_type_dict[category] == int:
                avg_dict[category] = int(round(category_total / data_length, 0))
            else:
                avg_dict[category] = round(category_total / data_length, 2)
    return avg_dict


# def add_entry(year, lahman_data, ootp_data, ootp_header, header_type_dict):
#     """
#     returns a string for ootp_data for player and year, using 'year' data
#     from lahman_data and prior year data from ootp_data
#     :param year: 
#     :param lahman_data: 
#     :param ootp_data: 
#     :param ootp_header: 
#     :param header_type_dict: 
#     """
#     year_data = lahman_data[year]
#     prior_data = ootp_data
#     avg_prior_data = computeAvg(prior_data, ootp_header, header_type_dict)
#     write_str = ''
#     for index in ootp_header:
#         category = ootp_header[index]
#         if category in year_data:
#             write_str += str(year_data[category]) + ','
#         else:
#             write_str += str(avg_prior_data[category]) + ','
#     return write_str.strip(',') + '\n'


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


def order_stats(data_dict, header_dict):
    """
    returns list of stats in the original order from the input file
    :param data_dict: 
    :param header_dict: 
    >>> order_stats({'key1':1, 'key2':2, 'key3':3}, {0:'key2', 1:'key3', 2:'key1'})
    [2, 3, 1]
    """
    stat_list = []
    for key in range(len(header_dict)):
        stat_list.append(data_dict[header_dict[key]])
    return stat_list


def import_lahman_files(master_file='master.csv', batting_file='batting.csv', fielding_file='fielding2.csv', 
                        pitching_file='pitching.csv', verbose=False):
    """
    :param verbose:
    :param master_file:
    :param batting_file: 
    :param fielding_file: 
    :param pitching_file: 
    imports Lahman master, batting, fielding and pitching files and returns the data in a dictionary of dictionaries
    with the following format:
        dicts: dictionary of dictionaries of the form:
        dicts['master'] = master_dicts
        dicts['bat'] = batting_dicts
        dicts['field'] = fielding_dicts
        dicts['pitch'] = pitching_dicts

        where each of <>Dicts is of the form:
            <>Dicts['data'] = <>Dict = dictionary of player data keyed by player_id
            <>Dicts['header'] = <>header_dict = dictionary of columns keyed by name
            <>Dicts['lookup'] = <>LookupDict = dictionary of column names keyed by column number
    """
    data = 'data'
    header = 'header'
    lookup = 'lookup'
    master = 'master'
    bat = 'bat'
    field = 'field'
    pitch = 'pitch'

    master_data, master_header, master_lookup = import_master(file_path=master_file, verbose=verbose)
    master_dicts = {data: master_data, header: master_header, lookup: master_lookup}

    batting_data, batting_header, batting_lookup = import_batting(file_path=batting_file, verbose=verbose)
    batting_dicts = {data: batting_data, header: batting_header, lookup: batting_lookup}

    field_data, field_header, field_lookup = import_fielding(file_path=fielding_file, verbose=verbose)
    fielding_dicts = {data: field_data, header: field_header, lookup: field_lookup}

    pitch_data, pitching_header, pitching_lookup = import_pitching(pitching_file, verbose=verbose)
    pitching_dicts = {data: pitch_data, header: pitching_header, lookup: pitching_lookup}

    return {master: master_dicts, bat: batting_dicts, field: fielding_dicts, pitch: pitching_dicts}


def import_lahman_data_file(file_path, file_type, verbose=False):
    """
    Imports ootp format Lahman database file
    Use for batting, pitching, fielding data files (NOT FOR MASTER DATA FILE)
    Returns dictionary keyed by "playerID", with stints merged
    
    :rtype : dict

    returns dictionary of dictionaries (return_dict):
        {'data': lahman_data_dict, 'header': lahman_header_dict, 'lookup': lookup_dict_dict}
        where:
            lahman_data_dict = dictionary of player data keyed by column header
            lahman_header_dict = dictionary of data headers keyed by index
            lookup_dict_dict = dictionary of data header column numbers indexed by header

    returns None on OSError indicating 'file_path' does not exist

    :param file_type: type of lahman file ('batting', 'pitching', 'fielding')
    :param verbose: if true, function provides feedback on file loading
    :param file_path: path to lahman data file
    """

    # open lahman file
    try:
        f = open(file_path)

    except OSError: # if file does not exist, return nothing
        print "File '" + file_path + "' does not exist."
        return

    # initialize keys in dictionary to be returned (see docstring for explanation of returned dict)
    data_label = 'data'
    header_label = 'header'
    lookup_label = 'lookup'
     
    # initialize dicts to return in return_dict
    data_dict = dict()
    header_dict = dict()
    lookup_dict = dict()

    # initialize return_dict
    return_dict = {data_label: data_dict, header_label: header_dict, lookup_label: lookup_dict}

    # read header line
    header_line = f.readline().strip().split(',')

    # set header_dict and lookup_dict
    for i in range(len(header_line)):
        header_dict[i] = header_line[i] #
        lookup_dict[header_line[i]] = i
        
    # initialize data to be used in computing loading progress
    file_size = os.stat(file_path).st_size
    bytes_read = len(header_line)
    last_fraction = 0

    # read player data
    for line in f:
        if verbose:
            # print file loading feeback
            bytes_read += len(line)
            fraction = round(float(bytes_read) / file_size, 2)
            if fraction - last_fraction > 0.05:
                pb.update_progress(fraction, "Importing '" + file_path + "'")
            last_fraction = fraction

        # parse data in line
        data = line.strip().split(',')
        for index, item in enumerate(data):
            if item == '': # if data item is empty string,
                data[index] = 0 # set to zero

        # initialize dictionary for current entry (i.e. data in current line)
        entry = entry_dict()

        # save data in current line to entry_dict, converting strings to numbers where appropriate
        for i in range(len(data)):
            entry[header_dict[i]] = convert_to_number(data[i])
            # note if you get a key error in the above lines, check if the last entry in the input file has an extra
            # comma at the end of it (i.e. an extra column)

        # extract player_id
        player_id = entry_dict['playerID']

        # extract year_id *************** not valid for master file *********************************
        year = entry_dict['yearID']

        # if this is the first time this player appears in the file (i.e. the player's first year),
        if player_id not in data_dict:

            year_data = dict() # initialize  year_data dict
            year_data[year] = entry_dict # add entry_dict to year_data dict
            data_dict[entry_dict[player_id]] = year_data # add year_data to player's data entry in data_dict

        # if player is already in the data_dict, add this year's data
        else:

            if year not in year_data:  # indicates the player has only one stint, i.e. played for only one team in year
                year_data[year] = entry_dict

            else:  # player year already has a stint, i.e. player played for more than one team in year

                year_data = merge_stints(entry_dict, year_data[year], file_type) #  merge stints

                #  *******************************************the following is why inheritance exists
                # if file_type == 'pitching':
                #     year_data[year] = merge_pitching_stints(entry_dict, year_data[year])
                # elif file_type == 'batting':
                #     year_data[year] = merge_pitching_stints(entry_dict, year_data[year])
                # elif file_type == 'fielding':
                #     year_data[year] = merge_fielding_stints(entry_dict, year_data[year])

    if verbose:
        pb.update_progress(1.0, "Importing '" + file_path + "'") #  print final update for file loading
    f.close()

    return return_dict


def import_pitching(file_path='Pitching.csv', verbose=False):
    """
    Imports ootp_ format Lahman database pitching file, typically "Pitching.csv"
    Returns dictionary keyed by "playerID", with stints merged.

    Note the test file 'pitching_test.csv' is a subset of the 'Pitching.csv' file from
    the 2012 Lahman database. The 'pitching_test.csv' file contains only those players
    whose IDs start with the letter 'a'.

    :rtype : object
    :param verbose:
    :param file_path:

    >>> pitching_dict = import_pitching(file_path='Pitching_test.csv')['data']
    >>> len(pitching_dict)
    4
    >>> pitching_dict['abbeybe01'][1895]['L']
    3
    """

    return import_lahman_data_file(file_path, 'pitching', verbose=verbose)


def import_batting(file_path='Batting.csv', verbose=False):
    """
    Imports ootp_ format Lahman database batting file, typically "Batting.csv"
    Returns dictionary keyed by "playerID", with stints merged.

    Note the test file 'batting_test.csv' is a subset of the 'batting.csv' file from the
    2012 Lahman database. The 'batting_test.csv' file contains only those players whose
    IDs start with the letter 'a'.

    :rtype : dict of dicts in the form {'data': data_dict, 'header': header_dict, 'lookup': lookup_dict}
    :param verbose:
    :param file_path:

    >>> batting_dict = import_batting('batting_test.csv')['data']
    >>> len(batting_dict)
    516
    >>> batting_dict['abadijo01'][1875]['G']
    12
    """

    return import_lahman_data_file(file_path, 'batting', verbose=verbose)


def import_fielding(file_path='Fielding2.csv', verbose=False):
    """
    Imports ootp_ format Lahman database fielding file, typically "Fielding2.csv"
    Returns dictionary keyed by "playerID", with stints merged.

    Note the test file 'fielding2_test.csv' is a subset of the 'Fielding2.csv' file from the
    2012 Lahman database. The 'Fielding2.csv' file contains only those players whose
    player_id s start with the letter 'a'.

    :rtype : object
    :param verbose:
    :param file_path:

    >>> fielding_dict = import_fielding('Fielding2_test.csv')['data']
    >>> len(fielding_dict)
    514
    >>> fielding_dict['abbeybe01'][1895]['G']
    89
    """

    return import_lahman_data_file(file_path, 'fielding', verbose=verbose)


def import_master(file_path='Master.csv', verbose=False):
    """
    Imports master Lahman file, typically 'Master.csv'.
    :rtype : object
    :param verbose:
    :param file_path:

    Returns three dictionaries:

    master_dict = dictionary of players from master file.  Keyed by playerID.  Each entry
        is a dictionary of the form {column_header:value}.
    header_dict = dictionary of column headers in the form {index:column_header}
    lookup_dict =  reverse dictionary of column headers in the form {column_header:index}

    Note that the test file 'master_test.csv' contains only IDs starting with 'a'.

    >>> len(import_master('master_test.csv')['data'])
    438
    """

    data_label = 'data'
    header_label = 'header'
    lookup_label = 'lookup'

    file_size = os.stat(file_path).st_size
    f = open(file_path)
    header = f.readline().strip().split(',')
    header_dict = dict()
    lookup_dict = dict()
    master_dict = dict()

    for i in range(len(header)):
        header_dict[i] = header[i]
        lookup_dict[header[i]] = i

    bytes_read = 0
    for line in f:
        if verbose:
            bytes_read += len(line)
            fraction = round(float(bytes_read) / file_size, 2)
            pb.update_progress(fraction, "Importing '" + file_path + "'")

        data = line.strip().split(',')
        for index, item in enumerate(data):
            if item == '':
                data[index] = 0

        entry_dict = dict()
        for i in range(len(data)):
            entry_dict[header_dict[i]] = convert_to_number(data[i])
        player_id = entry_dict['playerID']
        if player_id not in master_dict:
            master_dict[player_id] = entry_dict

    if verbose:
        pb.update_progress(1.0, "Importing '" + file_path + "'")
        print ''
    f.close()
    return {data_label: master_dict, header_label: header_dict, lookup_label: lookup_dict}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
