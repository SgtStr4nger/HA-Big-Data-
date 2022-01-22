import csv

mainDataSrcFile = "./raw-data/Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv"

def readCovidData(path):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        data = [[row[1], row[3], row[4]] for row in csvreader]
        return data[1:]

def accumulateByLandkreis(data, impfno):
    landkreise = {}
    for row in data:
        if row[1] == impfno:
            landkreis = row[0]
            landkreise[landkreis] = landkreise.get(landkreis, 0) + int(row[2])
    return landkreise

def getData():    
    data = readCovidData(mainDataSrcFile)
    landkreisImpfungen = { i : accumulateByLandkreis(data, f"{i}") for i in range(1, 4)}
    return landkreisImpfungen

    
if __name__ == "__main__":
    data = readCovidData(mainDataSrcFile)
    landkreisImpfungen = { i : accumulateByLandkreis(data, f"{i}") for i in range(1, 4)}
    print(landkreisImpfungen[1]["13003"])
