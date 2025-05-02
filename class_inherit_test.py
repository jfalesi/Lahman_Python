class int_type(object):
    def __init__(self, num):
        self.val = int(num)
        return

    def merge(self, num):
        self.val += num
        return

a = int_type(3)
print a.val
a.merge(4)
print a.val
