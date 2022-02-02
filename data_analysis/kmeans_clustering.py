# Using k-means clustering
import math

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#from data_analysis.data_preparation import Load_C_Data
from matplotlib import pyplot as plt

cluster_count = 16
pd.set_option('display.max_rows', 20)

def prepareDF():
    try:
        C_Data = pd.read_pickle('../data_analysis/C_Data.pkl')
    except IOError:
        print("File could not be found, creating file now...")
        #C_Data = Load_C_Data()

    C_Data.index = pd.to_datetime(C_Data.index)
# Dropping Column 16056, filled with NULL
    C_Data = C_Data.drop(columns=[16056])
    return C_Data

def MovingAverage(df=prepareDF()):
    df = df.rolling(7).mean()
    return df[6:]

def normalizeDF(df = MovingAverage()):
    return (df-df.min())/(df.max()-df.min())

def transformDimensions (df=normalizeDF()):
    print("Normalized df:",df)
    pca = PCA(n_components=2)
    return pca.fit_transform(df.transpose())

def KMeans_on_df( df= transformDimensions(), df_base=MovingAverage()):
    kmeans = KMeans(n_clusters=cluster_count, max_iter=5000)
    print('transforemd df:\n', df,'\nLength:', len(df))
    labels = kmeans.fit_predict(df)
    plt.figure(figsize=(25, 10))
    plt.scatter(df[:, 0], df[:, 1], c=labels, s=300)
    plt.savefig('Clustering.png', dpi=1000)
    plt.show()

    plot_count = math.ceil(math.sqrt(cluster_count))
    fig, axs = plt.subplots(plot_count, plot_count, figsize=(25, 25))
    fig.suptitle('Clusters')
    row_i = 0
    column_j = 0

    print(len(labels))
    for label in set(labels):
        print(label)
        cluster = []
        for i in range(len(labels)):
            if (labels[i] == label):
                axs[row_i, column_j].plot(df_base.iloc[:,i], c="gray", alpha=0.4)
                cluster.append(df_base.iloc[:,i])
        if len(cluster) > 0:
            cluster_df = pd.concat(cluster, axis=1, keys=[s.name for s in cluster])
            print(cluster_df)
            print(cluster_df.mean(axis=1))
            axs[row_i, column_j].plot(cluster_df.mean(axis=1), c="red")
            #axs[row_i, column_j].plot(np.average(cluster_df, axis=1), c="red")
        axs[row_i, column_j].set_title("Cluster"+str(column_j+(row_i*4)) )
        column_j += 1
        if column_j % plot_count == 0:
            row_i += 1
            column_j = 0
    plt.savefig('4x4_Cluster.png', dpi=1000)
    plt.show()

df = transformDimensions()

KMeans_on_df(df)
