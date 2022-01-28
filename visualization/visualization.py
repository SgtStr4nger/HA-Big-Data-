# Visualizing imported data for better understanding of relations of data
from data.acc_covdata import C_Datensatz_erstellen
from data.acc_vaccinedata import V_Datensatz_erstellen
import matplotlib.pyplot as plt


C_Dict = C_Datensatz_erstellen()
V_Dict = V_Datensatz_erstellen()


def plot_data(V_Data, C_Data):
    x = []
    y = []

    for lk_id in V_Data:
        for Date in V_Data[lk_id]:
            if lk_id in C_Data and Date in C_Data[lk_id]:
                x.append(V_Data[lk_id][Date][0])
                y.append(C_Data[lk_id][Date])


    plt.plot(x, y, "r+" , markersize= 0.1)
    plt.savefig('line_plot_hq.png', dpi=500)
    plt.show()





plot_data(V_Dict, C_Dict)