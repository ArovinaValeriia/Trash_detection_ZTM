from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource
from bokeh.palettes import Set3
from bokeh.palettes import Category20
from bokeh.palettes import RdBu3
from bokeh.resources import CDN
from bokeh.embed import file_html
import streamlit.components.v1 as components
import streamlit as st
import requests
import json

bokeh_width, bokeh_height = 1024,768
GOOGLE_API_KEY = 'poh'
RESIDENCE_LATLONG = []
BUSINESS_LATLONG = []
customer = [] # ideally this thing has addres

def addres_to_geolocation():
    GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='+customer['address'][0]+'&key='+GOOGLE_API_KEY
    geo_response = requests.request("GET", GEOCODE_URL)
    geodata = json.loads(geo_response.text)
    try:
        print(geodata['results'][0]['geometry']['location'])
        latlong = [geodata['results'][0]['geometry']['location']['lat'],geodata['results'][0]['geometry']['location']['lng']]
    except IndexError:
        latlong = None
        st.write('latlong not found')
    return latlong

def plotAll(data, zoom=15, map_type='roadmap'):
    gmap_options = GMapOptions(lat=data[0][1], lng=data[0][2], 
                               map_type=map_type, zoom=zoom)
    p = gmap(GOOGLE_API_KEY, gmap_options, title='AwanTunai - Risk Intelligence', 
             width=bokeh_width, height=bokeh_height)
    
    latArr = []
    longArr = []
    colorArr = []
    labelArr = []
    colidx = 0
    colpalette = Category20.get(20)
    print('palette length: ', len(Set3))
    
    for x in data:
        if(x[4] == 'Stationary'):
          latArr.append(x[1])
          longArr.append(x[2])
          labelArr.append(x[3])
          if(colidx == len(colpalette)):
              colidx=0
          colorArr.append(colpalette[colidx])
          colidx+=1
    
    print('latArr: ', latArr)
    print('longArr: ', longArr)
    print('colorArr: ', colorArr)
    print('label: ', labelArr)
    
    source = ColumnDataSource(dict(
                x=longArr,
                y=latArr,
                color=colorArr,
                label=labelArr
            ))
    
    center = p.circle(x='x', y='y', size=10, alpha=0.9, color='color', legend_group='label', source=source)
    
    if RESIDENCE_LATLONG is not None:
        p.triangle([RESIDENCE_LATLONG[1]], [RESIDENCE_LATLONG[0]], size=10, alpha=0.9, color='red')
    if BUSINESS_LATLONG is not None:
        p.triangle([BUSINESS_LATLONG[1]], [BUSINESS_LATLONG[0]], size=10, alpha=0.9, color='blue')
    html = file_html(p, CDN, "User locations")
    return html

data = []

if len(data) > 0:
    components.html(plotAll(data, 15, 'satellite'), height = bokeh_height + 100, width = bokeh_width + 100)
else:
    st.write('no location data found')