#
# read lahman database and do stuff
#
# For example, read a player's stats over his/her career and create a single entry that represents the average of the player's stats
# Could also pick a set of stats representative of best seasons
# Could do all kinds of wicked cool stuff
#

import numpy as np
from lahmanator_fns import *

masterDict, masterHeader, masterLookup = importMaster('Master_longo.csv')
batDict, batHeader, batLookup = importBat('Batting_longo.csv')
avgDict = dict()

ID = 'longoev01'

longo = batDict[ID]
num_years = len(longo)
num_cols = len(longo[longo.keys()[0]])

num_data = np.zeros(num_cols)

for year in longo:
    year_data = longo[year]
    ordered_data = orderedStats(year_data, batHeader)
    num_data += np.array([entry for entry in ordered_data if type(entry) == int])


##for key in avgDict:
##    if type(avgDict(key)) == int:
##        avgDict[key] = avgDict[key]/num_years
