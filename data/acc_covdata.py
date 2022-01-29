import csv
from datetime import date
from collections import namedtuple, defaultdict
import util

#Data Source Impfungen/Infektionen: RKI https://github.com/robert-koch-institut (25.01.22)
#Data Source Bevölkerungszahlen: DeStatis https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html (26.01.22 / Datenstand: 31.12.2020)
# LK 17000 : Bundesressort → Daten aus Impfungen durch den Bund, keine Ortsangabe, ergo keine Bevölkerungszahlen auffindbar
#Impfungen aufteilen in Grundimmunisiert (=Impfstatus 2, da J&J als zweitimpfungen eingetragen wurden) und Geboostert 

cData = util.read_csvData("raw-data\\Aktuell_Deutschland_SarsCov2_Infektionen.csv", 3,0,9, ",")

#[Kommentar]Daten in einem Namedtupel zusammenführen
TupelData = namedtuple("Tupeldata", ("Datum", "Ort", "Anzahl"))

def put_Into_Tuple():
    TupleList = []
    for i in range(len(cData)):
        if cData[i][1] != 'u':
            TupleList.append(TupelData(cData[i][0],int(cData[i][1]), int(cData[i][2])))
    return TupleList

cTupel = put_Into_Tuple()
fallzahlen = util.acc_Data(cTupel)
print(fallzahlen)
