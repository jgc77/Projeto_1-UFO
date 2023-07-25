# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:34:08 2023

Autor: joaog
"""
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd


class Plot_color:
    
    # Função para plotar gráfico de barras com degradê de cores
    def c_bar(data, colormap, title, xlabel, ylabel, rotation, grid, x_tick_jump, leg, media):
        plt.figure(figsize=(10, 6), dpi=300)
        norm_valores = (data - np.min(data)) / (np.max(data) - np.min(data))
        plt.bar(data.index, data.values, color=colormap(norm_valores))
        if media == True:
            mean_value = np.mean(data.values)
            plt.legend([f'Média: {mean_value:.1f}h'], loc= leg, fontsize=12)
        plt.title(title,fontsize=15)
        plt.xlabel(xlabel,fontsize=12)
        plt.ylabel(ylabel,fontsize=12)
        plt.grid(grid)
        sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=np.min(data), vmax=np.max(data)))
        sm._A = []
        plt.colorbar(sm, ax=plt.gca(), pad=0.05)
        plt.xticks(rotation=rotation)
        plt.xticks(data.index[::x_tick_jump], data.index[::x_tick_jump])

    # Função para plotar gráfico de barras
    def barh(data, cor, title ,xlabel, ylabel, rotation, grid, y_tick_jump):
        plt.figure(figsize=(10, 6), dpi=300)
        plt.barh(data.index, data.values, color=cor)
        mean_value = np.mean(data.values)
        plt.legend([f'Média: {mean_value:.2f}'], loc='center right', fontsize=12)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(title, fontsize=15)
        plt.grid(grid)
        plt.xticks(rotation=rotation)
        plt.yticks(data.index[::y_tick_jump], data.index[::y_tick_jump])

    # Função para plotar gráfico de linhas
    def linha(data, cor, title ,xlabel, ylabel, rotation, grid):
        plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(data.index, data.values, color=cor)
        moda_value = np.argmax(data.index)
        plt.legend([f'Moda: {moda_value:}h'], loc='upper left', fontsize=12)
        plt.xlabel(xlabel,fontsize=12)
        plt.ylabel(ylabel,fontsize=12)
        plt.title(title,fontsize=15)
        plt.grid(grid)
        plt.xticks(rotation=rotation)


    # Função para plotar mapa mundi
    def mapa(data,eixo1, eixo2):
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        ax = world.plot(figsize=(40, 35), color='#DCDCDC', edgecolor='k')
        ax.set_facecolor('#B0C4DE')
        plt.xlabel('Longitude', fontsize = 30)
        plt.ylabel('Latitude', fontsize = 30)
        plt.title('Mapa Mundi', fontsize = 40)
        data.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='y', marker='.', s=35, edgecolor='r', linewidth=0.4)

    # Função para plotar mapa dos Estados Unidos
    def mapa_us(data, eixo1, eixo2, xlabel, ylabel):
        data_us = data[data['country'] == 'us']
        usa_states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        usa_states = usa_states[usa_states['name'].isin(['United States of America'])]
        ax = usa_states.plot(figsize=(25, 20), color='#DCDCDC', edgecolor='k')
        ax.set_facecolor('#B0C4DE')
        plt.xlabel('', fontsize = 20)
        plt.ylabel('', fontsize = 20)
        plt.title('EUA', fontsize = 40)
        data_us.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='red', marker='.', s=20, edgecolor='b', linewidth=0.4)

    # Função para plotar gráfico de pizza
    def c_ocorren(data, colors, title, labels, explode):
        plt.subplots(figsize=(22, 14))
        plt.pie(data, explode=explode, colors= colors, autopct='%1.1f%%', textprops={'fontsize': 22}, pctdistance=0.83, labels= None, shadow=None)
        plt.legend(labels=labels, loc='lower right', fontsize = 15)
        plt.title(title, fontsize = 29)
        plt.axis('equal')
        plt.xticks(rotation=45, fontsize=15)

    # Dicionario para siglas de estado do USA
    def dici_state(data):
        estados = {
            'ca': 'California',
            'wa': 'Washington',
            'fl': 'Florida',
            'tx': 'Texas',
            'ny': 'New York',
            'az': 'Arizona',
            'il': 'Illinois',
            'pa': 'Pennsylvania',
            'oh': 'Ohio',
            'mi': 'Michigan',
            'nc': 'North Carolina',
            'or': 'Oregon',
            'mo': 'Missouri',
            'nj': 'New Jersey',
            'co': 'Colorado',
            'va': 'Virginia',
            'o' : 'Outros'
        }
        
        data.index = data.index.map(estados)
        return data
