class BattAvg(object):
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
