from collections import namedtuple

from data import util
from data.util import bev_to_Dict

cData = util.read_csvData("./data/raw-data/Aktuell_Deutschland_SarsCov2_Infektionen.csv", 3,0,9, ",")

#Daten in einem Namedtupel zusammenführen
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
def C_Data_per_bev():
    CDict = C_Datensatz_erstellen()
    BevDict = bev_to_Dict()
    for lk_id in CDict:
        if lk_id in BevDict:
            for date in CDict[lk_id]:
                CDict[lk_id].update({date: (CDict[lk_id][date]/BevDict[lk_id] * 100000) } )
        else: print(lk_id)
    return CDict
