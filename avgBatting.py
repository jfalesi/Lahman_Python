#
# avgBatting.py
#

from lahmanator_fns import *

batTypeDict = {'playerID':str, 'yearID':str, 'stint':str, 'teamID':str, 'lgID':str,
               'G':int, 'G_batting':int, 'AB':int, 'R':int, 'H':int, '2B':int, '3B':int,
               'HR':int, 'RBI':int, 'SB':int, 'CS':int, 'BB':int, 'SO':int, 'IBB':int,
               'HBP':int, 'SH':int, 'SF':int, 'GIDP':int, 'G_old':int}

yearsToAvg = [2009, 2010, 2011, 2013]
playerID = 'tulowtr01'
dataToAvg = dict()

batDict, batHeaderDict, batLookupDict = importBat('batting.csv')

for year in yearsToAvg:
    dataToAvg[year] = batDict[playerID][year]

avgDict = computeAvg(dataToAvg, batHeaderDict, batTypeDict)

yearToAdd = 2015
avgDict['yearID'] = yearToAdd
lahmanData = {yearToAdd:avgDict}

f = open('batting.csv', 'a')

entry = addEntry(playerID, yearToAdd, lahmanData, lahmanData, batHeaderDict, batHeaderDict, batTypeDict)

f.write(entry)
f.close()
