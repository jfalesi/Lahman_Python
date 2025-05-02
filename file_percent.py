import sys
import os


def get_file_fract(bytes_read, filename):
    """
    returns the fraction of the indicated file that is contained in "bytes_read"
    :param bytes_read: number of bytes read from the file
    :param filename: file being imported
    """

    file_size = os.stat(filename).st_size
    fract = float(bytes_read) / file_size
    return fract

# filename = "Master.csv"
# f = open(filename)
# bytes_read = 0
# for line in f:
#     bytes_read += len(line)
#     print get_file_fract(bytes_read, filename)