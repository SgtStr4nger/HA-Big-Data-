# Importing data for analysis

import pandas as pd

from data.acc_covdata import C_Data_per_bev
from data.acc_hospidata import H_Rate


def Create_C_Data():
    C_Data = pd.DataFrame.from_dict(C_Data_per_bev(), orient='columns')
    C_Data.to_pickle('C_Data.pkl')
    return C_Data

def Create_H_Data():
    H_Data = pd.DataFrame.from_dict(H_Rate(), orient='columns')
    H_Data.to_pickle('H_Data.pkl')
    return H_Data

