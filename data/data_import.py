import pandas as pd

def import_fallzahlen_lk ():
    df = pd.read_excel ('data/raw-data/Fallzahlen_Kum_Tab.xlsx', sheet_name=5 , engine='openpyxl')
    print ( df )
