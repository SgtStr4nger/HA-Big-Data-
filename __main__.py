from data_analysis.data_preparation import Create_C_Data, Create_H_Data
from data_analysis.kmeans_clustering import KMeans_on_df


try:
    f = open("data_analysis/C_Data.pkl")
except IOError:
    print("C_Data.pkl not accessible, creating now...")
    Create_C_Data()

try:
    f = open("data_analysis/H_Data.pkl")
except IOError:
    print("H_Data.pkl not accessible, creating now...")
    Create_H_Data()


Selection=["C", "H"]
for i in Selection:
    KMeans_on_df(i)