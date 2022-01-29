import csv
import datetime
import pandas as pd
from collections import namedtuple, defaultdict
from data import util
from data.LK_Data import DictBevBundesland

vaccineData = "../data/raw-data/Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv"

#[Kommentar]Datum, Ort, Impfung(Grundimmuniesierung, Booster), Anzahl aus Quelle auslesen
def read_vaccData():
    with open(vaccineData) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = [[row[0], row[1], row[3], row[4]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

bevDict = util.bev_to_Dict()
DictBLBev = DictBevBundesland()
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


# Erstelle Dict mit LK_ID, Date und Liste [0, 0]
def createVDict (BaseDict):
    date_generated = pd.date_range(datetime.date(2019, 6, 1),datetime.date(2022, 2, 16))
    emptyDict = defaultdict(dict)
    for id in BaseDict:
        for Date in date_generated:
            emptyDict[id][Date.strftime('%Y-%m-%d')] = [0, 0]
    return emptyDict

# Aus Tupeln ein Nested Dict formen: {LK_ID: {Datum: [Grundimmun][Booster]} }
vTupel = put_Into_Tuple()
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
    return Dict


def V_Dict_BL( lk_Dict ):
# kummuliere Impfungen aller LK eines BLs
    VDict_BL=createVDict(DictBevBundesland())
    for bl_id in VDict_BL:
        for lk_id in lk_Dict:
            if int(lk_id/1000)==bl_id:
                for date in lk_Dict[lk_id]:
                    VDict_BL[bl_id].update({date: [x + y for x, y in zip( VDict_BL[bl_id][date], lk_Dict[lk_id][date] ) ] })

# Impfquote des BL
        for date in VDict_BL[bl_id]:
            VDict_BL[bl_id].update({date: [x / DictBLBev[bl_id] for x in VDict_BL[bl_id][date]]})

    return VDict_BL




def V_Datensatz_erstellen():
    return V_Dict_BL(Dict_kummulieren(acc_Data(createVDict(bevDict))))


# Print Impfquote am 16.02.2022 aller IDs im gegebenen Dict.
def Print_V_Dataset(Data):
    for id in Data:
        print(id, ":", Data[id]['2022-02-16'])



#Print_V_Dataset(V_Dict_BL())
