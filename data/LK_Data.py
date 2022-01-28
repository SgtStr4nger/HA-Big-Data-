# Everything related LK, LK_ID

import util

bevData = util.bev_to_Dict()

#Accumulate BevData from all LK
def DictBevBundesland():
    BBev_Dict = {}
    for i in range (1,17):
        BBev_Dict[i]=0
        for lk_id in bevData:
            if int(lk_id/1000)==i:
                BBev_Dict.update({i: (BBev_Dict[i]+bevData[lk_id]) })
    return BBev_Dict

DictBev = DictBevBundesland()
