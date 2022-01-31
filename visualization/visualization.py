# Visualizing imported data for better understanding of relations of data

import matplotlib.pyplot as plt, pandas as pd, datetime


from data.acc_covdata import C_Datensatz_erstellen, C_Data_per_bev
from data.acc_hospidata import H_Rate
from data.acc_vaccinedata import V_Datensatz_erstellen

C_Dict = C_Datensatz_erstellen()
V_Dict = V_Datensatz_erstellen()
standard_date_range = pd.date_range(datetime.date(2019, 6, 1),datetime.date(2022, 1, 16)).strftime('%Y-%m-%d').tolist()

def plot_data(V_Data, C_Data, date_range=standard_date_range):
    x = []
    y = []

# Für jedes Datum jeder lk_id in CData Neuinfektionen des LK auf Impfquote des BL des LK plotten
    for i in range (2):
        for lk_id in C_Data:
            for Date in C_Data[lk_id]:
                if int(lk_id/1000) in V_Data and Date in V_Data[int(lk_id/1000)] and Date in date_range:
                    x.append(V_Data[int(lk_id/1000)][Date][i])
                    y.append(C_Data[lk_id][Date])

        plt.plot(x, y, "rx", markersize=0.1)
        plt.xlim(0,1)
        plt.ylim(0)
        plt.savefig('line_plot_V' + str(i) + '.png', dpi=500)
        plt.show()
        x.clear(), y.clear()


def TimeRange (W):
    date_list = pd.date_range(datetime.date(W[0], W[1], W[2]), datetime.date(W[3], W[4], W[5])).strftime('%Y-%m-%d').tolist()
    return date_list




#plot_data(V_Dict, C_Dict)
W1 = [2020, 3, 1, 2020, 6, 1]
W2 = [2020, 6, 1, 2021, 3, 1]
W3 = [2021, 3, 1, 2022, 2, 16]
W2u3 = [2020, 6, 1, 2022, 2, 16]
#plot_data(V_Dict, C_Dict, TimeRange(W2u3))
plot_data(V_Dict, C_Data_per_bev(), TimeRange(W2))
plot_data(V_Dict, H_Rate(), TimeRange(W2))
plot_data(V_Dict, C_Data_per_bev(), TimeRange(W3))
plot_data(V_Dict, H_Rate(), TimeRange(W3))
plot_data(V_Dict, C_Data_per_bev(), TimeRange(W2u3))
plot_data(V_Dict, H_Rate(), TimeRange(W2u3))