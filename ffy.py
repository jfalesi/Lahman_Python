from lahmanator_fns import *
from unprog import update_progress as up

masterFile = 'Master.csv'
batFile = 'Batting_lahman.csv'
fieldFile = 'Fielding_lahman.csv'
pitchFile = 'Pitching_lahman.csv'

string = "Importing master player data from '" + masterFile
masterDict, masterHeader, masterLookup = importMaster(masterFile, string)
string = "Importing batting data from '" + batFile
batDict, batHeader, batLookup = importBat(batFile, string)
string = "Importing fielding data from '" + fieldFile
fieldDict, fieldHeader, fieldLookup = importFld(fieldFile, string)
string = "Importing pitching data from '" + pitchFile
pitchDict, pitchHeader, pitchLookup = importPitch(pitchFile, string)

data = 'data'
header = 'header'
lookup = 'lookup'
master= 'master'
bat = 'bat'
field = 'field'
pitch = 'pitch'

masterDicts = {data:masterDict, header:masterHeader, lookup:masterLookup}
batDicts = {data:batDict, header:batHeader, lookup:batLookup}
fieldDicts = {data:fieldDict, header:fieldHeader, lookup:fieldLookup}
pitchDicts = {data:pitchDict, header:pitchHeader, lookup:pitchLookup}

dicts = {master:masterDicts, bat:batDicts, field:fieldDicts, pitch:pitchDicts}

def getFirstYear(ID, dataDict):
    """
    returns the first year in the league for the player identified by "ID"
    based on data in dataDict

    >>> getFirstYear('tulowtr01', importBat()[0])
    2006
    >>> getFirstYear('priceda01', importPitch()[0])
    2008
    >>> getFirstYear('tulowtr01', importFld()[0])
    2006
    """
    try:
        playerData = dataDict[ID]
    except KeyError:
        print "Player '" + ID + "' does not appear in the indicated dictionary."
        raise KeyError

    playerYears = sorted(playerData.keys())

    return playerYears[0]

def writeFirstYears(playerFile, dicts, importFile):
    """
    writes to importFile a string of the form "ID, first_year" for each player in playerFile

    playerFile: file of player IDs
    dicts: dictionary of dictionaries of the form:
        dicts['master'] = masterDicts
        dicts['bat'] = batDicts
        dicts['field'] = fieldDicts
        dicts['pitch'] = pitchDicts

        where each <>Dict is of the form:
            <>Dict['data'] = <>Dict = dictionary of player data keyed by ID
            <>Dict['header'] = <>HeaderDict = dictionary of columns keyed by name
            <>Dict['lookup'] = <>LookupDict = dictionary of column names keyed by column number
    importFile: file to which data is written, intended to be imported into OOTP
    """    

    print "Opening '" + playerFile + "'..."

    try:
        f = open(playerFile, 'r')
    except IOError:
        print "File '" + playerFile + "' does not exist."
        return

    playerList = []

    for line in f:
        playerID = line.strip()
        if playerID != '':
            print "Reading '" + playerID + "'..."
            playerList.append(playerID)

    f.close()
    print "Finished reading players.\n"

    g = open(importFile, 'w')

    print "Creating '" + importFile + "'..."
    for ID in playerList:
        print "Looking up '" + ID + "'..."
        try:
            fYear = getFirstYear(ID, fieldDict)
            print "First year for '" + ID + "' is " + str(fYear) + "."
        except KeyError:
            print "Skipping '" + ID + "'..."
        else:
            print "Writing '" + ID + "'..."
            outString = ID + ', ' + str(fYear) + '\n'
            g.write(outString)

    prstr = "Finished writing '" + importFile + "'.  The file is now ready to be imported into OOTP.\n"
    print prstr

    print "Closing '" + importFile + "'..."
    g.close()
    print "Closed."
    print "Returning..."
    return

writeFirstYears('playerfile.txt', dicts, 'importFile.csv')
print "Returned."

##if __name__=="__main__":
##    import doctest
##    doctest.testmod()
