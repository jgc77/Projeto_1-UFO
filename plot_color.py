# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:34:08 2023

@author: joaog
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd



class Plot_color:
    def c_bar(data, colormap, title, xlable, ylable):
        
        
        # Normalização dos valores para [0, 1]
        norm_valores = (data - np.min(data)) / (np.max(data) - np.min(data))


        # Criação do gráfico de barras com degradê de cores
        plt.bar(data.index, data.values, color=colormap(norm_valores))
        
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)