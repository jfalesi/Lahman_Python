from item_type_defs import *

class year_entry(dict):
    """
    """

    def __init__(self, data=None):
        """
        """
        dict.__init__(self)
        try:
            self.year_id = data['year_id']
            self['player_id'] = string_item(data['player_id'])
            
            return
        except KeyError:
            print "Data does not contain 'year_id' field in method year_entry.__init__()"
            print "Data is '" + str(self)
            return

    def add_stint(self, stint_data):
        """
        merges stint into existing player data
        """

        for key in self:
            item = self[key]
            item_to_merge = stint_data[key]
            item.merge(item_to_merge)
        return

class player_entry(dict):
    """
    player entry in a lahman data dictionary
    could be batting, pitching, or fielding entry
    player_entry is a dictionary of the form {'year_id': data}
    """

    def __init__(self, data=None):
        """
        creates player entry - pass this fuction a single row of data from a lahman file in dict form

        :param data #  dict of either batting, pitching or fielding data for a player in form
                        {'header': 'data_item', ... }
        """
        dict.__init__(self)
        try:
            self.player_id = data['player_id']
            year = data['year_id']
            self[year] = year_entry(data)
        except KeyError:
            print "Data does not contain 'player_id' field in method player_entry.__init__()"
            print "Data is '" + str(self)
        return

    def add_year_data(self, data=None):
        """
        adds data from 'data' to player_entry
        """
        if not data:
            print "Empty data ignored in method add_year_data()"
            return
        
        assert data['player_id'] == self.player_id
        year_to_add = data['year_id']

        if year_to_add not in self:
            self[year_to_add] = year_entry(data)

        else:
            year = year_to_add
            stint_to_add = data['stint']
            existing_stints = self[year]['stint']
            if stint_to_add not in existing_stints:
                self[year].add_stint(data)

        return


