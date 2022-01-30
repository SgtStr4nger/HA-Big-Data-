# dann auf Bewohner pro 100k Einwohner 
import csv
import datetime
from collections import namedtuple, defaultdict
from data import util

csvData = util.read_csvData("../data/raw-data/zeitreihe-tagesdaten.csv", 0, 2 ,5, ",")

# # #[Kommentar]Daten in einem Namedtupel zusammenführen
Tagesdaten_Hospitalisierungen = namedtuple("Tagesdaten_Hospitalisierungen", ("Datum", "Ort", "Anzahl"))
Hospitalisierungsdaten = (Tagesdaten_Hospitalisierungen(row[0], int(row[1]), int(row[2])) for row in csvData)
 
#Hospitalisierungen {LK_ID{Datum: Anzahl}}, Rate berechnen bei Verarbeitung?
akk_Hospitalisierungen = util.acc_Data(Hospitalisierungsdaten)
bevDaten = util.bev_to_Dict()

def H_Rate ():
    hospirate = {
        LK_IDs: {date: hospitalisierungen / bevDaten[LK_IDs] * 100_000 for date, hospitalisierungen in values.items()}
        for LK_IDs, values in akk_Hospitalisierungen.items()}
    return hospirate

hospirate = H_Rate()
#print(hospirate[1001])
