import csv, datetime
import pandas as pd
from collections import namedtuple, defaultdict

def read_csvData(path, r1, r2, r3, delim):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delim)
        data = [[row[r1], row[r2], row[r3]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

#Bevölkerungsdaten je Landkreis auslesen
def read_bevData():
    with open("../data/raw-data/Bev_Kreise.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        data = [[row[0], row[1]] for row in csvreader]
        #Keine Überschrift → Return everything
        return data

def bev_to_Dict():
    bevData = read_bevData()
    bevDict = {int(row[0]):int(row[1]) for row in bevData}
    return bevDict

def createCDict (BaseDict):
    date_generated = pd.date_range(datetime.date(2019, 6, 1),datetime.date(2022, 2, 16))
    emptyDict = defaultdict(dict)
    for id in BaseDict:
        for Date in date_generated:
            emptyDict[id][Date.strftime('%Y-%m-%d')] = 0
    return emptyDict

#[Kommentar] Aus Tupeln ein Nested Dict formen: {LK_ID: {Datum: Value} }
def acc_Data(data):
    akkData = createCDict(bev_to_Dict())
    for row in data:
        date = row[0]
        lk_id = row[1]
        value = row[2]
        # Exception for Berlin (lk_id 1100X), as there is only population data for whole Berlin
        if lk_id in range (11000,11013):
            akkData[11000][date] = akkData[11000][date]+value
        elif lk_id in akkData and date in akkData[lk_id]:
            akkData[lk_id][date] = akkData[lk_id][date]+value
    return akkData
#why tho? 
def C_Datensatz_erstellen (data):
    return acc_Data(data)