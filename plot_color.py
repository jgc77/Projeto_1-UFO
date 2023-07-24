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
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        
        #plotar marcadores
        data_us.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='red', marker='.', s=20, edgecolor='b', linewidth=0.4)
    
    #Plotar grafico em pizza com distribuição de ocorrencias por continente 
    def c_ocorren(data):    
        def get_continent(latitude, longitude):
        
            #if pd.notna(latitude) and pd.notna(longitude):
                if -60 <= latitude <= 85 and ((-170 <= longitude <= -35) or (35 <= longitude <= 170)):
                    return 'Americas'
                elif -60 <= latitude <= 85:
                    return 'Eurasia'
                elif -60 <= latitude <= -35 and 30 <= longitude <= 150:
                    return 'Africa'
                elif -60 <= latitude <= 85 and -30 <= longitude <= 180:
                    return 'Europe'
                elif -60 <= latitude <= 85 and -180 <= longitude <= -90:
                    return 'Australia'
                return 'Other'
    
    
        data['continent'] = data.apply(lambda row: get_continent(row['latitude'], row['longitude']), axis=1)
        ocorrencias_por_continente = data['continent'].value_counts()

        plt.figure(figsize=(15, 15))
        ocorrencias_por_continente.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink', 'lightgray'])
        plt.title('Distribuição das Ocorrências de UFOs por Continente')
        plt.axis('equal')
