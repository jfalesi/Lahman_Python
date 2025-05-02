#
# Update the Fielding2.csv file in the OOTP stats folder with entries in the latest
# Lahman database.  Averages fields that are not present in the Lahman database
# over the years in the OOTP database.
#

import numpy as np
from lahmanator_fns import *

fldTypeDict = {'playerID':str, 'yearID':str, 'stint':str, 'teamID':str, 'lgID':str,
               'POS':str, 'G':int, 'GS':int, 'InnOuts':int, 'PO':int, 'A':int, 'E':int,
               'DP':int, 'PB':int, 'WP':int, 'SB':int, 'CS':int, 'ZR':float, 'RF1':float,
               'RF3':float, 'Cability':int, 'Carm':int, 'OFarm':int, 'IndPO':int,
               'IndA':int}

fldDict, fldHeader, fldLookup = importFld('Fielding2.csv')

lahFldDict, lahFldHeader, lahFldLookup = importFld('Fielding_lahman.csv')

entriesToAdd = dict()

for player in lahFldDict:
    lahmanData = lahFldDict[player]
    OOTP_Data = fldDict[player]
    for year in lahmanData:
        if year not in OOTP_Data:
            entriesToAdd[player, year] = addEntry(player, year, lahmanData, OOTP_Data, fldHeader, lahFldHeader)

fldFile = 'Fielding2.csv'
f = open(fldFile, 'a')
for key in entriesToAdd:
    f.write(entriesToAdd[key])
f.close()

if __name__=="__main__":
    import doctest
    doctest.testmod()
