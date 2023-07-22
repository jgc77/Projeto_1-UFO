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
        
     
   #Função para plotar mapa    
    def mapa(data,eixo1, eixo2, xlabel, ylabel):
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        
        ax = world.plot(figsize=(20, 15),color='#B0C4DE', edgecolor='yellow')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        data.plot.scatter(x=eixo1, y=eixo2, ax=ax, color='red', s=1)
        
  