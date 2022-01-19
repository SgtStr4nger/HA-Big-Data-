import pandas as pd

def import_Fallzahlen ():
    df = pd.read_excel ('data/raw-data/Fallzahlen_Kum_Tab.xlsx')
    print ( df )
