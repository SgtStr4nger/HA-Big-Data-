import csv

#Data Source Bevölkerungszahlen: DeStatis https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html (26.01.22 / Datenstand: 31.12.2020)

def read_csvData(path, r1, r2, r3, delim):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=delim)
        data = [[row[r1], row[r2], row[r3]] for row in csvreader]
        #Data zu Testzwecken auf alle Datensätze begrenzt
        return data[1:]

#Bevölkerungsdaten je Landkreis auslesen
def read_bevData():
    with open("./raw-data/Bev_Kreise.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        data = [[row[0], row[1]] for row in csvreader]
        #Keine Überschrift → Return everything
        return data

def bev_to_Dict():
    bevData = read_bevData()
    bevDict = {int(row[0]):int(row[1]) for row in bevData}
    return bevDict