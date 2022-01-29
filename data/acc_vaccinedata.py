import csv
import datetime
import pandas as pd
from collections import namedtuple, defaultdict
import util

#Data Source Impfungen/Infektionen: RKI https://github.com/robert-koch-institut (25.01.22)
#Data Source Bevölkerungszahlen: DeStatis https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html (26.01.22 / Datenstand: 31.12.2020)
# LK 17000 : Bundesressort → Daten aus Impfungen durch den Bund, keine Ortsangabe, ergo keine Bevölkerungszahlen auffindbar
#Impfungen aufteilen in Grundimmunisiert (=Impfstatus 2, da J&J als zweitimpfungen eingetragen wurden) und Geboostert 
vaccineData = "data\\raw-data\\Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv"

#[Kommentar]Datum, Ort, Impfung(Grundimmuniesierung, Booster), Anzahl aus Quelle auslesen
def read_vaccData():
    with open(vaccineData) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = [[row[0], row[1], row[3], row[4]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]


bevDict = util.bev_to_Dict()
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

# Erstelle Dict mit LK_ID, Date und Liste [0, 0]
def createDict ():
    date_generated = pd.date_range(datetime.date(2019, 6, 1),datetime.date(2022, 2, 16))
    emptyDict = defaultdict(dict)
    for lk in bevDict:
        for Date in date_generated:
            emptyDict[lk][Date.strftime('%Y-%m-%d')] = [0, 0]
    return emptyDict

# #[Kommentar]Aus Tupeln ein Nested Dict formen: {LK_ID: {Datum: [Grundimmun][Booster]} }
def acc_Data(empty_dict):
    akkData = empty_dict
    for row in vTupel :
        date, lk_id, basicimmun, boost = row[0], row[1], row[2], row[3]
# [Kommentar] Einordnen der Zahlen in Dict, ausgenommen LK 17000 → Bundesresort
        if lk_id in akkData and date in akkData[lk_id] and lk_id != 17000:
            akkData[lk_id].update({date: [x + y for x, y in zip(akkData[lk_id][date], [basicimmun, boost])]})
    return akkData

def Dict_kummulieren ( Dict):
    for lk_id in Dict:
        for Date in Dict[lk_id]:

            #TODO: Optimize Date-1
            Date_as_datetime = datetime.datetime.strptime(Date, '%Y-%m-%d')
            Date_before = Date_as_datetime - datetime.timedelta(days=1)
            Date_before = datetime.datetime.strftime(Date_before, '%Y-%m-%d')
# Addiere Impfungen am Date zu denen vom Tag zuvor
            if Dict[lk_id].get(Date_before) != None:
                Dict[lk_id].update({Date: [x + y for x, y in zip(Dict[lk_id][Date_before], Dict[lk_id][Date]) ] })

# Teile Impfungen pro Tag durch Bevölkerung des Landkreises
        for Date in Dict[lk_id]:
            Dict[lk_id].update({Date: [x / bevDict[lk_id] for x in Dict[lk_id][Date]]})

    return Dict

def V_Datensatz_erstellen():
    return Dict_kummulieren(acc_Data(createDict()))

def Print_V_Dataset(Data):
    for lk_id in Data:
        print(lk_id, ":", Data[lk_id]['2022-02-16'])


V_Datensatz = V_Datensatz_erstellen()
#Print_V_Dataset(V_Datensatz)
#print(V_Datensatz)

#print(V_Datensatz[16077]['2022-02-16'][0])


