# -*- coding: utf-8 -*-
"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
UFO Sightings

@author: joaog

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

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

dt_ufo.sort_values('datetime', inplace=True) #Ordenar datetime do mais antigo para o mais recente.

# Numero de ocorrencias por ano
ocorrencias_ano = dt_ufo['year'].value_counts().sort_index() #contando as ocorrências por ano.

plt.figure(figsize=(10, 6))
plt.bar(ocorrencias_ano.index, ocorrencias_ano.values)
plt.xlabel('Ano')
plt.ylabel('Quantidade de Ocorrências')
plt.title('Ocorrências de UFOs por Ano')
plt.show()


#Horas
ocorrencias_hora = dt_ufo['hour'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(ocorrencias_hora.index, ocorrencias_hora.values)
plt.xlabel('Hora')
plt.ylabel('Quantidade de Ocorrências')
plt.title('Ocorrências de UFOs por Ano')
plt.show()

#Tipo do avistamento
tipo_ufo = dt_ufo['shape'].value_counts().sort_index()
tipo_ufoo = pd.DataFrame(tipo_ufo)
tipo_ufoo.sort_values('shape', inplace=True, ascending=False)

#mapa

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(10, 6),color='gray', edgecolor='white')
