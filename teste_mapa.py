import pandas as pd
import streamlit as st
import numpy as np
import folium
import random
from folium.plugins import MarkerCluster
from folium import FeatureGroup
import geopandas as gpd
from streamlit_folium import folium_static

#Carregar dados
coor = pd.read_csv("planilha_teste.csv")

st.title("Pontos de Coleta - Eunápolis-BA")

# Plotando o gráfico
mapa_sp = folium.Map(location = [-16.3731, -39.5751],
                  tiles= 'Cartodbpositron',
                  zoom_start=13)
markerCluster = MarkerCluster().add_to(mapa_sp)

for i, row in coor.iterrows():
    lat = coor.at[i,'Latitude']
    lng = coor.at[i,'Longitude']

    iframe = folium.IFrame(('Nome do Local: '+ str(coor.at[i, 'Nome do Local']) + '<br>'+
                            'Tipo de Material: '+ str(coor.at[i,'Tipo de Material'])+ '<br>'
                            'Contato: ' + str('(73) 9 3281-5566')))

    popup = folium.Popup(iframe, min_width=300, max_width=350,)
    icon = folium.Icon(color='green', prefix = 'fa', icon = 'home')
    folium.Marker(location=[lat, lng],
                  icon=icon, popup=popup).add_to(markerCluster)
folium_static(mapa_sp,width=720, height=600)