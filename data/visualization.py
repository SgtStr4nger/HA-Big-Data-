# Visualizing imported data for better understanding of relations of data
from Datapreparation import create_dict
import matplotlib.pyplot as plt

def plot_data(data):
    x, y = zip(*sorted(data.items()))
    plt.plot(x, y )
    plt.show()


vDict, cDict = create_dict()

plot_data(cDict[1001])