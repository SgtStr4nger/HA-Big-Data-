import csv
from datetime import date
from collections import namedtuple, defaultdict
import util

cData = util.read_csvData("raw-data\\Aktuell_Deutschland_SarsCov2_Infektionen.csv", 3,0,9, ",")

#[Kommentar]Daten in einem Namedtupel zusammenführen
TupelData = namedtuple("Tupeldata", ("Datum", "Ort", "Anzahl"))

def put_Into_Tuple():
    TupleList = []
    for i in range(len(cData)):
        if cData[i][1] != 'u':
            TupleList.append(TupelData(cData[i][0],int(cData[i][1]), int(cData[i][2])))
    return TupleList

#Fallzahlen in ein Namedtupel formen und daraus ein Dict bilden
cTupel = put_Into_Tuple()
fallzahlen = util.acc_Data(cTupel)

print(fallzahlen)
