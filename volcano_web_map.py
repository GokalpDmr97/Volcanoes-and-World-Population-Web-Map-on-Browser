import folium
import pandas as pd

#Reading data
data = pd.read_csv("volcanoes.txt", error_bad_lines=False)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#Html file for Google search
html = """
        Volcano name:<br>
        <a href= "https://www.google.com/search?q=%%22%s%%22"
            target = "_blank">%s</a><br>
            Height: %s m
"""

#This function returns color of markers based on height of mountains. 
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif  1000 <= elevation < 3000:
        return 'yellow'
    elif  3000 <= elevation < 5000:
        return 'orange'
    else:
        return 'red'
    


my_map = folium.Map(location = [36.99136,30.63978], zoom_start = 4, tiles="Stamen Terrain")

#To make 2 different layer for volcanoes and population, two FeatureGroup is created. 
#Volcanoes FeatureGroup

fgv = folium.FeatureGroup(name="Volcanoes") 

for lt,ln,el,nm in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html = html % (nm,nm,el),width=200, height = 100)
    fgv.add_child(folium.CircleMarker(location =(lt,ln),popup=folium.Popup(iframe),fill_color=color_producer(el), fill=True, fill_opacity = 0.7, color = 'grey', radius = 6))


#Population FeatureGroup
fgp = folium.FeatureGroup(name="Population") 
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


my_map.add_child(fgv)
my_map.add_child(fgp)
my_map.add_child(folium.LayerControl())
my_map.save("world_map.html")
