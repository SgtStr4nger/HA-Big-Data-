import csv
from datetime import date
from collections import namedtuple

vaccineData = "Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv"
covidData = "Aktuell_Deutschland_SarsCov2_Infektionen.csv"

#[Kommentar]Impfzahlen und Infektionszahlen je Ort und Datum aus Quelle auslesen
def read_Data(path,c1,c2,c3):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = [[row[c1], row[c2], row[c3]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

vData = read_Data(vaccineData, 0 ,1 , 4)
cData = read_Data(covidData, 3 ,0 , 9)

#[Kommentar]Daten in einem Namedtupel zusammenführen
TupelData = namedtuple("Tupeldata", ("Datum", "Ort", "Anzahl"))

def put_Into_Tuple(Data):
    TupleList = []
    for i in range(len(Data)):
        if Data[i][1] != 'u':
            TupleList.append(TupelData(Data[i][0],int(Data[i][1]), int(Data[i][2])))
    return TupleList

vTupel = put_Into_Tuple(vData)
cTupel = put_Into_Tuple(cData)


#[Kommentar]Aus Tupeln ein Dict formen, filterung über Ort+Datum
def acc_Data(Data):
    akkData = {}
    for row in Data:
        key =(row.Datum, row.Ort)
        akkData[key] = akkData.get(key,0) + row.Anzahl
    return akkData
vDict = acc_Data(vTupel)
cDict = acc_Data(cTupel)

#Aufruf der Daten: vDict[('yyyy-mm-dd', 'xxxxx')]
x = ('2022-01-15', 1003)
#print("anzahl Impfungen:", vDict[x])
print("anzahl Fälle:", cDict[x])
print("anzahl Impfungen", vDict[x])
