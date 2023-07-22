# -*- coding: utf-8 -*-
"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
UFO Sightings

@author: joaog

"""
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from plot_color import Plot_color


#from plot_colorful_barchart import Plot_color
    
#Carregar dataset
dt_ufo = pd.read_csv('C:\\Users\\joaog\\Documents\\UPE\\LPAA\\Projeto\\Datasets\\scrubbed.csv')
dt_ufo.info

# Convertendo dados e ordenando
dt_ufo['datetime'] = dt_ufo['datetime'].str.replace('24:00', '0:00') #alterando a hora 24:00 para 00:00.
dt_ufo['datetime'] = pd.to_datetime(dt_ufo['datetime'], errors='coerce') #convertendo a coluna datatime para datetime.

dt_ufo['year'] = pd.DatetimeIndex(dt_ufo['datetime']).year #Criando uma coluna year, para separar o ano.
dt_ufo['month'] = pd.DatetimeIndex(dt_ufo['datetime']).month #Criando uma coluna month, para separar o mês.
dt_ufo['day'] = pd.DatetimeIndex(dt_ufo['datetime']).day #Criando uma coluna day, para separar o dia.
dt_ufo['hour'] = pd.DatetimeIndex(dt_ufo['datetime']).hour #Criando uma coluna hour, para separar a hora.

dt_ufo['latitude'] = pd.to_numeric(dt_ufo['latitude'], errors='coerce') #convertendo a coluna latitude para numeros.
dt_ufo['date posted'] = pd.to_datetime(dt_ufo['date posted'], errors='coerce') #convertendo a coluna date posted para datetime.
dt_ufo['shape'] = dt_ufo['shape'].str.replace('Other', 'Other/Unknown') #retirando other, unknow do shape.
dt_ufo.sort_values('datetime', inplace=True) #Ordenar datetime do mais antigo para o mais recente.
dt_ufo.rename(columns={'longitude ': 'longitude'}, inplace = True)

#############################Avistamentos#####################################

# Numero de ocorrencias por ano
ocorrencias_ano = dt_ufo['year'].value_counts().sort_index() #contando as ocorrências por ano.
Plot_color.bar(ocorrencias_ano, 'green', 'Avistamento por Ano', 'Quantidade de ocorrências', 'Ano', 0, True)

#Horas com mais avistamentos
ocorrencias_hora = dt_ufo['hour'].value_counts().sort_index()
Plot_color.linha(ocorrencias_hora, 'red', 'Quantidade de Ufos por hora', 'Hora', 'Quantidade de ocorrências', 0, True)

#Tipos do avistamentos
ocorrencias_tipo = dt_ufo['shape'].value_counts().head(15)
Plot_color.c_bar(ocorrencias_tipo, cm.inferno, 'Tipos de avistamentos', 'Tipo do avistamento', 'Quantidade', 45, False)

#Mapa de disperção
Plot_color.mapa(dt_ufo,'longitude', 'latitude')
Plot_color.mapa_us(dt_ufo,'longitude', 'latitude', 'longitude', 'latitude')



