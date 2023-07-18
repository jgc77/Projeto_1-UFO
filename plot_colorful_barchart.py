# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:34:08 2023

@author: joaog
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Plot_color:
    def plot_cbar(self, data, colormap='Blues', title='', xlabel='', ylabel='', rotation=0):
        # Ordenar os dados em ordem decrescente
        data_sorted = data.sort_values(ascending=False)

        # Obter o colormap
        cmap = cm.get_cmap(colormap)

        # Criar a figura e os eixos
        fig, ax = plt.subplots()

        # Plotar as barras com o degradê de cores
        bars = ax.bar(data_sorted.index, data_sorted.values, color=cmap(data_sorted.values/max(data_sorted.values)))

        # Configurar título e rótulos dos eixos
        ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

        # Adicionar legenda de cores
        sm = plt.cm.ScalarMappable(cmap=cmap)
        sm.set_array(data_sorted.values)
        cbar = plt.colorbar(sm, ax=ax)
        cbar.set_label(ylabel)

        # Rotacionar os rótulos do eixo x (opcional)
        plt.xticks(rotation=rotation)
