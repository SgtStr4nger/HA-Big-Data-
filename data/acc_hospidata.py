# Quelle: https://www.corona-daten-deutschland.de/dataset/intensivstationen
# Anzahl Fälle im KH, dann auf Bewohner mappen, dann auf Bewohner pro 100k Einwohner 
import csv
import datetime
from collections import namedtuple, defaultdict
import util

hospiDataPath = "./data/raw-data/zeitreihe-tagesdaten.csv"

csvData = util.read_csvData(hospiDataPath, 0, 2 ,5, ",")

# # #[Kommentar]Daten in einem Namedtupel zusammenführen
Hospitalisierungen = namedtuple("Hospitalisierungen", ("Datum", "Ort", "Anzahl"))

hospiData = (Hospitalisierungen(row[0], int(row[1]), int(row[2])) for row in csvData)
 
print(hospiData)
#hTupel = []
    # for i in range(len(vaccData)):
    #             TupleList.append(Hospitalisierungen((hospiData[i][0]), int(hospiData[i][1]), 0, int(hospiData[i][3])))
    # return TupleList


