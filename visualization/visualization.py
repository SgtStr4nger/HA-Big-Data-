# Visualizing imported data for better understanding of relations of data
from data.acc_covdata import C_Datensatz_erstellen, C_Data_per_bev
from data.acc_vaccinedata import V_Datensatz_erstellen
import matplotlib.pyplot as plt

from data.util import bev_to_Dict

C_Dict = C_Datensatz_erstellen()
V_Dict = V_Datensatz_erstellen()


def plot_data(V_Data, C_Data):
    x = []
    y = []

# Für jedes Datum jeder lk_id in CData Neuinfektionen des LK auf Impfquote des BL des LK plotten
    for i in range (2):
        for lk_id in C_Data:
            for Date in C_Data[lk_id]:
                if int(lk_id/1000) in V_Data and Date in V_Data[int(lk_id/1000)]:
                    x.append(V_Data[int(lk_id/1000)][Date][i])
                    y.append(C_Data[lk_id][Date])

        plt.plot(x, y, "r+", markersize=0.1)
        plt.savefig('line_plot_V' + str(i) + '.png', dpi=500)
        plt.show()
        x.clear(), y.clear()








plot_data(V_Dict, C_Dict)
plot_data(V_Dict, C_Data_per_bev(C_Dict, bev_to_Dict()))