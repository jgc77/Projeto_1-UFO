# -*- coding: utf-8 -*-
"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
UFO Sightings

@author: joaog

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Carregar dataset
dt_ufo = pd.read_csv('C:\\Users\\joaog\\Documents\\UPE\\LPAA\\Projeto\\Datasets\\scrubbed.csv')
dt_ufo.info

# Convertendo as datas para o modo datetime
dt_ufo['datetime'] = pd.to_datetime(dt_ufo['datetime'], errors='coerce')
dt_ufo['date posted'] = pd.to_datetime(dt_ufo['date posted'], errors='coerce')
