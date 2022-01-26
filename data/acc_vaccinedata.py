import csv
from datetime import date
from collections import namedtuple, defaultdict

#Data Source Impfungen/Infektionen: RKI https://github.com/robert-koch-institut (25.01.22)
#Data Source Bevölkerungszahlen: DeStatis https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html (26.01.22 / Datenstand: 31.12.2020)
# LK 17000 : Bundesressort → Daten aus Impfungen durch den Bund, keine Ortsangabe, ergo keine Bevölkerungszahlen auffindbar
#Impfungen aufteilen in Grundimmunisiert (=Impfstatus 2, da J&J als zweitimpfungen eingetragen wurden) und Geboostert 
vaccineData = "Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv"
bevData = "raw-data\Bev_Kreise.csv"

#[Kommentar]Datum, Ort, Impfung(Grundimmuniesierung, Booster), Anzahl aus Quelle auslesen
def read_vaccData():
    with open(vaccineData) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = [[row[0], row[1], row[3], row[4]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

#[Kommentar] Bevölkerungsdaten je Landkreis auslesen
def read_bevData():
    with open(bevData) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        data = [[row[0], row[1]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

def bev_to_Dict():
    bevData = read_bevData()
    bevDict = {int(row[0]):int(row[1]) for row in bevData}
    return bevDict

bevDict = bev_to_Dict()
vaccData = read_vaccData()

# # #[Kommentar]Daten in einem Namedtupel zusammenführen
TupelData = namedtuple("Tupeldata", ("Datum", "Ort", "Grundimmunisierung", "Booster"))

def put_Into_Tuple():
    TupleList = []
    for i in range(len(vaccData)):
        if vaccData[i][1] != 'u':
            if vaccData[i][2] == '2':
                TupleList.append(TupelData((vaccData[i][0]), int(vaccData[i][1]), int(vaccData[i][3]), 0))
            if vaccData[i][2] == '3':
                TupleList.append(TupelData((vaccData[i][0]), int(vaccData[i][1]), 0, int(vaccData[i][3])))
    return TupleList

vTupel = put_Into_Tuple()


# #[Kommentar]Aus Tupeln ein Nested Dict formen: {LK_ID: {Datum: [Grundimmun][Booster]} }
def acc_Data():
    akkData = {}
    for row in vTupel:
        date, lk_id, basicimmun, boost = row[0], row[1], row[2], row[3]
        #[Kommentar] Check, ob korrespondierende Bevölkerungszahlen vorhanden
        if row[1] in bevDict:
            if lk_id in akkData and date in akkData[lk_id]:
                akkData[lk_id][date[0]] = [[akkData[lk_id][date[0]] + (basicimmun/ bevDict[row[1]])],akkData[lk_id][date[1]] + (boost/ bevDict[row[1]])]
            else:
                akkData[lk_id][date[1]] = [ (basicimmun/ bevDict[row[1]]) , (boost/ bevDict[row[1]])  ]
    return akkData
accc_DATA = acc_Data()
print(accc_DATA)
# vDict = acc_Data(vTupel)
# print(vDict[5314])

