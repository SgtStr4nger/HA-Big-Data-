import pandas as pd

def import_fallzahlen_lk ():
    # Load Inzidenz Zahlen pro Landkreis as dataframe
    df = pd.read_excel ('data/raw-data/Fallzahlen_Kum_Tab.xlsx', sheet_name=5 , header=4, engine='openpyxl')
    # removing unnecessary rows at end of dataframe, transform for easier user
    df = df.drop(range(411,416))
    df = df.sort_values(by=['NR'])
    df = df.reset_index ( drop=True )
    print ( df )



#TODO: Add import for other data