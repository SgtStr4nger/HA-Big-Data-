# Quelle: https://www.corona-daten-deutschland.de/dataset/intensivstationen
# Anzahl Fälle im KH, dann auf Bewohner mappen, dann auf Bewohner pro 100k Einwohner 
import csv
import datetime
from collections import namedtuple, defaultdict
import util

hospiDataPath = "./data/raw-data/zeitreihe-tagesdaten.csv"

csvData = util.read_csvData(hospiDataPath, 0, 2 ,5, ",")

# # #[Kommentar]Daten in einem Namedtupel zusammenführen
Tagesdaten_Hospitalisierungen = namedtuple("Tagesdaten_Hospitalisierungen", ("Datum", "Ort", "Anzahl"))
Hospitalisierungsdaten = (Tagesdaten_Hospitalisierungen(row[0], int(row[1]), int(row[2])) for row in csvData)
 
akk_Hospitalisierungen = util.acc_Data(Hospitalisierungsdaten)


