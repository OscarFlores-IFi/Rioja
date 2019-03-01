# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:18:14 2019

@author: if715029
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy as hi
import scipy.spatial.distance as sc

#%%
#rioja = pd.read_excel('../Data/la_rioja21-02-2019.xlsx',index_col='href')
rioja_no_duplicados = pd.read_excel('../Data/la_rioja21-02-2019.xlsx').iloc[:-2,:-1].dropna()

#%%
datos = rioja_no_duplicados.iloc[:,2:-1]
#%%
datos = (datos-datos.mean(axis=0))/datos.std(axis=0)
#%%
data = datos.values
for i in range(len(datos)):
    for j in range(len(datos)):
        if data[i].any() == data[j].any():
            if j != i:
                print([i,j])

#%%
Z = hi.linkage(datos,method='single',metric='euclidean')
#Z = sc.squareform(sc.pdist(datos))

#%%
plt.figure(figsize=(25,8))
plt.title('Dendograma')
plt.xlabel('Indice')
plt.ylabel('Distancia')
hi.dendrogram(Z)
plt.show()


























