# dann auf Bewohner pro 100k Einwohner 
import csv
import datetime
from collections import namedtuple, defaultdict
import util

csvData = util.read_csvData("./data/raw-data/zeitreihe-tagesdaten.csv", 0, 2 ,5, ",")

# # #[Kommentar]Daten in einem Namedtupel zusammenführen
Tagesdaten_Hospitalisierungen = namedtuple("Tagesdaten_Hospitalisierungen", ("Datum", "Ort", "Anzahl"))
Hospitalisierungsdaten = (Tagesdaten_Hospitalisierungen(row[0], int(row[1]), int(row[2])) for row in csvData)
 
#Hospitalisierungen {LK_ID{Datum: Anzahl}}, Rate berechnen bei Verarbeitung?
akk_Hospitalisierungen = util.acc_Data(Hospitalisierungsdaten)

print(akk_Hospitalisierungen)
