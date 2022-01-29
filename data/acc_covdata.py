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

#Fallzahlen in ein Namedtupel formen und daraus ein Dict bilden
fallzahlen = util.acc_Data(put_Into_Tuple())

#print(C_Datensatz_erstellen())