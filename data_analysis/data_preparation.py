# Preparing data for analysis
from collections import defaultdict

import pandas as pd, matplotlib.pyplot as plt

from data.acc_covdata import C_Datensatz_erstellen, C_Data_per_bev
from data.acc_hospidata import H_Rate
from data.acc_vaccinedata import V_Datensatz_erstellen, V_Dict_LK




def Create_C_Data():
    C_Data = pd.DataFrame.from_dict(C_Data_per_bev(), orient='columns')
    C_Data.to_pickle('C_Data.pkl')
    return C_Data

def Load_C_Data():
    val = input("Create [C] or load [L] Data")
    if val in ["C", "c"]:
        return Create_C_Data()
    else:
        try:
            C_Data = pd.read_pickle('../data_analysis/C_Data.pkl')
        except IOError:
            print("File could not be found, creating file now...")
            C_Data = Create_C_Data()
        return C_Data

def DF_V ():
    data = V_Dict_LK()
    build1 = defaultdict(list)
    build2 = defaultdict(list)
    keys = ['date'] + list(data.keys())
    for k, v in data.items():
        for k1, v1 in v.items():
            build1[k1].append(v1[0])
            build2[k1].append(v1[1])
    build1 = [[k] + v for k, v in build1.items()]
    build2 = [[k] + v for k, v in build2.items()]
    df1 = pd.DataFrame(build1, columns=keys).set_index('date')
    df2 = pd.DataFrame(build2, columns=keys).set_index('date')

    return df1,df2


def PrintDFCorr():
    CperB_df = pd.DataFrame.from_dict(C_Data_per_bev(), orient='columns')

    HperB_df = pd.DataFrame.from_dict(H_Rate(), orient='columns')
    D1= 700
    HperCperB_df = (HperB_df[D1:] / CperB_df[D1:])
    V1_df, V2_df =DF_V()
    print("C per B:\n", CperB_df[D1:])
    print("H per B:\n", HperB_df[D1:])
    print("V1 per B:\n", V1_df[D1:])
    print("H/C per B:\n", HperCperB_df)
    print("Corr V1 C per B:\n", V1_df[D1:].corrwith(CperB_df[D1:]))
    print("Corr V1 H per B:\n", V1_df[D1:].corrwith(HperB_df[D1:]))
    print("Corr V1 H/C per B:\n", V1_df[D1:].corrwith(HperCperB_df))
    print("Corr V1 C per B mean:\n", V1_df[D1:].corrwith(CperB_df[D1:]).mean())
    print("Corr V1 H per B mean:\n", V1_df[D1:].corrwith(HperB_df[D1:]).mean())
    print("Corr V1 H/C per B mean:\n", V1_df[D1:].corrwith(HperCperB_df).mean())



