class Era(object):
    """
    Earned Run Average
    """
    def __init__(self, ip=0, er=0):
        """
        """
        self.ip = float(ip)
        self.er = int(er)
        self.compute_era()
        return

    def compute_era(self):
        """
        """
        if self.ip == 0 and self.er == 0:
            self.value = 0.0
        else:
            try:
                self.value = self.er/self.ip * 9
            except ZeroDivisionError:
                self.value = float('inf')
    
    def merge(self, ip, er):
        """
        """
        self.ip += ip
        self.er += er
        self.compute_era()

    def print_val(self):
        """
        """
        print("{0:.2f}".format(round(self.value,2)))
        return
