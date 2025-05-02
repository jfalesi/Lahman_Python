class player_year_data(dict):
    """
    entry for player for particular year
    """
    def __init__(self, data=[], header=[]):
        """
        """
        dict.__init__(self)
        for key in header:
            self[header[key]] = data[key]
        return

    def merge_stint(self, stint=None):
        """
        """
        if not stint:
            print "Empty stint ignored."
            return
        
        for key in self:
            item_1 = self[key]
            item_2 = stint[key]
            item_1.merge(item_2)
        return

class data_item(object):
    """
    item in player_year_data
    """
    def __init__(self, data, data_type):
        self.type = data_type
        self.data = data
        self.intrinsic_type = type(data)

