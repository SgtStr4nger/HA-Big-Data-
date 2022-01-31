# Preparing data for analysis
from collections import defaultdict

import pandas as pd

from data.acc_covdata import C_Datensatz_erstellen, C_Data_per_bev
from data.acc_hospidata import H_Rate
from data.acc_vaccinedata import V_Datensatz_erstellen, V_Dict_LK

CperB_df =pd.DataFrame.from_dict(C_Data_per_bev(),orient='columns')

HperB_df =pd.DataFrame.from_dict(H_Rate(),orient='columns')




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






D1= 710
print(CperB_df[D1:])
V1_df, V2_df =DF_V()
print(HperB_df[D1:])

print(V1_df[D1:].corrwith(CperB_df[D1:]))
print(V1_df[D1:].corrwith(HperB_df[D1:]))
#print(CperB_df.corrwith(HperB_df))