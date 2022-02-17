# Using k-means clustering
import math
import openpyxl
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#from data_analysis.data_preparation import Load_C_Data
from matplotlib import pyplot as plt

cluster_count = 16

def prepareDF():
    try:
        C_Data = pd.read_pickle('../data_analysis/C_Data.pkl')
    except IOError:
        print("File could not be found, creating file now...")
        #C_Data = Load_C_Data()

    C_Data.index = pd.to_datetime(C_Data.index)
# Dropping Column 16056, filled with NULL → Eisenach, merged with Aachen? (to be proofed)
    C_Data = C_Data.drop(columns=[16056])
# Return Data beginning from 01.01.2020, first case 27.01.2020
    return C_Data[214:]

def PlotRawData(C_Data):
    plt.figure(figsize=(25, 10))
    C_Data.plot(legend=False, lw=0.25)
    plt.xlabel("Date", labelpad=0.25)
    plt.ylabel("New infections per 100k inhabitants", labelpad=15)
    plt.title("Raw infection data")
    plt.savefig('RawDataPlot.png', dpi=1000)
    plt.show()

def PlotMAData(C_Data):
    plt.figure(figsize=(25, 10))
    C_Data.plot(legend=False, lw=0.25)
    plt.xlabel("Date", labelpad=0.25)
    plt.ylabel("New infections per 7 days per 100k inhabitants", labelpad=15)
    plt.title("7 day moving average infection data")
    plt.savefig('MADataPlot.png', dpi=1000)
    plt.show()



def MovingAverage(df=prepareDF()):
    PlotRawData(df)
    df = df.rolling(7).mean()
    return df[6:]

def PlotNormData(C_Data):
    plt.figure(figsize=(25, 10))
    C_Data.plot(legend=False, lw=0.25)
    plt.xlabel("Date", labelpad=0.25)
    plt.ylabel("New infections per 7 days per 100k inhabitants", labelpad=15)
    plt.title("Normalized 7 day moving average infection data")
    plt.savefig('NormDataPlot.png', dpi=1000)
    plt.show()

def normalizeDF(df = MovingAverage()):
    PlotMAData(df)
    return (df-df.min())/(df.max()-df.min())

# Ab hier ist Auswertung

def transformDimensions (df=normalizeDF()):
    PlotNormData(df)
    pca = PCA(n_components=2)
    return pca.fit_transform(df.transpose())

def KMeans_on_df( df= transformDimensions(), df_base=MovingAverage()):
    kmeans = KMeans(n_clusters=cluster_count,init='k-means++', max_iter=10000)
    labels = kmeans.fit_predict(df)
    plt.figure(figsize=(10, 10))
    plt.scatter(df[:, 0], df[:, 1], c=labels, s=75)
    plt.title("KMeans++ on dimensional reduced data")
    plt.savefig('Clustering.png', dpi=1000)
    plt.show()

    plot_count = math.ceil(math.sqrt(cluster_count))
    fig, axs = plt.subplots(plot_count, plot_count, figsize=(25, 25))
    fig.suptitle('Clusters')
    row_i = 0
    column_j = 0

    for label in set(labels):
        cluster = []
        for i in range(len(labels)):
            if (labels[i] == label):
                axs[row_i, column_j].plot(df_base.iloc[:,i], c="gray", alpha=0.4,lw=0.25)
                cluster.append(df_base.iloc[:,i])
        if len(cluster) > 0:
            cluster_df = pd.concat(cluster, axis=1, keys=[s.name for s in cluster])
            axs[row_i, column_j].plot(cluster_df.mean(axis=1), c="red",lw=0.5)
        axs[row_i, column_j].set_title("Cluster "+str(column_j+(row_i*4)) )
        column_j += 1
        if column_j % plot_count == 0:
            row_i += 1
            column_j = 0
    plt.savefig('4x4_Cluster.png', dpi=1000)
    plt.show()
    ClusterDis(labels)
    ClusterTable(labels, df_base)

def ClusterDis(labels):
    cluster_c = [len(labels[labels == i]) for i in range(cluster_count)]
    cluster_n = ["Cluster " + str(i) for i in range(cluster_count)]
    plt.figure(figsize=(15, 5))
    plt.title("Cluster Distribution for KMeans++")
    plt.bar(cluster_n, cluster_c)
    for index, value in enumerate(cluster_c):
        plt.text(index, (value+0.5), str(value), ha="center")
    plt.savefig('ClusteringDistribution.png', dpi=1000)
    plt.show()

def ClusterTable(labels, df_base):
    label_names = [f"Cluster {label}" for label in labels]
    ClTable=pd.DataFrame(zip(list(df_base.columns.values), label_names), columns=["Series", "Cluster"]).set_index("Series")
    ClTable= ClTable.sort_values(["Cluster", "Series"])
    ClTable.to_csv("Clustering Table.csv")


#df = transformDimensions()

KMeans_on_df()
