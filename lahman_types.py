# test comment

class IntItem(int):
    """
    item class for integer type
    """
    def __init__(self, num):
        """
        """
        int.__init__(self)
        self = num
        return

    def merge(num):
        """
        """
        self += num
        return
    
class StrItem(str)
    """
    item class for string type
    """
    def __init__(self, string):
        """
        """
        str.__init__(self)
        self = string
        return
    
    def merge(string)
        """
        """
        self = self + ', ' + string
        return

class BattAvgItem(object):
    """
    batting average
    """
    def __init__(self, at_bats=0, hits=0):
        """
        """
        self.at_bats = int(at_bats)
        self.hits = int(hits)
        self.compute_avg()
        return

    def compute_avg(self):
        """
        """
        if self.at_bats == 0 and self.hits == 0:
            self.value = 0.0
        else:
            try:
                self.value = float(self.hits)/self.at_bats
            except ZeroDivisionError:
                self.value = float('inf')
    
    def merge(self, at_bats, hits):
        """
        """
        self.at_bats += at_bats
        self.hits += hits
        self.compute_avg

    def print_val(self):
        """
        """
        self.compute_avg()
        print("{0:.3f}".format(round(self.value,3)))
        return

class EraItem(object):
    """
    Earned Run Average
    """
    def __init__(self, ip=0, er=0):
        """
        """
        self.innings_pitched = float(ip)
        self.earned_runs = int(er)
        self.compute_era()
        return

    def compute_era(self):
        """
        """
        if self.innings_pitched == 0 and self.earned_runs == 0:
            self.value = 0.0
        else:
            try:
                self.value = self.earned_runs/self.innings_pitched * 9
            except ZeroDivisionError:
                self.value = float('inf')
    
    def merge(self, ip, er):
        """
        """
        self.innings_pitched += ip
        self.earned_runs += er
        self.compute_era()

    def print_val(self):
        """
        """
        print("{0:.2f}".format(round(self.value,2)))
        return

class ZoneRatingItem(object):
    """
    """
    def __init__(self, val):
        self.value = val
    
