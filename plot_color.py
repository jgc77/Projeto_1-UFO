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
    def plot_cbar(data, colormap='Blues', title='', xlabel='', ylabel='', rotation=0):
        # Criar um DataFrame com os dados
        df = pd.DataFrame(data, columns=['values'])

        # Ordenar os dados em ordem decrescente
        df_sorted = df.sort_values(by='values', ascending=False)

        # Obter o colormap
        cmap = cm.get_cmap(colormap)

        # Criar a figura e os eixos
        fig, ax = plt.subplots()

        # Plotar as barras com o degradê de cores
        bars = ax.bar(df_sorted.index, df_sorted['values'], color=cmap(df_sorted['values']/max(df_sorted['values'])))

        # Configurar título e rótulos dos eixos
        ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

        # Adicionar legenda de cores
        sm = plt.cm.ScalarMappable(cmap=cmap)
        sm.set_array(df_sorted['values'])
        cbar = plt.colorbar(sm, ax=ax)
        cbar.set_label(ylabel)

        # Rotacionar os rótulos do eixo x (opcional)
        plt.xticks(rotation=rotation)
