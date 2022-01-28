# Everything related LK, LK_ID

from data.acc_vaccinedata import bev_to_Dict

bevData = bev_to_Dict()

#Accumulate BevData from all LK
def DictBevBundesland():
    BBev_Dict = {}
    for i in range (1,17):
        for lk_id in bevData:
            if int(lk_id/1000)==i:
                BBev_Dict[i]=bevData[lk_id]
    return BBev_Dict


print(DictBevBundesland())