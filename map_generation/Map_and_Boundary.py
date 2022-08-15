import pandas as pd
import folium
import json

center = (51.3823, -2.3512)
Bath_map = folium.Map(location=center, zoom_start=13)


caz_bound = "Lat_Long_data.geojson"

geo_bound = json.load(open(caz_bound))

layer = folium.GeoJson(data=geo_bound, name='Clean Air Zone').add_to(Bath_map)

data = pd.read_csv("Caz_road_Boundaries.csv")

for i in range(0, len(data)):
    folium.Marker(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
        popup=data.iloc[i]['Street_name'],
        icon=folium.Icon(color='lightred', icon='car', icon_color='white', prefix='fa')).add_to(Bath_map)

folium.LayerControl().add_to(Bath_map)
Bath_map.fit_bounds(layer.get_bounds())
Bath_map.save(outfile="Bath_CAZ_Roads.html")
