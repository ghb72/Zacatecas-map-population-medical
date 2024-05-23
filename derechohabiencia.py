import pandas as pd
import requests
import plotly.express as px

df = pd.read_csv('derechohabiencia_32.csv')

salud = df[df['indicador']=='Porcentaje de Poblacion afiliada a servicios de salud']
salud.index = salud['cve_municipio']
year2020_salud = salud['2020']

import requests
import plotly.express as px

repo_url = 'https://raw.githubusercontent.com/PhantomInsights/mexico-geojson/main/2022/states/Zacatecas.json' #Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()


fig1 = px.choropleth(data_frame=salud,
                    geojson=mx_regions_geo,
                    locations='desc_municipio',
                    featureidkey='properties.NOMGEO',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='2020',
                    color_continuous_scale="burg",
                   )

fig1.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
fig1.update_geos(fitbounds="locations", visible=False)

fig1.update_layout(
    margin={"r":0,"t":40, "l":0,"b":0.5},
    font_family="Bahnschrift",
    title_text = 'PORCENTAJE DE POBLACIÓN AFILIADA <br> A SERVICIOS DE SALUD',
    template="plotly_dark",
    annotations = [dict(
        x=0,
        y=0,
        xref='paper',
        yref='paper',
        text='Fuente: <a href="https://www.inegi.org.mx/programas/ccpv/2020/"> Censos y Conteos de Población y Vivienda Inegi 2020 </a>',
        showarrow = False
    ),
    ],
    title=dict(text='Porcentaje de Poblacion afiliada a servicios de salud', font=dict(size=35), automargin=True, y=1, yref='paper')
)


fig1.add_annotation(
    text='Para el 2020 el 79.7 % <br>\
de la población de Zacatecas estaba afiliada a algún <br>\
servicio de salud. De la cual solo el 1.1 % estaba <br>\
afiliada a Servicios del Bienestar, el 40% al IMSS, <br>\
el 8.8% al ISSSTE, 49% al seguro popular, 0.6 % a <br>\
privado, el 0.38 % a SS de PEMEX, Defensa o Marina.',
    x = 0.05,
    y = 0.7,
    xref='paper',
    yref='paper',
    showarrow=False,
    font=dict(
            size=18
            )
    )

fig1.show()