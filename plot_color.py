# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:34:08 2023

@author: joaog
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import geopandas as gpd
#from matplotlib.collections import LineCollection
#from matplotlib.colors import Normalize




class Plot_color:
    
    #Função para plotar em degrade
    def c_bar(data, colormap, title, xlabel, ylabel, rt, grid):
        
        #Definindo tamanho e dpi do gráfico
        plt.figure(figsize=(10, 6), dpi=300)
        
        # Normalização dos valores para [0, 1]
        norm_valores = (data - np.min(data)) / (np.max(data) - np.min(data))

        # Criação do gráfico de barras com degradê de cores
        plt.bar(data.index, data.values, color=colormap(norm_valores))
        
        #Legendas
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        
        # Adicionando legenda de cores (colorbar)
        sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=np.min(data), vmax=np.max(data)))
        sm._A = []  
        plt.colorbar(sm, ax=plt.gca(), pad=0.05)
        
        #Rotação
        plt.xticks(rotation=rt)
        plt.xticks(data.index[::2], data.index[::2])
        
    '''
    #Função para plotar em degrade
    def c_line(data):
        
        x = np.arange(len(data))  # Índices numéricos para representar as horas
        y = data["duration (seconds)"].values  # Valores da quantidade para cada hora

        # Calcula o primeiro derivado dos dados y
        dydx = np.gradient(y)

        # Criação dos pontos e das segmentos usando os arrays x e y
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        # Cria uma normalização para mapear os pontos para as cores do mapa de cores
        norm = Normalize(dydx.min(), dydx.max())
        lc = LineCollection(segments, cmap='viridis', norm=norm)
        lc.set_array(dydx)
        lc.set_linewidth(2)
        line = ax.add_collection(lc)
        fig.colorbar(line, ax=ax)
        plt.grid(True)
        

        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(y.min() - 38, y.max() + 38)  # Ajuste o limite vertical conforme necessário
        plt.show()
    '''
    
    #Função para plotar em barra
    def bar(data, cor, title ,xlabel, ylabel, rt, grid):
        
        #Definindo tamanho e dpi do gráfico
        plt.figure(figsize=(10, 6), dpi=300)
        
        #Criação do gráfico de barras
        plt.barh(data.index, data.values, color=cor)
        
        #Legendas
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(grid)

        #Rotação
        plt.xticks(rotation=rt)
        
    #Função para plotar em linha
    def linha(data, cor, title ,xlabel, ylabel, rt, grid):
        
        #Definindo tamanho e dpi do gráfico
        plt.figure(figsize=(10, 6), dpi=300)
        
        #Criação do gráfico de barras
        plt.plot(data.index, data.values, color=cor)
        
        #Legendas
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(grid)
        
        #Rotação
        plt.xticks(rotation=rt)
        
     
   #Função para plotar mapa mundi    
    def mapa(data,eixo1, eixo2):
        
        #importar mapa mundi
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        
        #plotar mapa mundi
        ax = world.plot(figsize=(40, 35),color='#DCDCDC', edgecolor='k')
        ax.set_facecolor('#B0C4DE')
               
        #legendas
        ax.set_xticks([])
        ax.set_yticks([])
        
        #plotar marcadores
        data.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='y', marker='.', s=30, edgecolor='b', linewidth=0.4)
    
    #Função para plotar mapa dos Estados Unidos 
    def mapa_us(data, eixo1, eixo2, xlabel, ylabel):
        
        #Filtar Estados Unidos de data
        data_us = data[data['country'] == 'us']
        
        #Importar mapa dos Estados Unidos
        usa_states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        usa_states = usa_states[usa_states['name'].isin(['United States of America'])]

        #plotar mapa dos Estados Unidos
        ax = usa_states.plot(figsize=(25, 20),color='#DCDCDC', edgecolor='k')
        ax.set_facecolor('#B0C4DE')

        #legendas
        ax.set_xticks([])
        ax.set_yticks([])
        
        #plotar marcadores
        data_us.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='red', marker='.', s=20, edgecolor='b', linewidth=0.4)
    
    #Plotar grafico em pizza com distribuição de ocorrencias por continente 
    def c_ocorren(data, colors, title, labels, explode):    
        
        plt.subplots(figsize=(18, 10))
        
        plt.pie(data, explode=explode, colors= colors, autopct='%1.1f%%', textprops={'fontsize': 22}, labels= None, shadow=None)
        
        plt.legend(labels=labels, loc='lower right')
        plt.title(title, fontsize = 20)
        plt.axis('equal')
        plt.xticks(rotation=45, fontsize=15)

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
