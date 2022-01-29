import csv
from datetime import date
from collections import namedtuple, defaultdict
from data import util

cData = util.read_csvData("../data/raw-data/Aktuell_Deutschland_SarsCov2_Infektionen.csv", 3,0,9, ",")

#[Kommentar]Daten in einem Namedtupel zusammenführen
TupelData = namedtuple("Tupeldata", ("Datum", "Ort", "Anzahl"))

def put_Into_Tuple():
    TupleList = []
    for i in range(len(cData)):
        if cData[i][1] != 'u':
            TupleList.append(TupelData(cData[i][0],int(cData[i][1]), int(cData[i][2])))
    return TupleList

def C_Datensatz_erstellen():
    return util.acc_Data(put_Into_Tuple())

# Corona Data based on population of LK
def C_Data_per_bev(CDict, BevDict):
    #Exception for Berlin (lk_id 1100X), as there is only population data for whole Berlin
    for lk_id in range (11001, 11013):
        for date in CDict[lk_id]:
            CDict[11000].update({date: CDict[lk_id][date]})
        del CDict[lk_id]
    for lk_id in CDict:
        if lk_id in BevDict:
            for date in CDict[lk_id]:
                CDict[lk_id].update({date: (CDict[lk_id][date]/BevDict[lk_id]) } )
        else: print(lk_id)
    return CDict


#Fallzahlen in ein Namedtupel formen und daraus ein Dict bilden
fallzahlen = util.acc_Data(put_Into_Tuple())

#print(C_Datensatz_erstellen())